---
layout: container
name:  "quay.io/biocontainers/bioconductor-coregnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-coregnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-coregnet/container.yaml"
updated_at: "2025-05-19 03:30:13.088859"
latest: "1.38.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-coregnet"
aliases:
 - "glpsol"
versions:
 - "1.32.0--r41hc0cfd56_2"
 - "1.36.0--r42hc0cfd56_0"
 - "1.36.0--r42ha9d7317_2"
 - "1.38.0--r43ha9d7317_0"
 - "1.38.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-coregnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-coregnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-coregnet", "latest": {"1.38.0--r43ha9d7317_1": "sha256:c6ebe3cc22b9bb0308660d1b7ae89a20d14827a8f4b9b346c3bc9ed146f8a9b2"}, "tags": {"1.32.0--r41hc0cfd56_2": "sha256:e1d16ac6afb96a0cdab9c0b0c3f8db2f496ad2bff5917c64a15d5d502a0e3d0b", "1.36.0--r42hc0cfd56_0": "sha256:c721a18fa153e5809162ba2af04785e117a020da9752aeedf01e0293597d2dd2", "1.36.0--r42ha9d7317_2": "sha256:c89ed8a4347761771942a5937d9c3e793d8191aa05b8566752a51446f699f85f", "1.38.0--r43ha9d7317_0": "sha256:cbbb6e9c17c2d0e56c530ceca0c2120c65dc71f62cdf6ed0270454aa0efa94ee", "1.38.0--r43ha9d7317_1": "sha256:c6ebe3cc22b9bb0308660d1b7ae89a20d14827a8f4b9b346c3bc9ed146f8a9b2"}, "docker": "quay.io/biocontainers/bioconductor-coregnet", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-coregnet.
shpc-registry automated BioContainers addition for bioconductor-coregnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-coregnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-coregnet:1.38.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-coregnet/1.38.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-coregnet/1.38.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-coregnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coregnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coregnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-coregnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-coregnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-coregnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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