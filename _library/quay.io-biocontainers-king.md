---
layout: container
name:  "quay.io/biocontainers/king"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/king/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/king/container.yaml"
updated_at: "2025-02-07 03:18:04.675840"
latest: "2.2.7--h077b44d_3"
container_url: "https://biocontainers.pro/tools/king"
aliases:
 - "king"
versions:
 - "2.2.7--hd03093a_0"
 - "2.2.7--hdcf5f25_2"
 - "2.2.7--h077b44d_3"
description: "shpc-registry automated BioContainers addition for king"
config: {"url": "https://biocontainers.pro/tools/king", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for king", "latest": {"2.2.7--h077b44d_3": "sha256:89a18ca94bc8751931b0839e2831ed90b2940144c033bb664454d4c22840cdd1"}, "tags": {"2.2.7--hd03093a_0": "sha256:a858ae9560c407057952bc18e4b5bfd7401022dbe275f66836bbc0e9eec677fa", "2.2.7--hdcf5f25_2": "sha256:89bdcaa2f5f8a76989ef15bf297dd32496fb8ba91acd834428d50a36ff373090", "2.2.7--h077b44d_3": "sha256:89a18ca94bc8751931b0839e2831ed90b2940144c033bb664454d4c22840cdd1"}, "docker": "quay.io/biocontainers/king", "aliases": {"king": "/usr/local/bin/king"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/king.
shpc-registry automated BioContainers addition for king
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/king
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/king:2.2.7--h077b44d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/king/2.2.7--h077b44d_3
$ module help quay.io/biocontainers/king/2.2.7--h077b44d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### king-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### king-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### king-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### king-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### king-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### king-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### king

```bash
$ singularity exec <container> /usr/local/bin/king
$ podman run --it --rm --entrypoint /usr/local/bin/king   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/king   -v ${PWD} -w ${PWD} <container> -c " $@"
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