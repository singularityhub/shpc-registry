---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecoli2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecoli2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecoli2.db/container.yaml"
updated_at: "2025-09-04 03:26:45.323580"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-ecoli2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-ecoli2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecoli2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecoli2.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:2c0482b9802b1e6cae5a86f292f38274c4be12ea3b8127f2ce98a8d1228b2dfe"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:2b301fca27e2e30311e04769855445a241c1bb21276331f19558848271cca733", "3.13.0--r41hdfd78af_1": "sha256:6067fecb3110eb9e76bcb9b8bd0148319cef1d79e2d0af3b0c057017fff4d6c8", "3.13.0--r42hdfd78af_2": "sha256:9bd0822a69ccf45802be4d228c9d9af6200ad0fee5a207cb4da8ff0b9cc13101", "3.13.0--r43hdfd78af_3": "sha256:874c9c0b0fb6ab758811cd9b8e39704871bcd0c0713196dc8b87bb7e01b2883b", "3.13.0--r43hdfd78af_4": "sha256:164e5d7c9b7bbd3504122b2b1ffec987738043fbbb081529c885aa4f6947e796", "3.13.0--r44hdfd78af_5": "sha256:2c0482b9802b1e6cae5a86f292f38274c4be12ea3b8127f2ce98a8d1228b2dfe"}, "docker": "quay.io/biocontainers/bioconductor-ecoli2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecoli2.db.
shpc-registry automated BioContainers addition for bioconductor-ecoli2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoli2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoli2.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecoli2.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-ecoli2.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecoli2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoli2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoli2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecoli2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecoli2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecoli2.db-inspect-deffile:

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