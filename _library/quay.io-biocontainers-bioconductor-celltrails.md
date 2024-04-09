---
layout: container
name:  "quay.io/biocontainers/bioconductor-celltrails"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celltrails/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celltrails/container.yaml"
updated_at: "2024-04-09 02:23:18.181235"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-celltrails"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-celltrails"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celltrails", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celltrails", "latest": {"1.20.0--r43hdfd78af_0": "sha256:931a7e5e9575b4b266bee7abed70e57ed441ab26a18b1c6e8a45f0d5bf38124f"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:a07ba68691a04cbfc70d9ff2c5da5ba5fed59788a834b7262590f82941d38254", "1.16.0--r42hdfd78af_0": "sha256:9931d79f1bb6d856a5a354c823621d8dc24e663e7a908d2b15c2f8971a6229db", "1.12.0--r41hdfd78af_0": "sha256:a84debccee2236f6f1db176dc05e8ddc2695166fad9f0fadaa8fa62022f49805", "1.10.0--r41hdfd78af_0": "sha256:f64f7fe0a6c5ffb5eec35febe76d6206a887a30469f751e1d766aa4a61db82a7", "1.18.0--r43hdfd78af_0": "sha256:340b0c49d2f039ec8693c5d2482cdaa0d40e310e76441fbf304c36687fe020c4", "1.20.0--r43hdfd78af_0": "sha256:931a7e5e9575b4b266bee7abed70e57ed441ab26a18b1c6e8a45f0d5bf38124f"}, "docker": "quay.io/biocontainers/bioconductor-celltrails", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celltrails.
shpc-registry automated BioContainers addition for bioconductor-celltrails
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celltrails
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celltrails:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celltrails/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-celltrails/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celltrails-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celltrails-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celltrails-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celltrails-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celltrails-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celltrails-inspect-deffile:

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