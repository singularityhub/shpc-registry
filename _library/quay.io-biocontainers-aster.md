---
layout: container
name:  "quay.io/biocontainers/aster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aster/container.yaml"
updated_at: "2023-03-10 03:38:02.330232"
latest: "1.3--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/aster"
aliases:
 - "asterisk"
 - "astral"
 - "astral-pro"
versions:
 - "1.3--h9f5acd7_1"
description: "singularity registry hpc automated addition for aster"
config: {"url": "https://biocontainers.pro/tools/aster", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aster", "latest": {"1.3--h9f5acd7_1": "sha256:7662b11a19008b7a13b77ae116f2d20231d3ca19b47fabf4977b90b438fd4d9f"}, "tags": {"1.3--h9f5acd7_1": "sha256:7662b11a19008b7a13b77ae116f2d20231d3ca19b47fabf4977b90b438fd4d9f"}, "docker": "quay.io/biocontainers/aster", "aliases": {"asterisk": "/usr/local/bin/asterisk", "astral": "/usr/local/bin/astral", "astral-pro": "/usr/local/bin/astral-pro"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aster.
singularity registry hpc automated addition for aster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aster:1.3--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aster/1.3--h9f5acd7_1
$ module help quay.io/biocontainers/aster/1.3--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asterisk

```bash
$ singularity exec <container> /usr/local/bin/asterisk
$ podman run --it --rm --entrypoint /usr/local/bin/asterisk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asterisk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### astral

```bash
$ singularity exec <container> /usr/local/bin/astral
$ podman run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### astral-pro

```bash
$ singularity exec <container> /usr/local/bin/astral-pro
$ podman run --it --rm --entrypoint /usr/local/bin/astral-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/astral-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
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