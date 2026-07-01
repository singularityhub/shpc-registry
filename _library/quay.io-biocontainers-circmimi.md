---
layout: container
name:  "quay.io/biocontainers/circmimi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circmimi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/circmimi/container.yaml"
updated_at: "2026-07-01 07:28:10.389206"
latest: "0.18.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/circmimi"
aliases:
 - "RCS_filter.py"
 - "checkAA_reads.py"
 - "circmimi_tools"
 - "get_RCS.py"
 - "get_RCS_summary.py"
 - "get_flanking_seq.py"
 - "gfClient"
 - "miranda"
 - "mp_blat.py"
 - "pslPretty"
 - "pslReps"
 - "faToNib"
 - "nibFrag"
 - "pslSort"
 - "gfServer"
 - "blat"
 - "idna"
 - "twoBitToFa"
 - "twoBitInfo"
 - "faToTwoBit"
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
versions:
 - "0.18.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for circmimi"
config: {"url": "https://biocontainers.pro/tools/circmimi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for circmimi", "latest": {"0.18.5--pyhdfd78af_0": "sha256:a8c60fe68bf6cd261ea34804cb2da845f643286ea78e5103c6625c0a903042cb"}, "tags": {"0.18.5--pyhdfd78af_0": "sha256:a8c60fe68bf6cd261ea34804cb2da845f643286ea78e5103c6625c0a903042cb"}, "docker": "quay.io/biocontainers/circmimi", "aliases": {"RCS_filter.py": "/usr/local/bin/RCS_filter.py", "checkAA_reads.py": "/usr/local/bin/checkAA_reads.py", "circmimi_tools": "/usr/local/bin/circmimi_tools", "get_RCS.py": "/usr/local/bin/get_RCS.py", "get_RCS_summary.py": "/usr/local/bin/get_RCS_summary.py", "get_flanking_seq.py": "/usr/local/bin/get_flanking_seq.py", "gfClient": "/usr/local/bin/gfClient", "miranda": "/usr/local/bin/miranda", "mp_blat.py": "/usr/local/bin/mp_blat.py", "pslPretty": "/usr/local/bin/pslPretty", "pslReps": "/usr/local/bin/pslReps", "faToNib": "/usr/local/bin/faToNib", "nibFrag": "/usr/local/bin/nibFrag", "pslSort": "/usr/local/bin/pslSort", "gfServer": "/usr/local/bin/gfServer", "blat": "/usr/local/bin/blat", "idna": "/usr/local/bin/idna", "twoBitToFa": "/usr/local/bin/twoBitToFa", "twoBitInfo": "/usr/local/bin/twoBitInfo", "faToTwoBit": "/usr/local/bin/faToTwoBit", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/circmimi.
singularity registry hpc automated addition for circmimi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circmimi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circmimi:0.18.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circmimi/0.18.5--pyhdfd78af_0
$ module help quay.io/biocontainers/circmimi/0.18.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circmimi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circmimi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circmimi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circmimi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circmimi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circmimi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RCS_filter.py

```bash
$ singularity exec <container> /usr/local/bin/RCS_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/RCS_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RCS_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkAA_reads.py

```bash
$ singularity exec <container> /usr/local/bin/checkAA_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/checkAA_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkAA_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circmimi_tools

```bash
$ singularity exec <container> /usr/local/bin/circmimi_tools
$ podman run --it --rm --entrypoint /usr/local/bin/circmimi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circmimi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_RCS.py

```bash
$ singularity exec <container> /usr/local/bin/get_RCS.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_RCS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_RCS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_RCS_summary.py

```bash
$ singularity exec <container> /usr/local/bin/get_RCS_summary.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_RCS_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_RCS_summary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_flanking_seq.py

```bash
$ singularity exec <container> /usr/local/bin/get_flanking_seq.py
$ podman run --it --rm --entrypoint /usr/local/bin/get_flanking_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_flanking_seq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfClient

```bash
$ singularity exec <container> /usr/local/bin/gfClient
$ podman run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfClient   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miranda

```bash
$ singularity exec <container> /usr/local/bin/miranda
$ podman run --it --rm --entrypoint /usr/local/bin/miranda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miranda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mp_blat.py

```bash
$ singularity exec <container> /usr/local/bin/mp_blat.py
$ podman run --it --rm --entrypoint /usr/local/bin/mp_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mp_blat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslPretty

```bash
$ singularity exec <container> /usr/local/bin/pslPretty
$ podman run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslPretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslReps

```bash
$ singularity exec <container> /usr/local/bin/pslReps
$ podman run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslReps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToNib

```bash
$ singularity exec <container> /usr/local/bin/faToNib
$ podman run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToNib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nibFrag

```bash
$ singularity exec <container> /usr/local/bin/nibFrag
$ podman run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nibFrag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pslSort

```bash
$ singularity exec <container> /usr/local/bin/pslSort
$ podman run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslSort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blat

```bash
$ singularity exec <container> /usr/local/bin/blat
$ podman run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitInfo

```bash
$ singularity exec <container> /usr/local/bin/twoBitInfo
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
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