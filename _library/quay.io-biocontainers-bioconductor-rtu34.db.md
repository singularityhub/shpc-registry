---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtu34.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtu34.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtu34.db/container.yaml"
updated_at: "2025-05-05 03:58:35.546880"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-rtu34.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-rtu34.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtu34.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtu34.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:b909f6c73a825121ee1e57c807a7e31214ed8b0388e8f906a49da8f8e7847d4a"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:0987310da61db7ce8e008747c37560a9f1c0230977ad39573094d9bd8fe5bf50", "3.13.0--r42hdfd78af_2": "sha256:6436ada9d592ad155b28a0b6d8e60f76aef504f462ae0d00fdab5c5d604a64bc", "3.13.0--r43hdfd78af_3": "sha256:4e73c3a3f906f5c568bcb02c78dfc98e91ef0f9d59717f38cd4f72e238fd2e85", "3.13.0--r43hdfd78af_4": "sha256:9eaa3c888d3a14b9f440fbc117df3f89ffffc20dd70dac35a728bda7c2a176fa", "3.13.0--r44hdfd78af_5": "sha256:b909f6c73a825121ee1e57c807a7e31214ed8b0388e8f906a49da8f8e7847d4a"}, "docker": "quay.io/biocontainers/bioconductor-rtu34.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtu34.db.
shpc-registry automated BioContainers addition for bioconductor-rtu34.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtu34.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtu34.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtu34.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-rtu34.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtu34.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtu34.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtu34.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtu34.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtu34.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtu34.db-inspect-deffile:

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