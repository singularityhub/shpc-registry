#!/usr/bin/env python3

# This script uses count data from https://github.com/singularityhub/shpc-registry-cache
# to:

# - Subsetting to those in a container, including counts
# - Rank ordering from least to greatest (lower frequency is a more unique command)
# - Including any counts with a frequency < 10
# - Above that, including the next N
# - Use these to generate a new container.yaml for the file (if it does not exist yet)

# It requires a local clone of shpc-registry-cache with a counts file available,
# along with a json file with commands found there.
# Usage:
# python .github/scripts/update_biocontainers.py --cache ../shpc-registry-cache --registry $PWD

import argparse
import os
import collections
from shpc.main import get_client
import shpc.utils
import sys
import requests

from bs4 import BeautifulSoup

import pipelib.steps as step
import pipelib.pipeline as pipeline


# A pipeline to process docker tags
steps = (
    # Scrub commits from version string
    step.filters.CleanCommit(),
    # Parse versions, return sorted ascending, and taking version major.minor.patch into account
    step.container.ContainerTagSort(),
)
p = pipeline.Pipeline(steps)


here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(os.path.dirname(here))


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC BioContainer Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--cache", help="Path to cache with counts.json.")
    parser.add_argument("--registry", help="Path to registry root.", default=root)
    parser.add_argument("--maintainer", help="Author", default="@vsoch")
    parser.add_argument(
        "--min-count-inclusion", help="Author", default=10, type=int, dest="min_count"
    )
    parser.add_argument(
        "--additional-count-inclusion",
        help="Author",
        default=25,
        type=int,
        dest="add_count",
    )
    return parser


def include_path(path):
    """
    Various manual filters
    """
    for ending in [
        "post-link.sh",
        ".debug",
        "pre-link.sh",
        ".so",
        ".dll",
        ".gz",
        ".dna",
        ".dox",
        ".db",
        ".db3",
        ".config",
        ".defaults",
        ".dat",
        ".dn",
        ".d",
    ]:
        if path.endswith(ending):
            return False
    return True


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
    counts = os.path.join(args.cache, "counts.json")

    for path in args.registry, args.cache:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist")

    # Read in counts
    counts = shpc.utils.read_json(counts)

    # Keep track of those we've seen in the cache
    seen = set()

    # For each entry in the cache (which might not be in our registry) check for it!
    for entry in shpc.utils.recursive_find(
        os.path.join(args.cache, "quay.io"), ".json"
    ):
        # Reset addition count
        add_count = args.add_count

        # We really only need the container uri,
        basename = os.path.basename(entry)
        image, tag = basename.replace(".json", "").split(":", 1)
        seen.add(image)
        image = "quay.io/biocontainers/%s" % image

        container_dir = os.path.join(args.registry, image)
        if os.path.exists(container_dir):
            continue

        print(f"Image {image} found in cache and not in registry!")
        aliases = shpc.utils.read_json(entry)

        # Look up counts and always take the number under a threshold (10)
        keepers = {}
        for x, path in aliases.items():

            # Always take the very unique ones!
            if counts[x] <= args.min_count and include_path(path):
                keepers[x] = path

        # of the remaining we have, sorted by count, keep top N (lower numbers == more unique)
        alias_counts = {x: counts[x] for x in aliases if x not in keepers}

        # Lowest to highest
        sorted_counts = list(collections.OrderedDict(alias_counts))

        while add_count > 0 and sorted_counts:
            keeper = sorted_counts.pop(0)
            if include_path(keeper):
                keepers[keeper] = aliases[keeper]
                add_count -= 1

        for alias, _ in aliases.items():
            if alias not in counts:
                counts[alias] = 0
            counts[alias] += 1

        # Now add the container, and use the tag
        container = f"{image}:{tag}"
        entry_name = image.split(os.sep)[-1]

        # First derive and save the aliases - we can filter based
        try:
            add_container(cli, container, args.maintainer, entry_name, aliases=keepers)
        except:
            print(f"Issue adding container {container}")

    # Now add those not yet seen!
    print(f"Found {len(seen)} containers already added.")
    response = requests.get("https://depot.galaxyproject.org/singularity/")
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    uris = get_tags(links, seen)

    # For each uri, get latest version of tags not an error
    for uri, tags in uris.items():

        if "UNAUTHORIZED" in tags[0]:
            continue

        # The updated and transformed items
        try:
            ordered = p.run(list(tags), unwrap=False)
        except:
            continue

        if not ordered:
            continue

        tag = ordered[0]._original
        container = f"quay.io/biocontainers/{uri}:{tag}"

        # We don't have aliases here
        try:
            add_container(cli, container, args.maintainer, uri, aliases=[])
        except:
            print(f"Issue adding container {container}")


def get_tags(links, seen):
    uris = {}

    # Use the latest for each unique
    for link in links:
        if ":" not in link.text:
            continue
        image, tag = link.text.split(":", 1)
        if image in seen or image in uris:
            continue
        print(f"Retrieving tags for {image}")
        tags = requests.get(f"https://crane.ggcr.dev/ls/quay.io/biocontainers/{image}")
        uris[image] = [x for x in tags.text.split("\n") if x]
    return uris


def add_container(cli, container, maintainer, entry_name, aliases):
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
    if aliases:
        result["aliases"] = aliases
    shpc.utils.write_yaml(result, container_yaml)


if __name__ == "__main__":
    main()
