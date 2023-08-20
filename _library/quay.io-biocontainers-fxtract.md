---
layout: container
name:  "quay.io/biocontainers/fxtract"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fxtract/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fxtract/container.yaml"
updated_at: "2023-08-20 02:37:25.267910"
latest: "2.4--h1eb128b_2"
container_url: "https://biocontainers.pro/tools/fxtract"
aliases:
 - "fxtract"
versions:
 - "2.4--h131032e_0"
 - "2.4--h1eb128b_2"
description: "singularity registry hpc automated addition for fxtract"
config: {"url": "https://biocontainers.pro/tools/fxtract", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fxtract", "latest": {"2.4--h1eb128b_2": "sha256:e060c9ee68a84bb1f3d2111ad49ef4109bd928101787c20e2cf2d9ebccb3a219"}, "tags": {"2.4--h131032e_0": "sha256:be1ede43ada2648df04b125e130f5f05121853c7880393e4d4135f268f55dc68", "2.4--h1eb128b_2": "sha256:e060c9ee68a84bb1f3d2111ad49ef4109bd928101787c20e2cf2d9ebccb3a219"}, "docker": "quay.io/biocontainers/fxtract", "aliases": {"fxtract": "/usr/local/bin/fxtract"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fxtract.
singularity registry hpc automated addition for fxtract
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fxtract
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fxtract:2.4--h1eb128b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fxtract/2.4--h1eb128b_2
$ module help quay.io/biocontainers/fxtract/2.4--h1eb128b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fxtract-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fxtract-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fxtract-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fxtract-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fxtract-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fxtract-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fxtract

```bash
$ singularity exec <container> /usr/local/bin/fxtract
$ podman run --it --rm --entrypoint /usr/local/bin/fxtract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fxtract   -v ${PWD} -w ${PWD} <container> -c " $@"
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