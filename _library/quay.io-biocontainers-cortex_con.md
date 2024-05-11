---
layout: container
name:  "quay.io/biocontainers/cortex_con"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cortex_con/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cortex_con/container.yaml"
updated_at: "2024-05-11 02:53:17.927760"
latest: "0.04c--h470a237_1"
container_url: "https://biocontainers.pro/tools/cortex_con"
aliases:
 - "cortex_con_31"
versions:
 - "0.04c--h470a237_1"
description: "shpc-registry automated BioContainers addition for cortex_con"
config: {"url": "https://biocontainers.pro/tools/cortex_con", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cortex_con", "latest": {"0.04c--h470a237_1": "sha256:238e0342749feffebbce811a69fc555000d52d8a0a32dfe2da9b9dec24517d65"}, "tags": {"0.04c--h470a237_1": "sha256:238e0342749feffebbce811a69fc555000d52d8a0a32dfe2da9b9dec24517d65"}, "docker": "quay.io/biocontainers/cortex_con", "aliases": {"cortex_con_31": "/usr/local/bin/cortex_con_31"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cortex_con.
shpc-registry automated BioContainers addition for cortex_con
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cortex_con
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cortex_con:0.04c--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cortex_con/0.04c--h470a237_1
$ module help quay.io/biocontainers/cortex_con/0.04c--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cortex_con-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cortex_con-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cortex_con-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cortex_con-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cortex_con-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cortex_con-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cortex_con_31

```bash
$ singularity exec <container> /usr/local/bin/cortex_con_31
$ podman run --it --rm --entrypoint /usr/local/bin/cortex_con_31   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cortex_con_31   -v ${PWD} -w ${PWD} <container> -c " $@"
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