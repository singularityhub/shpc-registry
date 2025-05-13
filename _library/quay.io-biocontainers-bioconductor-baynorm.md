---
layout: container
name:  "quay.io/biocontainers/bioconductor-baynorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-baynorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-baynorm/container.yaml"
updated_at: "2025-05-13 03:42:05.156693"
latest: "1.24.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-baynorm"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_1"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.0--r41hc247a5b_2"
 - "1.16.0--r42hf17093f_1"
 - "1.18.1--r43hf17093f_0"
 - "1.20.0--r43hf17093f_0"
 - "1.24.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-baynorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-baynorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-baynorm", "latest": {"1.24.0--r44he5774e6_0": "sha256:0abd61dec8e4d02e8d34fc7e660e33f328652855d7295c81c2fd1c105ed0cfeb"}, "tags": {"1.8.0--r40h399db7b_1": "sha256:88285a0f0e14fad190212258d19605281f9f67310bb05b8e43f9ff052a73a3ca", "1.16.0--r42hc247a5b_0": "sha256:0a66485ab70b68d885e1f7b7b00a9cbfd74991f1c5a7063333fc72743ec6d077", "1.12.0--r41hc247a5b_2": "sha256:f38ec361af7e2119d7c273eeb71d01fd47ec7b9aed7081aeea31d4898b35c2fe", "1.16.0--r42hf17093f_1": "sha256:2b6d1a674fafda237f77ef2d86f922bb14265091d292e0795d8a8b993092cad3", "1.18.1--r43hf17093f_0": "sha256:086cef8ce8d2243333ff840db6b3aa62f0afef13e3ee1449e52e1c3867169e18", "1.20.0--r43hf17093f_0": "sha256:1aea56506b2a438d4ee4820c7b1cc8d13940c4da016613b156a34704aade2321", "1.24.0--r44he5774e6_0": "sha256:0abd61dec8e4d02e8d34fc7e660e33f328652855d7295c81c2fd1c105ed0cfeb"}, "docker": "quay.io/biocontainers/bioconductor-baynorm", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-baynorm.
shpc-registry automated BioContainers addition for bioconductor-baynorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-baynorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-baynorm:1.24.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-baynorm/1.24.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-baynorm/1.24.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-baynorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-baynorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-baynorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-baynorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-baynorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-baynorm-inspect-deffile:

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