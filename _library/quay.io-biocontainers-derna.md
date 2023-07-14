---
layout: container
name:  "quay.io/biocontainers/derna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/derna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/derna/container.yaml"
updated_at: "2023-07-14 03:35:19.741127"
latest: "1.0.2--hdbdd923_1"
container_url: "https://biocontainers.pro/tools/derna"
aliases:
 - "derna"
versions:
 - "1.0.2--hdbdd923_1"
description: "singularity registry hpc automated addition for derna"
config: {"url": "https://biocontainers.pro/tools/derna", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for derna", "latest": {"1.0.2--hdbdd923_1": "sha256:45fb3f1d003076e2a4b67387d787ae2d539c67d0b2e3e5d7f3d94d3d76d1570e"}, "tags": {"1.0.2--hdbdd923_1": "sha256:45fb3f1d003076e2a4b67387d787ae2d539c67d0b2e3e5d7f3d94d3d76d1570e"}, "docker": "quay.io/biocontainers/derna", "aliases": {"derna": "/usr/local/bin/derna"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/derna.
singularity registry hpc automated addition for derna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/derna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/derna:1.0.2--hdbdd923_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/derna/1.0.2--hdbdd923_1
$ module help quay.io/biocontainers/derna/1.0.2--hdbdd923_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### derna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### derna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### derna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### derna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### derna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### derna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### derna

```bash
$ singularity exec <container> /usr/local/bin/derna
$ podman run --it --rm --entrypoint /usr/local/bin/derna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/derna   -v ${PWD} -w ${PWD} <container> -c " $@"
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