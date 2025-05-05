---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95e.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95e.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95e.db/container.yaml"
updated_at: "2025-05-05 03:59:41.690744"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95e.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95e.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95e.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95e.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:ac8cd37a18f07cc776d4193b36cc100228d6aa2ff98b6d8ed7cae876cf137a81"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:a34771cde0780cf2c66b7ab98fabd92138be8d4ac9a18ab1e61da5a094355cf0", "3.13.0--r42hdfd78af_2": "sha256:5af0e1d22a10469e5f5ea03a5f807df4ba8c984fb295d5f86c63213a738995e3", "3.13.0--r43hdfd78af_3": "sha256:caee01ea2199498eb067f971312f16374e42976874ec8875e546696e0fe8ffa6", "3.13.0--r43hdfd78af_4": "sha256:62e63c3a63523495f95405cac50bada250a3b71c6966bd6b145d33f1624fb4d5", "3.13.0--r44hdfd78af_5": "sha256:ac8cd37a18f07cc776d4193b36cc100228d6aa2ff98b6d8ed7cae876cf137a81"}, "docker": "quay.io/biocontainers/bioconductor-hgu95e.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95e.db.
shpc-registry automated BioContainers addition for bioconductor-hgu95e.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95e.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95e.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95e.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-hgu95e.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95e.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95e.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95e.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95e.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95e.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95e.db-inspect-deffile:

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