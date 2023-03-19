---
layout: container
name:  "quay.io/biocontainers/mantis_pfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mantis_pfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mantis_pfa/container.yaml"
updated_at: "2023-03-19 13:27:23.172805"
latest: "1.5.5--py310h1425a21_1"
container_url: "https://biocontainers.pro/tools/mantis_pfa"
aliases:
 - "mantis"
 - "nltk"
 - "diamond"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
 - "esl-alimerge"
 - "esl-alipid"
 - "esl-alirev"
 - "esl-alistat"
 - "esl-compalign"
 - "esl-compstruct"
 - "esl-construct"
 - "esl-histplot"
 - "esl-mask"
 - "esl-selectn"
 - "esl-seqrange"
 - "esl-seqstat"
 - "esl-sfetch"
 - "esl-shuffle"
 - "esl-ssdraw"
versions:
 - "1.5.5--py310h1425a21_1"
description: "singularity registry hpc automated addition for mantis_pfa"
config: {"url": "https://biocontainers.pro/tools/mantis_pfa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mantis_pfa", "latest": {"1.5.5--py310h1425a21_1": "sha256:cbb3560bb7075f82c29ca720d2dcb02bf97e48ece2885903ae6133b298fb96c3"}, "tags": {"1.5.5--py310h1425a21_1": "sha256:cbb3560bb7075f82c29ca720d2dcb02bf97e48ece2885903ae6133b298fb96c3"}, "docker": "quay.io/biocontainers/mantis_pfa", "aliases": {"mantis": "/usr/local/bin/mantis", "nltk": "/usr/local/bin/nltk", "diamond": "/usr/local/bin/diamond", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat", "esl-sfetch": "/usr/local/bin/esl-sfetch", "esl-shuffle": "/usr/local/bin/esl-shuffle", "esl-ssdraw": "/usr/local/bin/esl-ssdraw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mantis_pfa.
singularity registry hpc automated addition for mantis_pfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mantis_pfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mantis_pfa:1.5.5--py310h1425a21_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mantis_pfa/1.5.5--py310h1425a21_1
$ module help quay.io/biocontainers/mantis_pfa/1.5.5--py310h1425a21_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mantis_pfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mantis_pfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mantis_pfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mantis_pfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mantis_pfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mantis_pfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mantis

```bash
$ singularity exec <container> /usr/local/bin/mantis
$ podman run --it --rm --entrypoint /usr/local/bin/mantis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mantis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nltk

```bash
$ singularity exec <container> /usr/local/bin/nltk
$ podman run --it --rm --entrypoint /usr/local/bin/nltk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nltk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimerge

```bash
$ singularity exec <container> /usr/local/bin/esl-alimerge
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alipid

```bash
$ singularity exec <container> /usr/local/bin/esl-alipid
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alirev

```bash
$ singularity exec <container> /usr/local/bin/esl-alirev
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alistat

```bash
$ singularity exec <container> /usr/local/bin/esl-alistat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compalign

```bash
$ singularity exec <container> /usr/local/bin/esl-compalign
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compstruct

```bash
$ singularity exec <container> /usr/local/bin/esl-compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-construct

```bash
$ singularity exec <container> /usr/local/bin/esl-construct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-histplot

```bash
$ singularity exec <container> /usr/local/bin/esl-histplot
$ podman run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mask

```bash
$ singularity exec <container> /usr/local/bin/esl-mask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-selectn

```bash
$ singularity exec <container> /usr/local/bin/esl-selectn
$ podman run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqrange

```bash
$ singularity exec <container> /usr/local/bin/esl-seqrange
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqstat

```bash
$ singularity exec <container> /usr/local/bin/esl-seqstat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-sfetch

```bash
$ singularity exec <container> /usr/local/bin/esl-sfetch
$ podman run --it --rm --entrypoint /usr/local/bin/esl-sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-shuffle

```bash
$ singularity exec <container> /usr/local/bin/esl-shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/esl-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-ssdraw

```bash
$ singularity exec <container> /usr/local/bin/esl-ssdraw
$ podman run --it --rm --entrypoint /usr/local/bin/esl-ssdraw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-ssdraw   -v ${PWD} -w ${PWD} <container> -c " $@"
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