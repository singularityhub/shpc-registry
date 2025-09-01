---
layout: container
name:  "quay.io/biocontainers/canopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/canopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/canopy/container.yaml"
updated_at: "2025-09-01 03:43:17.780379"
latest: "0.25--h077b44d_1"
container_url: "https://biocontainers.pro/tools/canopy"
aliases:
 - "cc.bin"
versions:
 - "0.25--hdcf5f25_0"
 - "0.25--h077b44d_1"
description: "singularity registry hpc automated addition for canopy"
config: {"url": "https://biocontainers.pro/tools/canopy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for canopy", "latest": {"0.25--h077b44d_1": "sha256:86b64b3e6a1660675d909408a33a9e2238ddd81925d9585ec3c5841077578c9b"}, "tags": {"0.25--hdcf5f25_0": "sha256:c74b5ead63b0803dcbe1349b2ae3a51270426c40dab3428e58003047df5ec60f", "0.25--h077b44d_1": "sha256:86b64b3e6a1660675d909408a33a9e2238ddd81925d9585ec3c5841077578c9b"}, "docker": "quay.io/biocontainers/canopy", "aliases": {"cc.bin": "/usr/local/bin/cc.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/canopy.
singularity registry hpc automated addition for canopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/canopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/canopy:0.25--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/canopy/0.25--h077b44d_1
$ module help quay.io/biocontainers/canopy/0.25--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### canopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### canopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### canopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### canopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### canopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### canopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cc.bin

```bash
$ singularity exec <container> /usr/local/bin/cc.bin
$ podman run --it --rm --entrypoint /usr/local/bin/cc.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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