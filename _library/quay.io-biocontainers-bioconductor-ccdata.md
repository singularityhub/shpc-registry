---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccdata/container.yaml"
updated_at: "2025-08-28 12:34:44.393070"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccdata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccdata", "latest": {"1.32.0--r44hdfd78af_0": "sha256:51a22b1e735d5efc4c50bac6a3e0eef71ca4d08797f2e8230afb2bf3298c0eb2"}, "tags": {"1.8.0--r351_0": "sha256:dcbec2bd6334a908d977012c34575b792700841c3a1dd1cc0846340d289e6a1f", "1.24.0--r42hdfd78af_0": "sha256:81f28724f77c3188cf45a401701461d8d358cb4cc0fce8b62313b9e12387b410", "1.23.0--r42hdfd78af_0": "sha256:3ffaf80bf3ba3021a672a016700d674b97fbe29004bfd38bac97e7f5d80c83c2", "1.20.0--r41hdfd78af_1": "sha256:5c60fd2261f016047c4810d21a747c4ea00ae4356dcb4c673d3c6015b374252b", "1.18.0--r41hdfd78af_0": "sha256:81e5cd8f9adfac7e0922991571e217a0407bc347f6799ad5466bf2433d5388b3", "1.16.0--r40hdfd78af_1": "sha256:efbde2eda5f28b25ce0a5e164a604cdcb22d0b14d1d8405393629f02e0534f07", "1.26.0--r43hdfd78af_0": "sha256:4558486f57fb59a83273f669ca47fb5d4db07a3efc5bffe7fd09a9f0ec8ba87e", "1.28.0--r43hdfd78af_0": "sha256:7ddd13e75304473bc39d4c25050f22026e69185d770ea6c9e6a4c0ef71af38e6", "1.32.0--r44hdfd78af_0": "sha256:51a22b1e735d5efc4c50bac6a3e0eef71ca4d08797f2e8230afb2bf3298c0eb2"}, "docker": "quay.io/biocontainers/bioconductor-ccdata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccdata.
shpc-registry automated BioContainers addition for bioconductor-ccdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccdata:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccdata/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ccdata/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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