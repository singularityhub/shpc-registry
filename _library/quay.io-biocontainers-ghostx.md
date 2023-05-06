---
layout: container
name:  "quay.io/biocontainers/ghostx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghostx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ghostx/container.yaml"
updated_at: "2023-05-06 03:28:02.960478"
latest: "1.3.7--hfc679d8_1"
container_url: "https://biocontainers.pro/tools/ghostx"
aliases:
 - "ghostx"
versions:
 - "1.3.7--hfc679d8_1"
description: "shpc-registry automated BioContainers addition for ghostx"
config: {"url": "https://biocontainers.pro/tools/ghostx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghostx", "latest": {"1.3.7--hfc679d8_1": "sha256:b5f25d1ed3bc4bde68f6070a670ebca359853226c7fd89e81741d2c2fb7d335d"}, "tags": {"1.3.7--hfc679d8_1": "sha256:b5f25d1ed3bc4bde68f6070a670ebca359853226c7fd89e81741d2c2fb7d335d"}, "docker": "quay.io/biocontainers/ghostx", "aliases": {"ghostx": "/usr/local/bin/ghostx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghostx.
shpc-registry automated BioContainers addition for ghostx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghostx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghostx:1.3.7--hfc679d8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghostx/1.3.7--hfc679d8_1
$ module help quay.io/biocontainers/ghostx/1.3.7--hfc679d8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghostx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghostx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghostx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghostx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghostx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghostx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ghostx

```bash
$ singularity exec <container> /usr/local/bin/ghostx
$ podman run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
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