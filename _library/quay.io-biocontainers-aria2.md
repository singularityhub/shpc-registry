---
layout: container
name:  "quay.io/biocontainers/aria2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aria2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aria2/container.yaml"
updated_at: "2023-09-15 02:30:06.672656"
latest: "1.36.0"
container_url: "https://biocontainers.pro/tools/aria2"
aliases:
 - "aria2c"
versions:
 - "1.36.0"
description: "shpc-registry automated BioContainers addition for aria2"
config: {"url": "https://biocontainers.pro/tools/aria2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aria2", "latest": {"1.36.0": "sha256:acb0c86334ea0b2ba9454cc1b4d08f30c5a6ec7852159fd28fe34698154798d6"}, "tags": {"1.36.0": "sha256:acb0c86334ea0b2ba9454cc1b4d08f30c5a6ec7852159fd28fe34698154798d6"}, "docker": "quay.io/biocontainers/aria2", "aliases": {"aria2c": "/usr/local/bin/aria2c"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aria2.
shpc-registry automated BioContainers addition for aria2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aria2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aria2:1.36.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aria2/1.36.0
$ module help quay.io/biocontainers/aria2/1.36.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aria2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aria2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aria2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aria2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aria2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aria2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
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