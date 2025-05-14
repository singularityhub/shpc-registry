---
layout: container
name:  "quay.io/biocontainers/rotate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rotate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rotate/container.yaml"
updated_at: "2025-05-14 03:21:07.258206"
latest: "1.0--he4a0461_0"
container_url: "https://biocontainers.pro/tools/rotate"
aliases:
 - "composition"
 - "rotate"
versions:
 - "1.0--he4a0461_0"
description: "singularity registry hpc automated addition for rotate"
config: {"url": "https://biocontainers.pro/tools/rotate", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rotate", "latest": {"1.0--he4a0461_0": "sha256:40754380b67cddb23e20342f5bc1428249c2e94f80bf1ffe83960f442f6290e0"}, "tags": {"1.0--he4a0461_0": "sha256:40754380b67cddb23e20342f5bc1428249c2e94f80bf1ffe83960f442f6290e0"}, "docker": "quay.io/biocontainers/rotate", "aliases": {"composition": "/usr/local/bin/composition", "rotate": "/usr/local/bin/rotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rotate.
singularity registry hpc automated addition for rotate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rotate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rotate:1.0--he4a0461_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rotate/1.0--he4a0461_0
$ module help quay.io/biocontainers/rotate/1.0--he4a0461_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rotate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rotate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rotate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rotate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rotate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rotate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### composition

```bash
$ singularity exec <container> /usr/local/bin/composition
$ podman run --it --rm --entrypoint /usr/local/bin/composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rotate

```bash
$ singularity exec <container> /usr/local/bin/rotate
$ podman run --it --rm --entrypoint /usr/local/bin/rotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rotate   -v ${PWD} -w ${PWD} <container> -c " $@"
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