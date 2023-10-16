---
layout: container
name:  "quay.io/biocontainers/crussmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crussmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crussmap/container.yaml"
updated_at: "2023-10-16 03:16:58.388917"
latest: "1.0.0--h86f6036_0"
container_url: "https://biocontainers.pro/tools/crussmap"
aliases:
 - "crussmap"
versions:
 - "1.0.0--h86f6036_0"
description: "singularity registry hpc automated addition for crussmap"
config: {"url": "https://biocontainers.pro/tools/crussmap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for crussmap", "latest": {"1.0.0--h86f6036_0": "sha256:58f5d8238be0f05125eeb118a0f21592ec2c1a502c2894b77c66d85f358a51c3"}, "tags": {"1.0.0--h86f6036_0": "sha256:58f5d8238be0f05125eeb118a0f21592ec2c1a502c2894b77c66d85f358a51c3"}, "docker": "quay.io/biocontainers/crussmap", "aliases": {"crussmap": "/usr/local/bin/crussmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crussmap.
singularity registry hpc automated addition for crussmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crussmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crussmap:1.0.0--h86f6036_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crussmap/1.0.0--h86f6036_0
$ module help quay.io/biocontainers/crussmap/1.0.0--h86f6036_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crussmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crussmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crussmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crussmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crussmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crussmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crussmap

```bash
$ singularity exec <container> /usr/local/bin/crussmap
$ podman run --it --rm --entrypoint /usr/local/bin/crussmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crussmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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