#!/usr/bin/env python3

import argparse
import os
from shpc.main import get_client
from container_guts.main import ManifestGenerator
import shpc.utils
import requests
import re
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
    return parser


# A pipeline to process docker tags
steps = (
    # Scrub commits from version string
    step.filters.CleanCommit(),
    # Parse versions, return sorted ascending, and taking version major.minor.patch into account
    step.container.ContainerTagSort(),
)
p = pipeline.Pipeline(steps)


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

    uris = {}

    # Use the latest for each unique
    for link in links:
        if ":" not in link.text:
            continue
        image, tag = link.text.split(":", 1)

        # If we already have the registry folder, skip
        container_dir = os.path.join(args.registry, "quay.io", "biocontainers", image)
        if image in uris or os.path.exists(container_dir):
            continue

        print(f"Retrieving tags for {image}")
        tags = requests.get(f"https://crane.ggcr.dev/ls/quay.io/biocontainers/{image}")
        uris[image] = [x for x in tags.text.split("\n") if x]

    # For each uri, get latest version
    for uri, tags in uris.items():

        container_dir = os.path.join(args.registry, "quay.io", "biocontainers", uri)
        if "UNAUTHORIZED" in tags[0] or os.path.exists(container_dir):
            continue

        # The updated and transformed items
        ordered = p.run(list(tags), unwrap=False)
        tag = ordered[0]._original
        container = f"quay.io/biocontainers/{uri}:{tag}"
        add_container(cli, container, args.maintainer, uri)


# A bit manual, but a list of aliases to skip!
skips = [
    "[",
    "b2sum",
    "base32",
    "base64",
    "basename",
    "basenc",
    "cairo-trace",
    "cat",
    "chcon",
    "chgrp",
    "chmod",
    "chown",
    "chroot",
    "cjpeg",
    "cksum",
    "comm",
    "cp",
    "csplit",
    "cut",
    "date",
    "dd",
    "derb",
    "df",
    "dir",
    "dircolors",
    "dirname",
    "djpeg",
    "du",
    "echo",
    "env",
    "envsubst",
    "expand",
    "expr",
    "factor",
    "false",
    "fax2ps",
    "fax2tiff",
    "fc-cache",
    "fc-cat",
    "fc-conflist",
    "fc-list",
    "fc-match",
    "fc-pattern",
    "fc-query",
    "fc-scan",
    "fc-validate",
    "fmt",
    "fold",
    "freetype-config",
    "genbrk",
    "gencfu",
    "gencnval",
    "gendict",
    "genrb",
    "gettext",
    "gettext.sh",
    "gettextize",
    "gif2rgb",
    "gifbuild",
    "gifclrmp",
    "giffix",
    "giftext",
    "giftool",
    "groups",
    "head",
    "hostid",
    "id",
    "install",
    "jaotc",
    "jar",
    "jarsigner",
    "java",
    "javac",
    "javadoc",
    "javap",
    "jcmd",
    "jconsole",
    "jdb",
    "jdeprscan",
    "jdeps",
    "jfr",
    "jhsdb",
    "jimage",
    "jinfo",
    "jjs",
    "jlink",
    "jmap",
    "jmod",
    "join",
    "jpegtran",
    "jpgicc",
    "jps",
    "jrunscript",
    "jshell",
    "jstack",
    "jstat",
    "jstatd",
    "keytool",
    "kill",
    "libdeflate-gunzip",
    "libdeflate-gzip",
    "libpng-config",
    "libpng16-config",
    "link",
    "linkicc",
    "ln",
    "logname",
    "ls",
    "md5sum",
    "mkdir",
    "mkfifo",
    "mknod",
    "mktemp",
    "msgattrib",
    "msgcat",
    "msgcmp",
    "msgcomm",
    "msgconv",
    "msgen",
    "msgexec",
    "msgfilter",
    "msgfmt",
    "msggrep",
    "msginit",
    "msgmerge",
    "msgunfmt",
    "msguniq",
    "mv",
    "ngettext",
    "nice",
    "nl",
    "nohup",
    "nproc",
    "numfmt",
    "od",
    "pack200",
    "pal2rgb",
    "paste",
    "pathchk",
    "pcre-config",
    "pcregrep",
    "pcretest",
    "pinky",
    "png-fix-itxt",
    "pngfix",
    "ppm2tiff",
    "pr",
    "printenv",
    "printf",
    "psicc",
    "ptx",
    "pwd",
    "raw2tiff",
    "rdjpgcom",
    "readlink",
    "realpath",
    "recode-sr-latin",
    "rm",
    "rmdir",
    "rmic",
    "rmid",
    "rmiregistry",
    "runcon",
    "seq",
    "serialver",
    "sha1sum",
    "sha224sum",
    "sha256sum",
    "sha384sum",
    "sha512sum",
    "shred",
    "shuf",
    "sleep",
    "sort",
    "split",
    "stat",
    "stdbuf",
    "stty",
    "sum",
    "sync",
    "tac",
    "tail",
    "tee",
    "test",
    "tiff2bw",
    "tiff2pdf",
    "tiff2ps",
    "tiff2rgba",
    "tiffcmp",
    "tiffcp",
    "tiffcrop",
    "tiffdither",
    "tiffdump",
    "tiffinfo",
    "tiffmedian",
    "tiffset",
    "tiffsplit",
    "tificc",
    "timeout",
    "touch",
    "tr",
    "transicc",
    "true",
    "truncate",
    "tsort",
    "tty",
    "uname",
    "unexpand",
    "uniq",
    "unlink",
    "unlz4",
    "unpack200",
    "unzstd",
    "uptime",
    "users",
    "vdir",
    "wc",
    "webpinfo",
    "webpmux",
    "who",
    "whoami",
    "wrjpgcom",
    "xgettext",
    "yes",
    "zstd",
    "zstdcat",
    "zstdgrep",
    "zstdless",
    "zstdmt",
]


def include_path(path, basename):
    return (
        "sbin" not in path
        and "/usr/bin" not in path
        and not basename.startswith("xz")
        and not re.search(
            "^(xml|xz|lz|env-|ic|hwloc|unlzma|unxz|pkgdata|makeconv)", basename
        )
        and not path.startswith("/bin") and basename not in skips
    )


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
