---
layout: container
name:  "quay.io/biocontainers/padloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/padloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/padloc/container.yaml"
updated_at: "2026-01-16 04:02:13.820984"
latest: "2.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/padloc"
aliases:
 - "padloc"
 - "padloc.R"
 - "egrep"
 - "fgrep"
 - "grep"
 - "pandoc-lua"
 - "pandoc-server"
 - "x86_64-conda-linux-gnu.cfg"
 - "prodigal"
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
versions:
 - "2.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for padloc"
config: {"url": "https://biocontainers.pro/tools/padloc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for padloc", "latest": {"2.0.0--hdfd78af_0": "sha256:21fdf46bb90ca125621d66d8c6fdbc6ac664c14f6c4d5c1e7cfd61f1100ebb68"}, "tags": {"2.0.0--hdfd78af_0": "sha256:21fdf46bb90ca125621d66d8c6fdbc6ac664c14f6c4d5c1e7cfd61f1100ebb68"}, "docker": "quay.io/biocontainers/padloc", "aliases": {"padloc": "/usr/local/bin/padloc", "padloc.R": "/usr/local/bin/padloc.R", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "pandoc-lua": "/usr/local/bin/pandoc-lua", "pandoc-server": "/usr/local/bin/pandoc-server", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/padloc.
singularity registry hpc automated addition for padloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/padloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/padloc:2.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/padloc/2.0.0--hdfd78af_0
$ module help quay.io/biocontainers/padloc/2.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### padloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### padloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### padloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### padloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### padloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### padloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### padloc

```bash
$ singularity exec <container> /usr/local/bin/padloc
$ podman run --it --rm --entrypoint /usr/local/bin/padloc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/padloc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### padloc.R

```bash
$ singularity exec <container> /usr/local/bin/padloc.R
$ podman run --it --rm --entrypoint /usr/local/bin/padloc.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/padloc.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
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