---
layout: container
name:  "quay.io/biocontainers/gclib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gclib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gclib/container.yaml"
updated_at: "2024-03-12 02:56:45.796406"
latest: "0.0.1--h2d50403_5"
container_url: "https://biocontainers.pro/tools/gclib"
aliases:
 - "gtest"
 - "threads"
versions:
 - "0.0.1--h2d50403_5"
description: "shpc-registry automated BioContainers addition for gclib"
config: {"url": "https://biocontainers.pro/tools/gclib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gclib", "latest": {"0.0.1--h2d50403_5": "sha256:f8b3637096e3c680545ed7d38b2a8bd6d155cbc4a957608567c0c27ffcae2332"}, "tags": {"0.0.1--h2d50403_5": "sha256:f8b3637096e3c680545ed7d38b2a8bd6d155cbc4a957608567c0c27ffcae2332"}, "docker": "quay.io/biocontainers/gclib", "aliases": {"gtest": "/usr/local/bin/gtest", "threads": "/usr/local/bin/threads"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gclib.
shpc-registry automated BioContainers addition for gclib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gclib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gclib:0.0.1--h2d50403_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gclib/0.0.1--h2d50403_5
$ module help quay.io/biocontainers/gclib/0.0.1--h2d50403_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gclib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gclib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gclib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gclib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gclib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gclib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gtest

```bash
$ singularity exec <container> /usr/local/bin/gtest
$ podman run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### threads

```bash
$ singularity exec <container> /usr/local/bin/threads
$ podman run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
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