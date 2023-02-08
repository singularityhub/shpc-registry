#!/usr/bin/env python3

import argparse
import os
import sys
from shpc.main import get_client

here = os.getcwd()


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Alias Updater",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        description="add an alias to a container recipe.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    remove = subparsers.add_parser(
        "remove",
        description="remove one or more aliases from a container recipe",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    for command in add, remove:
        command.add_argument("--registry", help="Path to registry root.", default=here)
        command.add_argument("container", help="Container alias to edit")
        command.add_argument("alias", help="alias name")
        command.add_argument("path", help="alias path", nargs="?")
        command.add_argument(
            "--force",
            help="force adding an alias that already exists.",
            default=False,
            action="store_true",
        )
    return parser


def main():
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("  container: %s" % args.container)
    print("   registry: %s" % args.registry)
    print("      alias:")
    print("       name: %s" % args.alias)
    print("       path: %s" % args.path)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    match = cli.registry.find(args.container)
    if not match:
        sys.exit(
            f"Cannot find {args.container} module. Are you sure it exists in this registry?"
        )

    if args.command == "add":
        return add_alias(match, args.alias, args.path, force=args.force)
    return remove_alias(match, args.alias)


def remove_alias(module, alias):
    """
    Remove an alias
    """
    if "aliases" not in module._config:
        sys.exit(f"Container {module.name} has no aliases.")

    if alias not in module._config["aliases"]:
        sys.exit(f"Alias {alias} does not exist in {module.name}.")

    del module._config["aliases"][alias]

    # Clean up empty directive
    if not module._config["aliases"]:
        del module._config["aliases"]

    module.save(module.package_file)


def add_alias(module, alias, path, force=False):
    """
    Add an alias
    """
    if not path:
        sys.exit("A path is required to add an alias.")

    if "aliases" not in module._config:
        module._config["aliases"] = {}

    if alias in module._config["aliases"] and not force:
        path = module._config["aliases"][alias]
        sys.exit(f"Alias {alias} already exists at {path} and --force is not set.")

    module._config["aliases"][alias] = path
    module.save(module.package_file)


if __name__ == "__main__":
    main()
