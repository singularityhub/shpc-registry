---
layout: container
name:  "quay.io/biocontainers/bioconductor-expressionview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-expressionview/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-expressionview/container.yaml"
updated_at: "2024-10-26 03:25:14.884225"
latest: "1.42.0--r40h399db7b_1"
container_url: "https://biocontainers.pro/tools/bioconductor-expressionview"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.42.0--r40h399db7b_1"
description: "shpc-registry automated BioContainers addition for bioconductor-expressionview"
config: {"url": "https://biocontainers.pro/tools/bioconductor-expressionview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-expressionview", "latest": {"1.42.0--r40h399db7b_1": "sha256:c1b7f58f22a4e43d16c2a6579cd50f4ba79547b880b3a0dc26f900bdb3574bff"}, "tags": {"1.42.0--r40h399db7b_1": "sha256:c1b7f58f22a4e43d16c2a6579cd50f4ba79547b880b3a0dc26f900bdb3574bff"}, "docker": "quay.io/biocontainers/bioconductor-expressionview", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-expressionview.
shpc-registry automated BioContainers addition for bioconductor-expressionview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-expressionview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-expressionview:1.42.0--r40h399db7b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-expressionview/1.42.0--r40h399db7b_1
$ module help quay.io/biocontainers/bioconductor-expressionview/1.42.0--r40h399db7b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-expressionview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-expressionview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-expressionview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-expressionview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-expressionview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-expressionview-inspect-deffile:

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