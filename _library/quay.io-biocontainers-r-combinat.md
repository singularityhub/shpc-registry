---
layout: container
name:  "quay.io/biocontainers/r-combinat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-combinat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-combinat/container.yaml"
updated_at: "2022-10-27 00:19:12.456378"
latest: "0.0_8--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-combinat"

versions:
 - "0.0_8--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-combinat"
config: {"url": "https://biocontainers.pro/tools/r-combinat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-combinat", "latest": {"0.0_8--r3.3.2_0": "sha256:e8cdadad3b9e8657a133e52639a244e5448a88fa21b905e9b955b6d892e5a305"}, "tags": {"0.0_8--r3.3.2_0": "sha256:e8cdadad3b9e8657a133e52639a244e5448a88fa21b905e9b955b6d892e5a305"}, "docker": "quay.io/biocontainers/r-combinat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-combinat.
shpc-registry automated BioContainers addition for r-combinat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-combinat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-combinat:0.0_8--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-combinat/0.0_8--r3.3.2_0
$ module help quay.io/biocontainers/r-combinat/0.0_8--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-combinat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-combinat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-combinat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-combinat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-combinat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-combinat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-combinat

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