---
layout: container
name:  "quay.io/biocontainers/mummer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mummer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mummer/container.yaml"
updated_at: "2024-03-20 02:50:43.570723"
latest: "3.23--pl5321hdbdd923_16"
container_url: "https://biocontainers.pro/tools/mummer"
aliases:
 - "mummer"
versions:
 - "3.23--pl5321h87f3376_14"
 - "3.23--pl5321hdbdd923_16"
description: "shpc-registry automated BioContainers addition for mummer"
config: {"url": "https://biocontainers.pro/tools/mummer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mummer", "latest": {"3.23--pl5321hdbdd923_16": "sha256:6cc30f4cd6e23263532cd62400b12e4a740b1386d76ac4d6a39a40dcd54211b6"}, "tags": {"3.23--pl5321h87f3376_14": "sha256:7e8794c0f90afcca59db2b8d4be8c769b463ef7f3dc6d3f70970eae5c36ccf3f", "3.23--pl5321hdbdd923_16": "sha256:6cc30f4cd6e23263532cd62400b12e4a740b1386d76ac4d6a39a40dcd54211b6"}, "docker": "quay.io/biocontainers/mummer", "aliases": {"mummer": "/usr/local/bin/mummer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mummer.
shpc-registry automated BioContainers addition for mummer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mummer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mummer:3.23--pl5321hdbdd923_16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mummer/3.23--pl5321hdbdd923_16
$ module help quay.io/biocontainers/mummer/3.23--pl5321hdbdd923_16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mummer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mummer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mummer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mummer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mummer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mummer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
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