---
layout: container
name:  "quay.io/biocontainers/nanosimh"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanosimh/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanosimh/container.yaml"
updated_at: "2022-10-27 00:54:44.232560"
latest: "v1.0.1.8--py35r3.3.1_1"
container_url: "https://biocontainers.pro/tools/nanosimh"
aliases:
 - "nanosimh_simulate"
 - "nanosimh_train"
versions:
 - "v1.0.1.8--py35r3.3.1_1"
description: "shpc-registry automated BioContainers addition for nanosimh"
config: {"url": "https://biocontainers.pro/tools/nanosimh", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanosimh", "latest": {"v1.0.1.8--py35r3.3.1_1": "sha256:535870e69f8d18ca8062b3b960845ba077c41ffd6d831d739ea14ea0cc074449"}, "tags": {"v1.0.1.8--py35r3.3.1_1": "sha256:535870e69f8d18ca8062b3b960845ba077c41ffd6d831d739ea14ea0cc074449"}, "docker": "quay.io/biocontainers/nanosimh", "aliases": {"nanosimh_simulate": "/usr/local/bin/nanosimh_simulate", "nanosimh_train": "/usr/local/bin/nanosimh_train"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanosimh.
shpc-registry automated BioContainers addition for nanosimh
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanosimh
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanosimh:v1.0.1.8--py35r3.3.1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanosimh/v1.0.1.8--py35r3.3.1_1
$ module help quay.io/biocontainers/nanosimh/v1.0.1.8--py35r3.3.1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanosimh-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanosimh-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanosimh-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanosimh-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanosimh-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanosimh-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nanosimh_simulate

```bash
$ singularity exec <container> /usr/local/bin/nanosimh_simulate
$ podman run --it --rm --entrypoint /usr/local/bin/nanosimh_simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosimh_simulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanosimh_train

```bash
$ singularity exec <container> /usr/local/bin/nanosimh_train
$ podman run --it --rm --entrypoint /usr/local/bin/nanosimh_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosimh_train   -v ${PWD} -w ${PWD} <container> -c " $@"
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