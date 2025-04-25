---
layout: container
name:  "quay.io/biocontainers/bioconductor-gpart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gpart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gpart/container.yaml"
updated_at: "2025-04-25 02:57:32.883464"
latest: "1.12.0--r41h399db7b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gpart"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_1"
 - "1.12.0--r41h399db7b_0"
 - "1.10.0--r41h399db7b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gpart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gpart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gpart", "latest": {"1.12.0--r41h399db7b_0": "sha256:b285d12ed11c155f611d52059fbd5c095a3442b6b03a9ad226e428a765ecdfbd"}, "tags": {"1.8.0--r40h399db7b_1": "sha256:6ca0724efb65ce9b7f9e2e18a0d73cb40b9d8de598c5f578bd4ec981a115925f", "1.12.0--r41h399db7b_0": "sha256:b285d12ed11c155f611d52059fbd5c095a3442b6b03a9ad226e428a765ecdfbd", "1.10.0--r41h399db7b_0": "sha256:d5cf22aee5c750436ce1b48c206120157eca41e89cf99b0b2507f7e5235a9e78"}, "docker": "quay.io/biocontainers/bioconductor-gpart", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gpart.
shpc-registry automated BioContainers addition for bioconductor-gpart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gpart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gpart:1.12.0--r41h399db7b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gpart/1.12.0--r41h399db7b_0
$ module help quay.io/biocontainers/bioconductor-gpart/1.12.0--r41h399db7b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gpart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gpart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gpart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gpart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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