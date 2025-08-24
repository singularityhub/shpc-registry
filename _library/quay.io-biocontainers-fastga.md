---
layout: container
name:  "quay.io/biocontainers/fastga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastga/container.yaml"
updated_at: "2025-08-24 03:54:10.608039"
latest: "1.3--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/fastga"
aliases:
 - "ALNchain"
 - "ALNplot"
 - "ALNreset"
 - "ALNshow"
 - "ALNtoPAF"
 - "ALNtoPSL"
 - "FAtoGDB"
 - "FastGA"
 - "GDBshow"
 - "GDBstat"
 - "GDBtoFA"
 - "GIXcp"
 - "GIXmake"
 - "GIXmv"
 - "GIXrm"
 - "GIXshow"
 - "ONEview"
 - "PAFtoALN"
 - "PAFtoPSL"
versions:
 - "1.2--h577a1d6_0"
 - "1.3--h577a1d6_0"
description: "singularity registry hpc automated addition for fastga"
config: {"url": "https://biocontainers.pro/tools/fastga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastga", "latest": {"1.3--h577a1d6_0": "sha256:c247b19349772a19761f3685775ecd1d62735efc695fb33a5f30766b39e5f1a7"}, "tags": {"1.2--h577a1d6_0": "sha256:9eef8900d79e2f94505fe54e888152adc5289f7fdbe5862b6e19879e19628fd0", "1.3--h577a1d6_0": "sha256:c247b19349772a19761f3685775ecd1d62735efc695fb33a5f30766b39e5f1a7"}, "docker": "quay.io/biocontainers/fastga", "aliases": {"ALNchain": "/usr/local/bin/ALNchain", "ALNplot": "/usr/local/bin/ALNplot", "ALNreset": "/usr/local/bin/ALNreset", "ALNshow": "/usr/local/bin/ALNshow", "ALNtoPAF": "/usr/local/bin/ALNtoPAF", "ALNtoPSL": "/usr/local/bin/ALNtoPSL", "FAtoGDB": "/usr/local/bin/FAtoGDB", "FastGA": "/usr/local/bin/FastGA", "GDBshow": "/usr/local/bin/GDBshow", "GDBstat": "/usr/local/bin/GDBstat", "GDBtoFA": "/usr/local/bin/GDBtoFA", "GIXcp": "/usr/local/bin/GIXcp", "GIXmake": "/usr/local/bin/GIXmake", "GIXmv": "/usr/local/bin/GIXmv", "GIXrm": "/usr/local/bin/GIXrm", "GIXshow": "/usr/local/bin/GIXshow", "ONEview": "/usr/local/bin/ONEview", "PAFtoALN": "/usr/local/bin/PAFtoALN", "PAFtoPSL": "/usr/local/bin/PAFtoPSL"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastga.
singularity registry hpc automated addition for fastga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastga:1.3--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastga/1.3--h577a1d6_0
$ module help quay.io/biocontainers/fastga/1.3--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ALNchain

```bash
$ singularity exec <container> /usr/local/bin/ALNchain
$ podman run --it --rm --entrypoint /usr/local/bin/ALNchain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNchain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALNplot

```bash
$ singularity exec <container> /usr/local/bin/ALNplot
$ podman run --it --rm --entrypoint /usr/local/bin/ALNplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALNreset

```bash
$ singularity exec <container> /usr/local/bin/ALNreset
$ podman run --it --rm --entrypoint /usr/local/bin/ALNreset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNreset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALNshow

```bash
$ singularity exec <container> /usr/local/bin/ALNshow
$ podman run --it --rm --entrypoint /usr/local/bin/ALNshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALNtoPAF

```bash
$ singularity exec <container> /usr/local/bin/ALNtoPAF
$ podman run --it --rm --entrypoint /usr/local/bin/ALNtoPAF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNtoPAF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ALNtoPSL

```bash
$ singularity exec <container> /usr/local/bin/ALNtoPSL
$ podman run --it --rm --entrypoint /usr/local/bin/ALNtoPSL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ALNtoPSL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FAtoGDB

```bash
$ singularity exec <container> /usr/local/bin/FAtoGDB
$ podman run --it --rm --entrypoint /usr/local/bin/FAtoGDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FAtoGDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastGA

```bash
$ singularity exec <container> /usr/local/bin/FastGA
$ podman run --it --rm --entrypoint /usr/local/bin/FastGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GDBshow

```bash
$ singularity exec <container> /usr/local/bin/GDBshow
$ podman run --it --rm --entrypoint /usr/local/bin/GDBshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GDBshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GDBstat

```bash
$ singularity exec <container> /usr/local/bin/GDBstat
$ podman run --it --rm --entrypoint /usr/local/bin/GDBstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GDBstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GDBtoFA

```bash
$ singularity exec <container> /usr/local/bin/GDBtoFA
$ podman run --it --rm --entrypoint /usr/local/bin/GDBtoFA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GDBtoFA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GIXcp

```bash
$ singularity exec <container> /usr/local/bin/GIXcp
$ podman run --it --rm --entrypoint /usr/local/bin/GIXcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GIXcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GIXmake

```bash
$ singularity exec <container> /usr/local/bin/GIXmake
$ podman run --it --rm --entrypoint /usr/local/bin/GIXmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GIXmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GIXmv

```bash
$ singularity exec <container> /usr/local/bin/GIXmv
$ podman run --it --rm --entrypoint /usr/local/bin/GIXmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GIXmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GIXrm

```bash
$ singularity exec <container> /usr/local/bin/GIXrm
$ podman run --it --rm --entrypoint /usr/local/bin/GIXrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GIXrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GIXshow

```bash
$ singularity exec <container> /usr/local/bin/GIXshow
$ podman run --it --rm --entrypoint /usr/local/bin/GIXshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GIXshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ONEview

```bash
$ singularity exec <container> /usr/local/bin/ONEview
$ podman run --it --rm --entrypoint /usr/local/bin/ONEview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ONEview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PAFtoALN

```bash
$ singularity exec <container> /usr/local/bin/PAFtoALN
$ podman run --it --rm --entrypoint /usr/local/bin/PAFtoALN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PAFtoALN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PAFtoPSL

```bash
$ singularity exec <container> /usr/local/bin/PAFtoPSL
$ podman run --it --rm --entrypoint /usr/local/bin/PAFtoPSL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PAFtoPSL   -v ${PWD} -w ${PWD} <container> -c " $@"
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