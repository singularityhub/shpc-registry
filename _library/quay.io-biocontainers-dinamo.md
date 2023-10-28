---
layout: container
name:  "quay.io/biocontainers/dinamo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dinamo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dinamo/container.yaml"
updated_at: "2023-10-28 02:23:28.167887"
latest: "1.0--h376f1d3_4"
container_url: "https://biocontainers.pro/tools/dinamo"
aliases:
 - "dinamo"
versions:
 - "1.0--h2df963e_2"
 - "1.0--h376f1d3_4"
description: "shpc-registry automated BioContainers addition for dinamo"
config: {"url": "https://biocontainers.pro/tools/dinamo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dinamo", "latest": {"1.0--h376f1d3_4": "sha256:64227a611f7a3bc8fc4571cbcd5428d4e6ed4694c7f409c4fb04b46ac9acecde"}, "tags": {"1.0--h2df963e_2": "sha256:ab8ac75d97e570584c3ab7f30c6f1c9eb2675a3253dc7326bd39bc3aa48cccf3", "1.0--h376f1d3_4": "sha256:64227a611f7a3bc8fc4571cbcd5428d4e6ed4694c7f409c4fb04b46ac9acecde"}, "docker": "quay.io/biocontainers/dinamo", "aliases": {"dinamo": "/usr/local/bin/dinamo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dinamo.
shpc-registry automated BioContainers addition for dinamo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dinamo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dinamo:1.0--h376f1d3_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dinamo/1.0--h376f1d3_4
$ module help quay.io/biocontainers/dinamo/1.0--h376f1d3_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dinamo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dinamo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dinamo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dinamo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dinamo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dinamo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dinamo

```bash
$ singularity exec <container> /usr/local/bin/dinamo
$ podman run --it --rm --entrypoint /usr/local/bin/dinamo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dinamo   -v ${PWD} -w ${PWD} <container> -c " $@"
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