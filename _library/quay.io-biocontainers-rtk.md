---
layout: container
name:  "quay.io/biocontainers/rtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rtk/container.yaml"
updated_at: "2025-04-13 04:09:43.327607"
latest: "0.93.2--h077b44d_5"
container_url: "https://biocontainers.pro/tools/rtk"
aliases:
 - "rtk"
versions:
 - "0.93.2--hd03093a_2"
 - "0.93.2--hdcf5f25_4"
 - "0.93.2--h077b44d_5"
description: "shpc-registry automated BioContainers addition for rtk"
config: {"url": "https://biocontainers.pro/tools/rtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rtk", "latest": {"0.93.2--h077b44d_5": "sha256:297053059ea582e1297ff7545ad1bd7a3e8fbb38ec09bea7d8cefa98c55abf1c"}, "tags": {"0.93.2--hd03093a_2": "sha256:d597102d8d468ab21ec4c46b8bc40b5d4fbaa9c1ecf3f390989da60214515b0b", "0.93.2--hdcf5f25_4": "sha256:a33adc45a383d9cf2aa44eb469e360e630702db184b271af6b4b24be3c67394f", "0.93.2--h077b44d_5": "sha256:297053059ea582e1297ff7545ad1bd7a3e8fbb38ec09bea7d8cefa98c55abf1c"}, "docker": "quay.io/biocontainers/rtk", "aliases": {"rtk": "/usr/local/bin/rtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rtk.
shpc-registry automated BioContainers addition for rtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rtk:0.93.2--h077b44d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rtk/0.93.2--h077b44d_5
$ module help quay.io/biocontainers/rtk/0.93.2--h077b44d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rtk

```bash
$ singularity exec <container> /usr/local/bin/rtk
$ podman run --it --rm --entrypoint /usr/local/bin/rtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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