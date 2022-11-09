---
layout: container
name:  "quay.io/biocontainers/autodock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autodock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autodock/container.yaml"
updated_at: "2022-11-09 00:31:27.515850"
latest: "4.2.6--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/autodock"
aliases:
 - "autodock4"
 - "autodock4.omp"
versions:
 - "4.2.6--h9f5acd7_1"
description: "shpc-registry automated BioContainers addition for autodock"
config: {"url": "https://biocontainers.pro/tools/autodock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for autodock", "latest": {"4.2.6--h9f5acd7_1": "sha256:7e885b64621b5c311b10889785143e580a323ca0281ca515c7c5c8ba475e8399"}, "tags": {"4.2.6--h9f5acd7_1": "sha256:7e885b64621b5c311b10889785143e580a323ca0281ca515c7c5c8ba475e8399"}, "docker": "quay.io/biocontainers/autodock", "aliases": {"autodock4": "/usr/local/bin/autodock4", "autodock4.omp": "/usr/local/bin/autodock4.omp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autodock.
shpc-registry automated BioContainers addition for autodock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autodock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autodock:4.2.6--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autodock/4.2.6--h9f5acd7_1
$ module help quay.io/biocontainers/autodock/4.2.6--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autodock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autodock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autodock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autodock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autodock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autodock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autodock4

```bash
$ singularity exec <container> /usr/local/bin/autodock4
$ podman run --it --rm --entrypoint /usr/local/bin/autodock4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autodock4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autodock4.omp

```bash
$ singularity exec <container> /usr/local/bin/autodock4.omp
$ podman run --it --rm --entrypoint /usr/local/bin/autodock4.omp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autodock4.omp   -v ${PWD} -w ${PWD} <container> -c " $@"
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