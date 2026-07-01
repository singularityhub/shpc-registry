---
layout: container
name:  "quay.io/biocontainers/eplacer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eplacer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eplacer/container.yaml"
updated_at: "2026-07-01 15:18:25.458577"
latest: "0.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/eplacer"
aliases:
 - "eplacer"
 - "nad"
 - "ncbi-acc-download"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "gawk-5.4.0"
 - "readal"
 - "statal"
 - "trimal"
 - "idna"
 - "torchfrtrace"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "sort-by-length"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
 - "xlink"
 - "xlink.ini"
 - "xsearch"
versions:
 - "0.1.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for eplacer"
config: {"url": "https://biocontainers.pro/tools/eplacer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for eplacer", "latest": {"0.1.5--pyhdfd78af_0": "sha256:47433d823fab287da42eed7e4cbc2f032021bc2fa6e394150e7155ea024de0cc"}, "tags": {"0.1.5--pyhdfd78af_0": "sha256:47433d823fab287da42eed7e4cbc2f032021bc2fa6e394150e7155ea024de0cc"}, "docker": "quay.io/biocontainers/eplacer", "aliases": {"eplacer": "/usr/local/bin/eplacer", "nad": "/usr/local/bin/nad", "ncbi-acc-download": "/usr/local/bin/ncbi-acc-download", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "idna": "/usr/local/bin/idna", "torchfrtrace": "/usr/local/bin/torchfrtrace", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eplacer.
singularity registry hpc automated addition for eplacer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eplacer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eplacer:0.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eplacer/0.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/eplacer/0.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eplacer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eplacer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eplacer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eplacer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eplacer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eplacer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eplacer

```bash
$ singularity exec <container> /usr/local/bin/eplacer
$ podman run --it --rm --entrypoint /usr/local/bin/eplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nad

```bash
$ singularity exec <container> /usr/local/bin/nad
$ podman run --it --rm --entrypoint /usr/local/bin/nad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-acc-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-acc-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-acc-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-acc-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-by-length

```bash
$ singularity exec <container> /usr/local/bin/sort-by-length
$ podman run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/xcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch

```bash
$ singularity exec <container> /usr/local/bin/xfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch.ini

```bash
$ singularity exec <container> /usr/local/bin/xfetch.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfilter

```bash
$ singularity exec <container> /usr/local/bin/xfilter
$ podman run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xinfo

```bash
$ singularity exec <container> /usr/local/bin/xinfo
$ podman run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink

```bash
$ singularity exec <container> /usr/local/bin/xlink
$ podman run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink.ini

```bash
$ singularity exec <container> /usr/local/bin/xlink.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsearch

```bash
$ singularity exec <container> /usr/local/bin/xsearch
$ podman run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)