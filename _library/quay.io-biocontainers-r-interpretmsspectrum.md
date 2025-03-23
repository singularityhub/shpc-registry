---
layout: container
name:  "quay.io/biocontainers/r-interpretmsspectrum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-interpretmsspectrum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-interpretmsspectrum/container.yaml"
updated_at: "2025-03-23 03:33:42.363676"
latest: "1.3.3--r43h3342da4_1"
container_url: "https://biocontainers.pro/tools/r-interpretmsspectrum"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.2--r41h3342da4_2"
 - "1.3.3--r42h3342da4_0"
 - "1.2--r42h3342da4_3"
 - "1.3.3--r43h3342da4_1"
description: "shpc-registry automated BioContainers addition for r-interpretmsspectrum"
config: {"url": "https://biocontainers.pro/tools/r-interpretmsspectrum", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-interpretmsspectrum", "latest": {"1.3.3--r43h3342da4_1": "sha256:b5cb91f41a532da626e21d66c9780c2d48489cea5541238bcde90a8efdf93cf2"}, "tags": {"1.2--r41h3342da4_2": "sha256:b2af360966d64406f167f8c6b4d7110ad75f7ded4ccc13895dbe563262da1d63", "1.3.3--r42h3342da4_0": "sha256:2e44ec84bd379c6a8691a6ce33f45c4c6fe6f5909f4a08a8102776a3b3a4472a", "1.2--r42h3342da4_3": "sha256:142b7651a8340b2b6de212a3df855b3e4c032fa4848436c2419e0332c371d3eb", "1.3.3--r43h3342da4_1": "sha256:b5cb91f41a532da626e21d66c9780c2d48489cea5541238bcde90a8efdf93cf2"}, "docker": "quay.io/biocontainers/r-interpretmsspectrum", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-interpretmsspectrum.
shpc-registry automated BioContainers addition for r-interpretmsspectrum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-interpretmsspectrum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-interpretmsspectrum:1.3.3--r43h3342da4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-interpretmsspectrum/1.3.3--r43h3342da4_1
$ module help quay.io/biocontainers/r-interpretmsspectrum/1.3.3--r43h3342da4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-interpretmsspectrum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-interpretmsspectrum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-interpretmsspectrum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-interpretmsspectrum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-interpretmsspectrum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-interpretmsspectrum-inspect-deffile:

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