---
layout: container
name:  "quay.io/biocontainers/bioconductor-mvgst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mvgst/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mvgst/container.yaml"
updated_at: "2022-10-27 00:48:47.462999"
latest: "1.12.0--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mvgst"
aliases:
 - "GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz"
versions:
 - "1.12.0--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mvgst"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mvgst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mvgst", "latest": {"1.12.0--r3.4.1_0": "sha256:edcd5f6a9bcaeb45b84ff1a84c4e861efce30d383f5de05f429516b92c0f1e57"}, "tags": {"1.12.0--r3.4.1_0": "sha256:edcd5f6a9bcaeb45b84ff1a84c4e861efce30d383f5de05f429516b92c0f1e57"}, "docker": "quay.io/biocontainers/bioconductor-mvgst", "aliases": {"GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mvgst.
shpc-registry automated BioContainers addition for bioconductor-mvgst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mvgst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mvgst:1.12.0--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mvgst/1.12.0--r3.4.1_0
$ module help quay.io/biocontainers/bioconductor-mvgst/1.12.0--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mvgst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvgst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvgst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mvgst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mvgst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mvgst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
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