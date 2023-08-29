---
layout: container
name:  "quay.io/biocontainers/bioconductor-maftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maftools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maftools/container.yaml"
updated_at: "2023-08-29 03:39:33.310774"
latest: "2.16.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maftools"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hd029910_0"
 - "2.14.0--r42hc0cfd56_0"
 - "2.10.05--r41hc0cfd56_0"
 - "2.14.0--r42ha9d7317_1"
 - "2.16.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maftools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maftools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maftools", "latest": {"2.16.0--r43ha9d7317_0": "sha256:d2a29dccb5b62faf648cfd0f8896da35401b7c42f0e0d7b50c8df9077877a5df"}, "tags": {"2.8.0--r41hd029910_0": "sha256:bcabe3ce0167d6893b164345824bf233037f90152f687155923306fa9f7b0a73", "2.14.0--r42hc0cfd56_0": "sha256:85a197c81a55ad102b0e09fde189ccd6409e76e24d540e89bda27eb69e2cd954", "2.10.05--r41hc0cfd56_0": "sha256:058f7104c820216854a0b054a85f7224ebe2cf33977e5c9a931d86c02a6053e8", "2.14.0--r42ha9d7317_1": "sha256:28b7309e8bc7c2f38e14394d54104d874ad8ffee478d0589756c0e161a55131d", "2.16.0--r43ha9d7317_0": "sha256:d2a29dccb5b62faf648cfd0f8896da35401b7c42f0e0d7b50c8df9077877a5df"}, "docker": "quay.io/biocontainers/bioconductor-maftools", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maftools.
shpc-registry automated BioContainers addition for bioconductor-maftools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maftools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maftools:2.16.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maftools/2.16.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-maftools/2.16.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maftools-inspect-deffile:

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