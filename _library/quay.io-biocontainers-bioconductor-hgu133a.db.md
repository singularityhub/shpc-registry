---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133a.db/container.yaml"
updated_at: "2025-02-21 03:31:24.512405"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133a.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r40_9"
 - "3.13.0--r41hdfd78af_1"
 - "3.2.3--r41hdfd78af_11"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133a.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:fc61b134f2e201211b23b1a66286c819e0b298f6ffb9965e5c38bb42788018b0"}, "tags": {"3.2.3--r40_9": "sha256:59037c961d06983598dda870c9013d77cad4fe9184db014730ff8516a38e179b", "3.13.0--r41hdfd78af_1": "sha256:25e1622daeead37783c064448b7044fb9c1f90b8c6e335c5a878fd1622ea4da2", "3.2.3--r41hdfd78af_11": "sha256:7985472b0d3d71d8a48baf3846595883143cdea667ffe722f90a6fee379f789f", "3.13.0--r42hdfd78af_2": "sha256:f45ff4f8e268ce013cf70ea4a5c2b96ba48d919ae71182e99932b49fa285b842", "3.13.0--r43hdfd78af_3": "sha256:30209ebdaf8a94c4f62945ad4f48527cf6c5323e76efc4e01adefd8873c23c4b", "3.13.0--r43hdfd78af_4": "sha256:fc61b134f2e201211b23b1a66286c819e0b298f6ffb9965e5c38bb42788018b0"}, "docker": "quay.io/biocontainers/bioconductor-hgu133a.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133a.db.
shpc-registry automated BioContainers addition for bioconductor-hgu133a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133a.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hgu133a.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133a.db-inspect-deffile:

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