---
layout: container
name:  "quay.io/biocontainers/chromsize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromsize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chromsize/container.yaml"
updated_at: "2025-04-18 03:05:52.136956"
latest: "0.0.2--ha6fb395_1"
container_url: "https://biocontainers.pro/tools/chromsize"
aliases:
 - "chromsize"
 - "chromsize-benchmark"
versions:
 - "0.0.2--h919a2d8_0"
 - "0.0.2--ha6fb395_1"
description: "singularity registry hpc automated addition for chromsize"
config: {"url": "https://biocontainers.pro/tools/chromsize", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chromsize", "latest": {"0.0.2--ha6fb395_1": "sha256:d608f1195e25f47e116479fbf3aa41bcabab3e035e86d9a012cd7988f0369d35"}, "tags": {"0.0.2--h919a2d8_0": "sha256:b48f455bd374dd3f10932b58ddf4a3892b8c8b8ef4dea8e6d6b6aae6673aa79c", "0.0.2--ha6fb395_1": "sha256:d608f1195e25f47e116479fbf3aa41bcabab3e035e86d9a012cd7988f0369d35"}, "docker": "quay.io/biocontainers/chromsize", "aliases": {"chromsize": "/usr/local/bin/chromsize", "chromsize-benchmark": "/usr/local/bin/chromsize-benchmark"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromsize.
singularity registry hpc automated addition for chromsize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromsize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromsize:0.0.2--ha6fb395_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromsize/0.0.2--ha6fb395_1
$ module help quay.io/biocontainers/chromsize/0.0.2--ha6fb395_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromsize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromsize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromsize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromsize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromsize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromsize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chromsize

```bash
$ singularity exec <container> /usr/local/bin/chromsize
$ podman run --it --rm --entrypoint /usr/local/bin/chromsize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromsize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chromsize-benchmark

```bash
$ singularity exec <container> /usr/local/bin/chromsize-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/chromsize-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromsize-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
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