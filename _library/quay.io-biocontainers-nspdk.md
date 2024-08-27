---
layout: container
name:  "quay.io/biocontainers/nspdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nspdk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nspdk/container.yaml"
updated_at: "2024-08-27 06:56:33.730062"
latest: "9.2--1"
container_url: "https://biocontainers.pro/tools/nspdk"
aliases:
 - "NSPDK"
versions:
 - "9.2--1"
description: "shpc-registry automated BioContainers addition for nspdk"
config: {"url": "https://biocontainers.pro/tools/nspdk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nspdk", "latest": {"9.2--1": "sha256:48ab7446323f5d84913a0b2e1ca28f13b984429e5f99ea013be1613a97797bc2"}, "tags": {"9.2--1": "sha256:48ab7446323f5d84913a0b2e1ca28f13b984429e5f99ea013be1613a97797bc2"}, "docker": "quay.io/biocontainers/nspdk", "aliases": {"NSPDK": "/usr/local/bin/NSPDK"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nspdk.
shpc-registry automated BioContainers addition for nspdk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nspdk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nspdk:9.2--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nspdk/9.2--1
$ module help quay.io/biocontainers/nspdk/9.2--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nspdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nspdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nspdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nspdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nspdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nspdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NSPDK

```bash
$ singularity exec <container> /usr/local/bin/NSPDK
$ podman run --it --rm --entrypoint /usr/local/bin/NSPDK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NSPDK   -v ${PWD} -w ${PWD} <container> -c " $@"
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