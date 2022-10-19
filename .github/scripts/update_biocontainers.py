#!/usr/bin/env python3

import argparse
import os
from shpc.main import get_client
from container_guts.main import ManifestGenerator
import shpc.utils
import shutil
import requests
import re
import glob
from bs4 import BeautifulSoup

import pipelib.steps as step
import pipelib.pipeline as pipeline

# Pre-generated sets of steps we can use
import pipelib.pipelines as pipelines


here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(os.path.dirname(here))


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC BioContainer Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--registry", help="Path to registry root.", default=root)
    parser.add_argument("--maintainer", help="Author", default="@vsoch")
    parser.add_argument(
        "--cache",
        help="cache to save container aliases",
        default=os.path.join(root, ".cache"),
    )
    return parser


# A pipeline to process docker tags
steps = (
    # Scrub commits from version string
    step.filters.CleanCommit(),
    # Parse versions, return sorted ascending, and taking version major.minor.patch into account
    step.container.ContainerTagSort(),
)
p = pipeline.Pipeline(steps)


def get_tags(links, registry):
    uris = {}

    # Use the latest for each unique
    for link in links:
        if ":" not in link.text:
            continue
        image, tag = link.text.split(":", 1)

        # If we already have the registry folder, skip
        container_dir = os.path.join(registry, "quay.io", "biocontainers", image)
        if image in uris or os.path.exists(container_dir):
            continue

        print(f"Retrieving tags for {image}")
        tags = requests.get(f"https://crane.ggcr.dev/ls/quay.io/biocontainers/{image}")
        uris[image] = [x for x in tags.text.split("\n") if x]
    return uris


def main():

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("  maintainer: %s" % args.maintainer)
    print("    registry: %s" % args.registry)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    response = requests.get("https://depot.galaxyproject.org/singularity/")
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    # Allow developer to provide tags in root
    tags_json = os.path.join(root, "tags.json")
    if os.path.exists(tags_json):
        uris = shpc.utils.read_json(tags_json)
    else:
        uris = get_tags(links, args.registry)

    # Ensure our alias cache exists
    if not os.path.exists(args.cache):
        shpc.utils.mkdir_p(args.cache)

    # Keep track of counts
    counts = {}

    # For each uri, get latest version
    for uri, tags in uris.items():

        container_dir = os.path.join(args.registry, "quay.io", "biocontainers", uri)
        if "UNAUTHORIZED" in tags[0] or os.path.exists(container_dir):
            continue

        # The updated and transformed items
        ordered = p.run(list(tags), unwrap=False)
        if not ordered:
            continue

        tag = ordered[0]._original
        container = f"quay.io/biocontainers/{uri}:{tag}"
        try:
            aliases = cache_aliases(container, args.cache, uri, tag)
        except:
            for path in glob.glob("/tmp/guts*"):
                shutil.rmtree(path)
            continue

        for alias, _ in aliases.items():
            if alias not in counts:
                counts[alias] = 0
            counts[alias] += 1

    import IPython

    IPython.embed()
    sys.exit()

    # Finally, use cache to write aliases to container.yaml
    for uri, tags in uris.items():

        container_dir = os.path.join(args.registry, "quay.io", "biocontainers", uri)
        if "UNAUTHORIZED" in tags[0] or os.path.exists(container_dir):
            continue

        # The updated and transformed items
        ordered = p.run(list(tags), unwrap=False)
        if not ordered:
            continue
        tag = ordered[0]._original
        container = f"quay.io/biocontainers/{uri}:{tag}"

        # First derive and save the aliases - we can filter based
        add_container(cli, container, args.maintainer, uri, cache=args.cache)


def include_path(path):
    """
    Filter out binaries that are in system bins.
    """
    return "sbin" not in path and "/usr/bin" not in path and not path.startswith("/bin")


def cache_aliases(container, cache, uri, tag):
    """
    Keep a cache of aliases to use later
    """
    letter = uri[0].lower()
    filename = os.path.join(
        cache, "quay.io", "biocontainers", letter, "%s:%s.json" % (uri, tag)
    )
    prefix = os.path.join(cache, "quay.io", "biocontainers", letter, "%s*" % uri)

    # Any glob of the container
    if os.path.exists(filename) or glob.glob(prefix):
        return shpc.utils.read_json(filename)

    # Generate guts
    gen = ManifestGenerator()
    manifests = gen.diff(container)

    # Assemble aliases
    aliases = {}
    for path in list(manifests.values())[0]["diff"]["unique_paths"]:
        name = os.path.basename(path)
        if not include_path(path):
            continue

        if name in aliases:
            print(f"Warning, duplicate alias {name}")
        print(path)
        aliases[name] = path

    parent = os.path.dirname(filename)
    shpc.utils.mkdir_p(parent)
    print(f"Writing {filename} with aliases")
    shpc.utils.write_json(aliases, filename)
    return aliases


def add_container(cli, container, maintainer, entry_name):
    """
    Add a container from a unique resource identifier.
    """
    print(f"Generating container entry for {container}")
    module_name = container.split(":")[0]
    container_yaml = cli.add(image="docker://" + container, module_name=module_name)

    # First clean up commented lines - not intended for automation
    toclean = shpc.utils.read_file(container_yaml).split("\n")
    lines = [x for x in toclean if not (x.strip().startswith("#") or not x.strip())]
    shpc.utils.write_file(container_yaml, "\n".join(lines))

    # Now read in as yaml (without comments)
    result = shpc.utils.read_yaml(container_yaml)
    result["maintainer"] = maintainer
    result[
        "description"
    ] = f"shpc-registry automated BioContainers addition for {entry_name}"
    result["url"] = f"https://biocontainers.pro/tools/{entry_name}"

    try:

        # Generate guts
        gen = ManifestGenerator()
        manifests = gen.diff(container)

        # Assemble aliases
        aliases = {}
        for path in list(manifests.values())[0]["diff"]["unique_paths"]:
            name = os.path.basename(path)
            if not include_path(path, name):
                continue

            if name in aliases:
                print(f"Warning, duplicate alias {name}")
            print(path)
            aliases[name] = path

        result["aliases"] = aliases
        print(f"Writing with aliases to {container_yaml}")
    except:
        pass

    shpc.utils.write_yaml(result, container_yaml)


if __name__ == "__main__":
    main()
