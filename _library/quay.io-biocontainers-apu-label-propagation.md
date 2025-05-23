---
layout: container
name:  "quay.io/biocontainers/apu-label-propagation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/apu-label-propagation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/apu-label-propagation/container.yaml"
updated_at: "2025-05-23 03:31:21.275436"
latest: "1.2--h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/apu-label-propagation"
aliases:
 - "apu-label-propagation"
versions:
 - "1.2--h031d066_2"
 - "1.2--h7b50bb2_3"
description: "singularity registry hpc automated addition for apu-label-propagation"
config: {"url": "https://biocontainers.pro/tools/apu-label-propagation", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for apu-label-propagation", "latest": {"1.2--h7b50bb2_3": "sha256:e00cdfb34bf148a8db52f6df482ead9104a2f47ab93e9a6853ab40955d0e8b5c"}, "tags": {"1.2--h031d066_2": "sha256:56ad53a43284dd1749dab6779d5712a37d2a17f716c1a7bd6a9cfaca6609c197", "1.2--h7b50bb2_3": "sha256:e00cdfb34bf148a8db52f6df482ead9104a2f47ab93e9a6853ab40955d0e8b5c"}, "docker": "quay.io/biocontainers/apu-label-propagation", "aliases": {"apu-label-propagation": "/usr/local/bin/apu-label-propagation"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/apu-label-propagation.
singularity registry hpc automated addition for apu-label-propagation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/apu-label-propagation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/apu-label-propagation:1.2--h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/apu-label-propagation/1.2--h7b50bb2_3
$ module help quay.io/biocontainers/apu-label-propagation/1.2--h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### apu-label-propagation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### apu-label-propagation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### apu-label-propagation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### apu-label-propagation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### apu-label-propagation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### apu-label-propagation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### apu-label-propagation

```bash
$ singularity exec <container> /usr/local/bin/apu-label-propagation
$ podman run --it --rm --entrypoint /usr/local/bin/apu-label-propagation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apu-label-propagation   -v ${PWD} -w ${PWD} <container> -c " $@"
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