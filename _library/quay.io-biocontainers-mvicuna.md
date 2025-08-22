---
layout: container
name:  "quay.io/biocontainers/mvicuna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mvicuna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mvicuna/container.yaml"
updated_at: "2025-08-22 03:18:31.684796"
latest: "1.0--h9948957_11"
container_url: "https://biocontainers.pro/tools/mvicuna"
aliases:
 - "mvicuna"
versions:
 - "1.0--h9f5acd7_8"
 - "1.0--h4ac6f70_10"
 - "1.0--h9948957_11"
description: "shpc-registry automated BioContainers addition for mvicuna"
config: {"url": "https://biocontainers.pro/tools/mvicuna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mvicuna", "latest": {"1.0--h9948957_11": "sha256:29ba72cc4ea217de6c86cbb8a28763be7b05920f99467d7f63dc079cbdb925ff"}, "tags": {"1.0--h9f5acd7_8": "sha256:9ffed2da86568ec0049e4e4c5ed84a631251192aa3c849951fdfaa399e7dc744", "1.0--h4ac6f70_10": "sha256:e00345c62ab115e0cef4180370aca07acc8b18acacc1386b8022df650786449b", "1.0--h9948957_11": "sha256:29ba72cc4ea217de6c86cbb8a28763be7b05920f99467d7f63dc079cbdb925ff"}, "docker": "quay.io/biocontainers/mvicuna", "aliases": {"mvicuna": "/usr/local/bin/mvicuna"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mvicuna.
shpc-registry automated BioContainers addition for mvicuna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mvicuna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mvicuna:1.0--h9948957_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mvicuna/1.0--h9948957_11
$ module help quay.io/biocontainers/mvicuna/1.0--h9948957_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mvicuna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mvicuna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mvicuna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mvicuna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mvicuna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mvicuna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mvicuna

```bash
$ singularity exec <container> /usr/local/bin/mvicuna
$ podman run --it --rm --entrypoint /usr/local/bin/mvicuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mvicuna   -v ${PWD} -w ${PWD} <container> -c " $@"
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