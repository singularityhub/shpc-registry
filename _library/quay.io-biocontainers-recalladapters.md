---
layout: container
name:  "quay.io/biocontainers/recalladapters"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recalladapters/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recalladapters/container.yaml"
updated_at: "2024-12-10 03:33:39.136967"
latest: "9.0.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/recalladapters"
aliases:
 - "recalladapters"
versions:
 - "9.0.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for recalladapters"
config: {"url": "https://biocontainers.pro/tools/recalladapters", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for recalladapters", "latest": {"9.0.0--h9ee0642_1": "sha256:6122fa4a531ff40bdb47bd58a8f20e20fcda3e077cceb1b60d3a4bccf6ae7232"}, "tags": {"9.0.0--h9ee0642_1": "sha256:6122fa4a531ff40bdb47bd58a8f20e20fcda3e077cceb1b60d3a4bccf6ae7232"}, "docker": "quay.io/biocontainers/recalladapters", "aliases": {"recalladapters": "/usr/local/bin/recalladapters"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recalladapters.
shpc-registry automated BioContainers addition for recalladapters
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recalladapters
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recalladapters:9.0.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recalladapters/9.0.0--h9ee0642_1
$ module help quay.io/biocontainers/recalladapters/9.0.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recalladapters-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recalladapters-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recalladapters-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recalladapters-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recalladapters-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recalladapters-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recalladapters

```bash
$ singularity exec <container> /usr/local/bin/recalladapters
$ podman run --it --rm --entrypoint /usr/local/bin/recalladapters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recalladapters   -v ${PWD} -w ${PWD} <container> -c " $@"
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