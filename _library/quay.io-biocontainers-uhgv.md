---
layout: container
name:  "quay.io/biocontainers/uhgv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uhgv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uhgv/container.yaml"
updated_at: "2026-07-01 15:26:53.624097"
latest: "2.0.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/uhgv"
aliases:
 - "pyrodigal-gv"
 - "uhgv"
 - "pyrodigal"
 - "archspec"
 - "rich-click"
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
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
versions:
 - "2.0.0--pyh106432d_0"
description: "singularity registry hpc automated addition for uhgv"
config: {"url": "https://biocontainers.pro/tools/uhgv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for uhgv", "latest": {"2.0.0--pyh106432d_0": "sha256:9a745999d9271cd8b86202246d1ed4cd67635ac64d223fa1bc9502ac97fee932"}, "tags": {"2.0.0--pyh106432d_0": "sha256:9a745999d9271cd8b86202246d1ed4cd67635ac64d223fa1bc9502ac97fee932"}, "docker": "quay.io/biocontainers/uhgv", "aliases": {"pyrodigal-gv": "/usr/local/bin/pyrodigal-gv", "uhgv": "/usr/local/bin/uhgv", "pyrodigal": "/usr/local/bin/pyrodigal", "archspec": "/usr/local/bin/archspec", "rich-click": "/usr/local/bin/rich-click", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uhgv.
singularity registry hpc automated addition for uhgv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uhgv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uhgv:2.0.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uhgv/2.0.0--pyh106432d_0
$ module help quay.io/biocontainers/uhgv/2.0.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uhgv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uhgv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uhgv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uhgv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uhgv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uhgv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyrodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uhgv

```bash
$ singularity exec <container> /usr/local/bin/uhgv
$ podman run --it --rm --entrypoint /usr/local/bin/uhgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uhgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bsmp2info

```bash
$ singularity exec <container> /usr/local/bin/bsmp2info
$ podman run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsa2xml

```bash
$ singularity exec <container> /usr/local/bin/fsa2xml
$ podman run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2info

```bash
$ singularity exec <container> /usr/local/bin/gbf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
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