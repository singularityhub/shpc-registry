---
layout: container
name:  "quay.io/biocontainers/gvcfgenotyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gvcfgenotyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gvcfgenotyper/container.yaml"
updated_at: "2025-03-09 02:42:16.114968"
latest: "2019.02.26--h13024bc_5"
container_url: "https://biocontainers.pro/tools/gvcfgenotyper"
aliases:
 - "gvcfgenotyper"
versions:
 - "2019.02.26--h468198e_2"
 - "2019.02.26--hf5e1c6e_4"
 - "2019.02.26--h13024bc_5"
description: "shpc-registry automated BioContainers addition for gvcfgenotyper"
config: {"url": "https://biocontainers.pro/tools/gvcfgenotyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gvcfgenotyper", "latest": {"2019.02.26--h13024bc_5": "sha256:c789d0a605654e2cbe3f82fe7c9b37e1ca5d0542ef2d2f9c25cc9656c45f8151"}, "tags": {"2019.02.26--h468198e_2": "sha256:bfaf411ececc4f25e50939ba22c9cf4a2d12f1e612356333903af1694268c8ae", "2019.02.26--hf5e1c6e_4": "sha256:9b06ad6a58211d2d6d8b1c0d2732baf6892c29cbb00339f8aad6b48320f9a7eb", "2019.02.26--h13024bc_5": "sha256:c789d0a605654e2cbe3f82fe7c9b37e1ca5d0542ef2d2f9c25cc9656c45f8151"}, "docker": "quay.io/biocontainers/gvcfgenotyper", "aliases": {"gvcfgenotyper": "/usr/local/bin/gvcfgenotyper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gvcfgenotyper.
shpc-registry automated BioContainers addition for gvcfgenotyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gvcfgenotyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gvcfgenotyper:2019.02.26--h13024bc_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gvcfgenotyper/2019.02.26--h13024bc_5
$ module help quay.io/biocontainers/gvcfgenotyper/2019.02.26--h13024bc_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gvcfgenotyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gvcfgenotyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gvcfgenotyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gvcfgenotyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gvcfgenotyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gvcfgenotyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gvcfgenotyper

```bash
$ singularity exec <container> /usr/local/bin/gvcfgenotyper
$ podman run --it --rm --entrypoint /usr/local/bin/gvcfgenotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvcfgenotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
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