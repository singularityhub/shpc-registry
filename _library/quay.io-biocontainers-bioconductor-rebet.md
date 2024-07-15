---
layout: container
name:  "quay.io/biocontainers/bioconductor-rebet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rebet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rebet/container.yaml"
updated_at: "2024-07-15 03:01:27.903828"
latest: "1.20.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rebet"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hd029910_1"
 - "1.16.0--r42hc0cfd56_0"
 - "1.12.0--r41hc0cfd56_2"
 - "1.10.0--r41hd029910_0"
 - "1.16.0--r42ha9d7317_1"
 - "1.18.0--r43ha9d7317_0"
 - "1.20.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rebet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rebet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rebet", "latest": {"1.20.0--r43ha9d7317_0": "sha256:b5edc0105adaeeaebf6cdf8859694567b7d4af8bed0001f9ebc64152df6bd185"}, "tags": {"1.8.0--r40hd029910_1": "sha256:dfe0d0a6acdf391425d5b21de2fbd1b591d543ac79399fb919b9d514ee07cd02", "1.16.0--r42hc0cfd56_0": "sha256:757ae249d2ee44cd192ece02b8cec6da0f330805a7d5d8355dda152df9fa67f1", "1.12.0--r41hc0cfd56_2": "sha256:e6c92d2712b589c871aa064d8044abd29966a65525d3d72ce3ba12e5fe04c31e", "1.10.0--r41hd029910_0": "sha256:64c83a3608e641d4dc72a0de46a307f7c92be6bf89c8ed85d3fe15a2f991d631", "1.16.0--r42ha9d7317_1": "sha256:3d7877b35c247bcea0816d65ff7c99a80552a81a47902fbd55afed7df3b5d06f", "1.18.0--r43ha9d7317_0": "sha256:6be29a3c300917214cb5d2e1965ac7cda95c9642677c1ba3b567a0be7f40ae56", "1.20.0--r43ha9d7317_0": "sha256:b5edc0105adaeeaebf6cdf8859694567b7d4af8bed0001f9ebc64152df6bd185"}, "docker": "quay.io/biocontainers/bioconductor-rebet", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rebet.
shpc-registry automated BioContainers addition for bioconductor-rebet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rebet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rebet:1.20.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rebet/1.20.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-rebet/1.20.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rebet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rebet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rebet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rebet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rebet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rebet-inspect-deffile:

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