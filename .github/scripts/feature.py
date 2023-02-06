#!/usr/bin/env python3

import argparse
import os
import sys
from shpc.main import get_client

here = os.getcwd()


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Feature Updater",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        description="add a feature to a container recipe.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    remove = subparsers.add_parser(
        "remove",
        description="remove one or more features from a container recipe",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    for command in add, remove:
        command.add_argument("--registry", help="Path to registry root.", default=here)
        command.add_argument("container", help="Container alias to edit")
        command.add_argument("feature", help="feature name")
        command.add_argument(
            "value", help="feature value (e.g., true/false or path)", nargs="?"
        )
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
    print("    feature:")
    print("       name: %s" % args.feature)
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
        return add_feature(match, args.feature, args.value, force=args.force)
    return remove_feature(match, args.feature)


def remove_feature(module, feature):
    """
    Remove a feature
    """
    if "features" not in module._config:
        sys.exit(f"Container {module.name} has no features.")

    if feature not in module._config["features"]:
        sys.exit(f"Feature {feature} does not exist in {module.name}.")

    del module._config["features"][feature]

    # Clean up empty directive
    if not module._config["features"]:
        del module._config["features"]
    module.save(module.package_file)


def add_feature(module, feature, value, force=False):
    """
    Add a feature
    """
    if not value:
        sys.exit("A value is required to add a feature.")

    if "features" not in module._config:
        module._config["features"] = {}

    # Parse string boolean
    if value.lower() == "false":
        value = False
    elif value.lower() == "true":
        value = True
    elif value.lower() in ["none", "null"]:
        value = None

    if feature in module._config["features"] and not force:
        value = module._config["features"][feature]
        sys.exit(f"Feature {feature} already exists as {value} and --force is not set.")

    module._config["features"][feature] = value
    module.save(module.package_file)


if __name__ == "__main__":
    main()
