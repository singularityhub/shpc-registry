---
layout: container
name:  "quay.io/biocontainers/snakeobjects"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakeobjects/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snakeobjects/container.yaml"
updated_at: "2022-10-27 00:23:51.207402"
latest: "3.1.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/snakeobjects"
aliases:
 - "sobjects"
versions:
 - "3.1.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for snakeobjects"
config: {"url": "https://biocontainers.pro/tools/snakeobjects", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakeobjects", "latest": {"3.1.1--pyh5e36f6f_0": "sha256:1d92811a3779c5c9c7ed9046b2b9a88f8a5694e481c1ac896efe0ec4f1021b04"}, "tags": {"3.1.1--pyh5e36f6f_0": "sha256:1d92811a3779c5c9c7ed9046b2b9a88f8a5694e481c1ac896efe0ec4f1021b04"}, "docker": "quay.io/biocontainers/snakeobjects", "aliases": {"sobjects": "/usr/local/bin/sobjects"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakeobjects.
shpc-registry automated BioContainers addition for snakeobjects
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakeobjects
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakeobjects:3.1.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakeobjects/3.1.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/snakeobjects/3.1.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakeobjects-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakeobjects-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakeobjects-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakeobjects-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakeobjects-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakeobjects-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sobjects

```bash
$ singularity exec <container> /usr/local/bin/sobjects
$ podman run --it --rm --entrypoint /usr/local/bin/sobjects   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sobjects   -v ${PWD} -w ${PWD} <container> -c " $@"
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