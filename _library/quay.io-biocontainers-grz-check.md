---
layout: container
name:  "quay.io/biocontainers/grz-check"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-check/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-check/container.yaml"
updated_at: "2025-09-01 04:16:17.168749"
latest: "0.1.0--h3ec5717_0"
container_url: "https://biocontainers.pro/tools/grz-check"
aliases:
 - "grz-check"
versions:
 - "0.1.0--h3ec5717_0"
description: "singularity registry hpc automated addition for grz-check"
config: {"url": "https://biocontainers.pro/tools/grz-check", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-check", "latest": {"0.1.0--h3ec5717_0": "sha256:4d4aef0ed678bd15499ed720e0b5c43bc31d316d116ca19ff073b805d684a55b"}, "tags": {"0.1.0--h3ec5717_0": "sha256:4d4aef0ed678bd15499ed720e0b5c43bc31d316d116ca19ff073b805d684a55b"}, "docker": "quay.io/biocontainers/grz-check", "aliases": {"grz-check": "/usr/local/bin/grz-check"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-check.
singularity registry hpc automated addition for grz-check
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-check
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-check:0.1.0--h3ec5717_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-check/0.1.0--h3ec5717_0
$ module help quay.io/biocontainers/grz-check/0.1.0--h3ec5717_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-check-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-check-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-check-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-check-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-check-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-check-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grz-check

```bash
$ singularity exec <container> /usr/local/bin/grz-check
$ podman run --it --rm --entrypoint /usr/local/bin/grz-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grz-check   -v ${PWD} -w ${PWD} <container> -c " $@"
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