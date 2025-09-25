---
layout: container
name:  "quay.io/biocontainers/libmuscle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libmuscle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libmuscle/container.yaml"
updated_at: "2025-09-25 07:26:50.418660"
latest: "3.7--h503566f_2"
container_url: "https://biocontainers.pro/tools/libmuscle"

versions:
 - "3.7--h470a237_1"
 - "3.7--h503566f_2"
description: "shpc-registry automated BioContainers addition for libmuscle"
config: {"url": "https://biocontainers.pro/tools/libmuscle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libmuscle", "latest": {"3.7--h503566f_2": "sha256:426ed4f825bb2b295b8caced6fa7a3fe7c967435701fc4debb607461d4ecf2e8"}, "tags": {"3.7--h470a237_1": "sha256:653702fb482a0b91674a1c787db9784f5601f20d1e4474358b68a12cf181ed09", "3.7--h503566f_2": "sha256:426ed4f825bb2b295b8caced6fa7a3fe7c967435701fc4debb607461d4ecf2e8"}, "docker": "quay.io/biocontainers/libmuscle"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libmuscle.
shpc-registry automated BioContainers addition for libmuscle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libmuscle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libmuscle:3.7--h503566f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libmuscle/3.7--h503566f_2
$ module help quay.io/biocontainers/libmuscle/3.7--h503566f_2
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