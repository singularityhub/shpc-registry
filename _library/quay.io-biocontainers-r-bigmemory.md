---
layout: container
name:  "quay.io/biocontainers/r-bigmemory"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bigmemory/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bigmemory/container.yaml"
updated_at: "2025-04-06 03:48:08.296474"
latest: "4.5.19--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-bigmemory"

versions:
 - "4.5.19--r3.2.2_0"
 - "4.5.19--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-bigmemory"
config: {"url": "https://biocontainers.pro/tools/r-bigmemory", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bigmemory", "latest": {"4.5.19--r3.2.2_0": "sha256:5433a95fc7d3ded05e28c0d08630aeb251c60f317e528794082be60fb7ae8358"}, "tags": {"4.5.19--r3.2.2_0": "sha256:5433a95fc7d3ded05e28c0d08630aeb251c60f317e528794082be60fb7ae8358", "4.5.19--r3.3.2_0": "sha256:80d177c09cf18da0072454de22d0c4c734f93d061df4c16801a976035c3063fd"}, "docker": "quay.io/biocontainers/r-bigmemory"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bigmemory.
shpc-registry automated BioContainers addition for r-bigmemory
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bigmemory
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bigmemory:4.5.19--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bigmemory/4.5.19--r3.2.2_0
$ module help quay.io/biocontainers/r-bigmemory/4.5.19--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bigmemory-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bigmemory-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bigmemory-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bigmemory-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bigmemory-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bigmemory-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-bigmemory

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