---
layout: container
name:  "quay.io/biocontainers/bioconductor-champ"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-champ/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-champ/container.yaml"
updated_at: "2025-04-26 03:02:37.186214"
latest: "2.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-champ"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.22.0--r41hdfd78af_0"
 - "2.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-champ"
config: {"url": "https://biocontainers.pro/tools/bioconductor-champ", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-champ", "latest": {"2.28.0--r42hdfd78af_0": "sha256:f802b9709f7e60f529fc5cbe159b1bc3ad066c509a79490b1f1e8be470b80069"}, "tags": {"2.22.0--r41hdfd78af_0": "sha256:c0cd9f27cc89e1c8a367e2213b9f4be0b4f28fc7c9a5acd0c5e63cb637ba0321", "2.28.0--r42hdfd78af_0": "sha256:f802b9709f7e60f529fc5cbe159b1bc3ad066c509a79490b1f1e8be470b80069"}, "docker": "quay.io/biocontainers/bioconductor-champ", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-champ.
shpc-registry automated BioContainers addition for bioconductor-champ
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-champ
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-champ:2.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-champ/2.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-champ/2.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-champ-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-champ-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-champ-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-champ-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-champ-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-champ-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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