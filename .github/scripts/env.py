#!/usr/bin/env python3

import argparse
import os
import sys
from shpc.main import get_client

here = os.getcwd()


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Environment Updater",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        description="add an environment variable to a container recipe.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    remove = subparsers.add_parser(
        "remove",
        description="remove one or more environment variables from a container recipe",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    for command in add, remove:
        command.add_argument("--registry", help="Path to registry root.", default=here)
        command.add_argument("container", help="Container alias to edit")
        command.add_argument("name", help="environment variable name")
        command.add_argument("value", help="environment variable value", nargs="?")
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
    print("      envar:")
    print("       name: %s" % args.name)
    print("      value: %s" % args.value)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    match = cli.registry.find(args.container)
    if not match:
        sys.exit(
            f"Cannot find {args.container} module. Are you sure it exists in this registry?"
        )

    if args.command == "add":
        return add_envar(match, args.name, args.value, force=args.force)
    return remove_envar(match, args.name)


def remove_envar(module, name):
    """
    Remove an environment variable
    """
    if "env" not in module._config:
        sys.exit(f"Container {module.name} has no environment variables.")

    if name not in module._config["env"]:
        sys.exit(f"Environment variable {name} does not exist in {module.name}.")

    del module._config["env"][name]

    # Clean up empty directive
    if not module._config["env"]:
        del module._config["env"]
    module.save(module.package_file)


def add_envar(module, name, value, force=False):
    """
    Add an environment variable
    """
    if "env" not in module._config:
        module._config["env"] = {}

    # Parse string boolean
    if value == None:
        value = ""
    elif value.lower() == "false":
        value = False
    elif value.lower() == "true":
        value = True
    elif value.lower() in ["none", "null"]:
        value = ""

    if name in module._config["env"] and not force:
        value = module._config["env"][name]
        sys.exit(
            f"Environment variable {name} already exists as {value} and --force is not set."
        )

    module._config["env"][name] = value
    module.save(module.package_file)


if __name__ == "__main__":
    main()
