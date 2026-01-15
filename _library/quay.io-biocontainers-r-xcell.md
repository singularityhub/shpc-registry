---
layout: container
name:  "quay.io/biocontainers/r-xcell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-xcell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-xcell/container.yaml"
updated_at: "2026-01-15 04:31:22.380415"
latest: "1.3--r44h9948957_8"
container_url: "https://biocontainers.pro/tools/r-xcell"

versions:
 - "1.3--r41h9f5acd7_3"
 - "1.3--r42h9f5acd7_4"
 - "1.3--r42h4ac6f70_5"
 - "1.3--r43h4ac6f70_6"
 - "1.3--r44h9948957_7"
 - "1.3--r44h9948957_8"
description: "shpc-registry automated BioContainers addition for r-xcell"
config: {"url": "https://biocontainers.pro/tools/r-xcell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-xcell", "latest": {"1.3--r44h9948957_8": "sha256:6ecb73c6c3bb0b18fc00a01f9d97c02e646fee6d708214dd7269f4ac46fff2f8"}, "tags": {"1.3--r41h9f5acd7_3": "sha256:d4df34367e86884b0ee998b360033c19e9efc430906af30729a6da3a3e00d919", "1.3--r42h9f5acd7_4": "sha256:66a22120276d2f0e5917eb77b453397c3c49f7e8f324826238d20cb8be74a63f", "1.3--r42h4ac6f70_5": "sha256:17631e543e4ca6341463ed84bbe28c1509327e5ec3d4c77e4d0224adb5c34ff5", "1.3--r43h4ac6f70_6": "sha256:6a4fc9221a6d95aa9e0778d3ae790df493558176c8cb807374bcaa8d4515ccf6", "1.3--r44h9948957_7": "sha256:4b003ffe72455bbdceb1e35b649d3e1590e5996a8979e2c49df5ccfd1e81d19c", "1.3--r44h9948957_8": "sha256:6ecb73c6c3bb0b18fc00a01f9d97c02e646fee6d708214dd7269f4ac46fff2f8"}, "docker": "quay.io/biocontainers/r-xcell"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-xcell.
shpc-registry automated BioContainers addition for r-xcell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-xcell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-xcell:1.3--r44h9948957_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-xcell/1.3--r44h9948957_8
$ module help quay.io/biocontainers/r-xcell/1.3--r44h9948957_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-xcell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-xcell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-xcell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-xcell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-xcell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-xcell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-xcell

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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