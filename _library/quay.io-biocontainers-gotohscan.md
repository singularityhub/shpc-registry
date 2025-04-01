---
layout: container
name:  "quay.io/biocontainers/gotohscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gotohscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gotohscan/container.yaml"
updated_at: "2025-04-01 03:55:34.037057"
latest: "1.3--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/gotohscan"
aliases:
 - "GotohScan"
versions:
 - "1.3--hec16e2b_4"
 - "1.3--h031d066_6"
 - "1.3--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for gotohscan"
config: {"url": "https://biocontainers.pro/tools/gotohscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gotohscan", "latest": {"1.3--h7b50bb2_7": "sha256:3a6e2850100990e3e87537234f8d2058a70c855144fd491e585e18d8bdda57fe"}, "tags": {"1.3--hec16e2b_4": "sha256:9e76a0a45ffd892c7934926846f25d08dba859f43588f87494de45cf2c581bae", "1.3--h031d066_6": "sha256:ef921b19725bb70b85cc2c6db69202c973da650f5bf89943974ca501cd99b9c4", "1.3--h7b50bb2_7": "sha256:3a6e2850100990e3e87537234f8d2058a70c855144fd491e585e18d8bdda57fe"}, "docker": "quay.io/biocontainers/gotohscan", "aliases": {"GotohScan": "/usr/local/bin/GotohScan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gotohscan.
shpc-registry automated BioContainers addition for gotohscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gotohscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gotohscan:1.3--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gotohscan/1.3--h7b50bb2_7
$ module help quay.io/biocontainers/gotohscan/1.3--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gotohscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gotohscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gotohscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gotohscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gotohscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gotohscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GotohScan

```bash
$ singularity exec <container> /usr/local/bin/GotohScan
$ podman run --it --rm --entrypoint /usr/local/bin/GotohScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GotohScan   -v ${PWD} -w ${PWD} <container> -c " $@"
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