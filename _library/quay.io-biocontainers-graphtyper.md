---
layout: container
name:  "quay.io/biocontainers/graphtyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphtyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphtyper/container.yaml"
updated_at: "2023-04-25 03:01:45.547172"
latest: "2.7.2--h468198e_1"
container_url: "https://biocontainers.pro/tools/graphtyper"
aliases:
 - "graphtyper"
versions:
 - "2.7.2--h468198e_1"
description: "shpc-registry automated BioContainers addition for graphtyper"
config: {"url": "https://biocontainers.pro/tools/graphtyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphtyper", "latest": {"2.7.2--h468198e_1": "sha256:460157e9b228d9286bcf3a1d0169d6a25c7a46b3e651734adefadfe8ed428b12"}, "tags": {"2.7.2--h468198e_1": "sha256:460157e9b228d9286bcf3a1d0169d6a25c7a46b3e651734adefadfe8ed428b12"}, "docker": "quay.io/biocontainers/graphtyper", "aliases": {"graphtyper": "/usr/local/bin/graphtyper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphtyper.
shpc-registry automated BioContainers addition for graphtyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphtyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphtyper:2.7.2--h468198e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphtyper/2.7.2--h468198e_1
$ module help quay.io/biocontainers/graphtyper/2.7.2--h468198e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphtyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphtyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphtyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphtyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphtyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphtyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphtyper

```bash
$ singularity exec <container> /usr/local/bin/graphtyper
$ podman run --it --rm --entrypoint /usr/local/bin/graphtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
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