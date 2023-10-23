---
layout: container
name:  "quay.io/biocontainers/bumbershoot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bumbershoot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bumbershoot/container.yaml"
updated_at: "2023-10-23 03:01:09.776556"
latest: "3_0_21142_0e4f4a4--h7d875b9_0"
container_url: "https://biocontainers.pro/tools/bumbershoot"
aliases:
 - "adjustScanRankerScoreByGroup"
 - "directag"
 - "idpAssemble"
 - "idpQonvert"
 - "idpQuery"
 - "myrimatch"
 - "pepitome"
 - "quameter"
 - "tagrecon"
versions:
 - "3_0_21142_0e4f4a4--h7d875b9_0"
description: "shpc-registry automated BioContainers addition for bumbershoot"
config: {"url": "https://biocontainers.pro/tools/bumbershoot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bumbershoot", "latest": {"3_0_21142_0e4f4a4--h7d875b9_0": "sha256:06ddd345f823d00f2ea26d3fe6a65588df7263040aa2d7380e8d8c49a7b3428e"}, "tags": {"3_0_21142_0e4f4a4--h7d875b9_0": "sha256:06ddd345f823d00f2ea26d3fe6a65588df7263040aa2d7380e8d8c49a7b3428e"}, "docker": "quay.io/biocontainers/bumbershoot", "aliases": {"adjustScanRankerScoreByGroup": "/usr/local/bin/adjustScanRankerScoreByGroup", "directag": "/usr/local/bin/directag", "idpAssemble": "/usr/local/bin/idpAssemble", "idpQonvert": "/usr/local/bin/idpQonvert", "idpQuery": "/usr/local/bin/idpQuery", "myrimatch": "/usr/local/bin/myrimatch", "pepitome": "/usr/local/bin/pepitome", "quameter": "/usr/local/bin/quameter", "tagrecon": "/usr/local/bin/tagrecon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bumbershoot.
shpc-registry automated BioContainers addition for bumbershoot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bumbershoot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bumbershoot:3_0_21142_0e4f4a4--h7d875b9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bumbershoot/3_0_21142_0e4f4a4--h7d875b9_0
$ module help quay.io/biocontainers/bumbershoot/3_0_21142_0e4f4a4--h7d875b9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bumbershoot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bumbershoot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bumbershoot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bumbershoot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bumbershoot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bumbershoot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adjustScanRankerScoreByGroup

```bash
$ singularity exec <container> /usr/local/bin/adjustScanRankerScoreByGroup
$ podman run --it --rm --entrypoint /usr/local/bin/adjustScanRankerScoreByGroup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjustScanRankerScoreByGroup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### directag

```bash
$ singularity exec <container> /usr/local/bin/directag
$ podman run --it --rm --entrypoint /usr/local/bin/directag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/directag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idpAssemble

```bash
$ singularity exec <container> /usr/local/bin/idpAssemble
$ podman run --it --rm --entrypoint /usr/local/bin/idpAssemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idpAssemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idpQonvert

```bash
$ singularity exec <container> /usr/local/bin/idpQonvert
$ podman run --it --rm --entrypoint /usr/local/bin/idpQonvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idpQonvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idpQuery

```bash
$ singularity exec <container> /usr/local/bin/idpQuery
$ podman run --it --rm --entrypoint /usr/local/bin/idpQuery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idpQuery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myrimatch

```bash
$ singularity exec <container> /usr/local/bin/myrimatch
$ podman run --it --rm --entrypoint /usr/local/bin/myrimatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myrimatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pepitome

```bash
$ singularity exec <container> /usr/local/bin/pepitome
$ podman run --it --rm --entrypoint /usr/local/bin/pepitome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pepitome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quameter

```bash
$ singularity exec <container> /usr/local/bin/quameter
$ podman run --it --rm --entrypoint /usr/local/bin/quameter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quameter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tagrecon

```bash
$ singularity exec <container> /usr/local/bin/tagrecon
$ podman run --it --rm --entrypoint /usr/local/bin/tagrecon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tagrecon   -v ${PWD} -w ${PWD} <container> -c " $@"
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