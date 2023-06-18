---
layout: container
name:  "quay.io/biocontainers/colord"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/colord/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/colord/container.yaml"
updated_at: "2023-06-18 02:54:44.586103"
latest: "1.1.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/colord"
aliases:
 - "colord"
versions:
 - "1.1.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for colord"
config: {"url": "https://biocontainers.pro/tools/colord", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for colord", "latest": {"1.1.0--h9ee0642_1": "sha256:cde7f3de1298fa9c6f31bebffb889395a3560edf51b29f5f9c36bf7d52fcc48b"}, "tags": {"1.1.0--h9ee0642_1": "sha256:cde7f3de1298fa9c6f31bebffb889395a3560edf51b29f5f9c36bf7d52fcc48b"}, "docker": "quay.io/biocontainers/colord", "aliases": {"colord": "/usr/local/bin/colord"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/colord.
shpc-registry automated BioContainers addition for colord
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/colord
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/colord:1.1.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/colord/1.1.0--h9ee0642_1
$ module help quay.io/biocontainers/colord/1.1.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### colord-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### colord-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### colord-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### colord-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### colord-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### colord-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### colord

```bash
$ singularity exec <container> /usr/local/bin/colord
$ podman run --it --rm --entrypoint /usr/local/bin/colord   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colord   -v ${PWD} -w ${PWD} <container> -c " $@"
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