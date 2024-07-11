---
layout: container
name:  "quay.io/biocontainers/bioconductor-mugaexampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mugaexampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mugaexampledata/container.yaml"
updated_at: "2024-07-11 03:06:23.861836"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mugaexampledata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mugaexampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mugaexampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mugaexampledata", "latest": {"1.22.0--r43hdfd78af_0": "sha256:3e0971ee4dedccd71d7c46ebd4665ac1b3b709a5e0184bfb3267730e5233b530"}, "tags": {"1.9.0--r40_0": "sha256:b5b98de92801f9fa7b3e17857822b60098403986b15e510fac562c7a51da7125", "1.17.0--r42hdfd78af_0": "sha256:46161e7af12a157ba941f6321b920bfe87dab1da8691ec7813575dc21d4ee4ee", "1.14.0--r41hdfd78af_1": "sha256:eb3aa79e48ba14e9054c3c56cb7c0b9a855599b9b644fa87a3a4ecb713c4f3f9", "1.12.0--r41hdfd78af_0": "sha256:42753e4c033085871cd5e68bf9cc56defec87c55e6050f034d546d4aaef6808c", "1.10.0--r40hdfd78af_1": "sha256:293f4457669c34392693df36e86b6ae7c3769cbc49851b36cae4d0fe6006226d", "1.20.0--r43hdfd78af_0": "sha256:7f3ebbcde8f431dbc61b1e1a78e983a9f7604ea95296796ab7b3a2714e092936", "1.22.0--r43hdfd78af_0": "sha256:3e0971ee4dedccd71d7c46ebd4665ac1b3b709a5e0184bfb3267730e5233b530"}, "docker": "quay.io/biocontainers/bioconductor-mugaexampledata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mugaexampledata.
shpc-registry automated BioContainers addition for bioconductor-mugaexampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mugaexampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mugaexampledata:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mugaexampledata/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mugaexampledata/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mugaexampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mugaexampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mugaexampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mugaexampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mugaexampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mugaexampledata-inspect-deffile:

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