#!/usr/bin/env python3

import argparse
import os
from shpc.main import get_client
from container_guts.main import ManifestGenerator
import shpc.utils

here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(os.path.dirname(here))


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Container Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("image", help="Container URI to add")
    parser.add_argument("--registry", help="Path to registry root.", default=root)
    parser.add_argument("--maintainer", help="Author", default="@vsoch")
    parser.add_argument("--url", help="URL for package")
    parser.add_argument("--description", help="Description for the container")
    return parser


def main():
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("       image: %s" % args.image)
    print("    registry: %s" % args.registry)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    module_name = args.image.split(":")[0]
    container_yaml = cli.add(args.image, module_name)
    container = shpc.utils.read_yaml(container_yaml)

    if args.maintainer:
        container["maintainer"] = args.maintainer
    if args.description:
        container["description"] = args.description
    if args.url:
        container["url"] = args.url

    # Generate guts
    cli = ManifestGenerator()
    manifests = cli.diff(args.image)

    # Assemble aliases
    aliases = {}
    for path in list(manifests.values())[0]["diff"]["unique_paths"]:
        # Don't include system bin
        if "sbin" in path or "/usr/bin" in path:
            print(f"Skipping system bin {path}")
            continue

        name = os.path.basename(path)
        if name in aliases:
            print(f"Warning, duplicate alias {name}")
        aliases[name] = path

    container["aliases"] = aliases
    print(f"Writing with aliases to {container_yaml}")
    shpc.utils.write_yaml(container, container_yaml)
    print(f"container_yaml={container_yaml} >> $GITHUB_OUTPUT")


if __name__ == "__main__":
    main()
