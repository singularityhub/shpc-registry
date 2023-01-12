---
layout: container
name:  "quay.io/biocontainers/libmuscle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libmuscle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libmuscle/container.yaml"
updated_at: "2023-01-12 03:04:22.239604"
latest: "3.7--h470a237_1"
container_url: "https://biocontainers.pro/tools/libmuscle"

versions:
 - "3.7--h470a237_1"
description: "shpc-registry automated BioContainers addition for libmuscle"
config: {"url": "https://biocontainers.pro/tools/libmuscle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libmuscle", "latest": {"3.7--h470a237_1": "sha256:bf9fc0fcc57d6c315e3b7c81b639243b3e29a4c5f87e7eb35c846fa6d7a7b0c4"}, "tags": {"3.7--h470a237_1": "sha256:bf9fc0fcc57d6c315e3b7c81b639243b3e29a4c5f87e7eb35c846fa6d7a7b0c4"}, "docker": "quay.io/biocontainers/libmuscle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libmuscle.
shpc-registry automated BioContainers addition for libmuscle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libmuscle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libmuscle:3.7--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libmuscle/3.7--h470a237_1
$ module help quay.io/biocontainers/libmuscle/3.7--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libmuscle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libmuscle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libmuscle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libmuscle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libmuscle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libmuscle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libmuscle

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