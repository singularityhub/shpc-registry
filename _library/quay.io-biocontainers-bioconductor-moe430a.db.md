---
layout: container
name:  "quay.io/biocontainers/bioconductor-moe430a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moe430a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moe430a.db/container.yaml"
updated_at: "2023-05-14 02:38:30.414700"
latest: "3.13.0--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-moe430a.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-moe430a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moe430a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moe430a.db", "latest": {"3.13.0--r42hdfd78af_2": "sha256:5f761831fc783e6399ead260826f6d6ff571dde36ebc15d1e58efb62d4a2e34e"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:0e9c4ce223cdda8b561891164833a913cb6b6285adc7d2ca3fd62b3d675d92d1", "3.13.0--r41hdfd78af_1": "sha256:7937af599c756318a86ee442af654e67b22fad2c6066e99d3b13a19d35c6ba9d", "3.13.0--r42hdfd78af_2": "sha256:5f761831fc783e6399ead260826f6d6ff571dde36ebc15d1e58efb62d4a2e34e"}, "docker": "quay.io/biocontainers/bioconductor-moe430a.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moe430a.db.
shpc-registry automated BioContainers addition for bioconductor-moe430a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430a.db:3.13.0--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moe430a.db/3.13.0--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-moe430a.db/3.13.0--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moe430a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moe430a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moe430a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moe430a.db-inspect-deffile:

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