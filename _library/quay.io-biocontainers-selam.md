---
layout: container
name:  "quay.io/biocontainers/selam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/selam/container.yaml"
updated_at: "2025-02-04 02:48:23.163122"
latest: "0.9--h3053a90_4"
container_url: "https://biocontainers.pro/tools/selam"
aliases:
 - "SELAM"
 - "SELAM_STATS"
versions:
 - "0.9--h5e66344_0"
 - "0.9--h0432e7c_2"
 - "0.9--h0432e7c_3"
 - "0.9--h3053a90_4"
description: "singularity registry hpc automated addition for selam"
config: {"url": "https://biocontainers.pro/tools/selam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for selam", "latest": {"0.9--h3053a90_4": "sha256:c76b09a8e43d6ebc42a9b3e0480d4bbced868560e12cf8f39d3ce29cc6fa974a"}, "tags": {"0.9--h5e66344_0": "sha256:8198f72a7136a90900d0effd0aee9d7c4a2d5c24efec729ab4bf3ad9c6024927", "0.9--h0432e7c_2": "sha256:7ede757fed3993f42972fdd993ebdab601edce833bf6f15c88c2d500051d3aa4", "0.9--h0432e7c_3": "sha256:d7e442f862279ace7643866417a4827bbc0e95793bef1812b6a0d43a7e68bcf2", "0.9--h3053a90_4": "sha256:c76b09a8e43d6ebc42a9b3e0480d4bbced868560e12cf8f39d3ce29cc6fa974a"}, "docker": "quay.io/biocontainers/selam", "aliases": {"SELAM": "/usr/local/bin/SELAM", "SELAM_STATS": "/usr/local/bin/SELAM_STATS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selam.
singularity registry hpc automated addition for selam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selam:0.9--h3053a90_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selam/0.9--h3053a90_4
$ module help quay.io/biocontainers/selam/0.9--h3053a90_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SELAM

```bash
$ singularity exec <container> /usr/local/bin/SELAM
$ podman run --it --rm --entrypoint /usr/local/bin/SELAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SELAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SELAM_STATS

```bash
$ singularity exec <container> /usr/local/bin/SELAM_STATS
$ podman run --it --rm --entrypoint /usr/local/bin/SELAM_STATS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SELAM_STATS   -v ${PWD} -w ${PWD} <container> -c " $@"
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