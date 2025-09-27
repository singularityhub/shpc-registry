---
layout: container
name:  "quay.io/biocontainers/leviathan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/leviathan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/leviathan/container.yaml"
updated_at: "2025-09-27 03:05:38.979577"
latest: "1.0.2--h9948957_4"
container_url: "https://biocontainers.pro/tools/leviathan"
aliases:
 - "LEVIATHAN"
 - "LRez"
versions:
 - "1.0.2--h9f5acd7_2"
 - "1.0.2--h4ac6f70_3"
 - "1.0.2--h9948957_4"
description: "shpc-registry automated BioContainers addition for leviathan"
config: {"url": "https://biocontainers.pro/tools/leviathan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for leviathan", "latest": {"1.0.2--h9948957_4": "sha256:293db4f75cef2fbb2edab3257003ecef5bba604aec77a26b8bc7b9c0ab2462fe"}, "tags": {"1.0.2--h9f5acd7_2": "sha256:8202932299e05c944ad3033ef0131c0b2c17d54dc4316986c9363a324e1e680b", "1.0.2--h4ac6f70_3": "sha256:31196b84c9444a49f7f63489108ae38cde3e66ca09565a38e11e618789ad1c08", "1.0.2--h9948957_4": "sha256:293db4f75cef2fbb2edab3257003ecef5bba604aec77a26b8bc7b9c0ab2462fe"}, "docker": "quay.io/biocontainers/leviathan", "aliases": {"LEVIATHAN": "/usr/local/bin/LEVIATHAN", "LRez": "/usr/local/bin/LRez"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/leviathan.
shpc-registry automated BioContainers addition for leviathan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/leviathan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/leviathan:1.0.2--h9948957_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/leviathan/1.0.2--h9948957_4
$ module help quay.io/biocontainers/leviathan/1.0.2--h9948957_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### leviathan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### leviathan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### leviathan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### leviathan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### leviathan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### leviathan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LEVIATHAN

```bash
$ singularity exec <container> /usr/local/bin/LEVIATHAN
$ podman run --it --rm --entrypoint /usr/local/bin/LEVIATHAN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LEVIATHAN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LRez

```bash
$ singularity exec <container> /usr/local/bin/LRez
$ podman run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
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