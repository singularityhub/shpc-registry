---
layout: container
name:  "quay.io/biocontainers/kma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kma/container.yaml"
updated_at: "2024-07-01 04:10:29.105066"
latest: "1.4.14--he4a0461_1"
container_url: "https://biocontainers.pro/tools/kma"
aliases:
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
versions:
 - "1.4.0--h7132678_0"
 - "1.4.14--he4a0461_1"
description: "shpc-registry automated BioContainers addition for kma"
config: {"url": "https://biocontainers.pro/tools/kma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kma", "latest": {"1.4.14--he4a0461_1": "sha256:af5d86d5d799dcbf208faf46f7dcf82861fdfe6e8f51584fef964421d90910ed"}, "tags": {"1.4.0--h7132678_0": "sha256:e92f97e163dd82fefa40e9c3794cb0ff6cd818c953d3cc78b739e3a51afcdfe1", "1.4.14--he4a0461_1": "sha256:af5d86d5d799dcbf208faf46f7dcf82861fdfe6e8f51584fef964421d90910ed"}, "docker": "quay.io/biocontainers/kma", "aliases": {"kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kma.
shpc-registry automated BioContainers addition for kma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kma:1.4.14--he4a0461_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kma/1.4.14--he4a0461_1
$ module help quay.io/biocontainers/kma/1.4.14--he4a0461_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
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