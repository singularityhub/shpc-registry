---
layout: container
name:  "quay.io/biocontainers/rtk2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rtk2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rtk2/container.yaml"
updated_at: "2026-01-01 07:13:16.794788"
latest: "2.11.2--h077b44d_1"
container_url: "https://biocontainers.pro/tools/rtk2"
aliases:
 - "rtk2"
versions:
 - "2.10--hdcf5f25_0"
 - "2.11.2--hdcf5f25_0"
 - "2.11.2--h077b44d_1"
description: "singularity registry hpc automated addition for rtk2"
config: {"url": "https://biocontainers.pro/tools/rtk2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rtk2", "latest": {"2.11.2--h077b44d_1": "sha256:9dc69f43e47d2535a5590f05d0a3a21cb0bf486846add48c04d64f0bb28087a5"}, "tags": {"2.10--hdcf5f25_0": "sha256:4f9ac7d7405bc53f0b5f65911ceccd2f2c35b0e513d81f44afc1ab532a8db260", "2.11.2--hdcf5f25_0": "sha256:0ce524a705af598d751ad38dd43a3654f0b9e4ab7c724db0dd10eaeb92ce9b80", "2.11.2--h077b44d_1": "sha256:9dc69f43e47d2535a5590f05d0a3a21cb0bf486846add48c04d64f0bb28087a5"}, "docker": "quay.io/biocontainers/rtk2", "aliases": {"rtk2": "/usr/local/bin/rtk2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rtk2.
singularity registry hpc automated addition for rtk2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rtk2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rtk2:2.11.2--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rtk2/2.11.2--h077b44d_1
$ module help quay.io/biocontainers/rtk2/2.11.2--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rtk2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rtk2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rtk2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rtk2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rtk2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rtk2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rtk2

```bash
$ singularity exec <container> /usr/local/bin/rtk2
$ podman run --it --rm --entrypoint /usr/local/bin/rtk2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rtk2   -v ${PWD} -w ${PWD} <container> -c " $@"
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