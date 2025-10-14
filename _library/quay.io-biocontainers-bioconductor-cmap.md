---
layout: container
name:  "quay.io/biocontainers/bioconductor-cmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cmap/container.yaml"
updated_at: "2025-10-14 03:08:07.032020"
latest: "1.15.1--r44hdfd78af_16"
container_url: "https://biocontainers.pro/tools/bioconductor-cmap"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.15.1--r40hdfd78af_9"
 - "1.15.1--r41hdfd78af_12"
 - "1.15.1--r42hdfd78af_13"
 - "1.15.1--r43hdfd78af_14"
 - "1.15.1--r43hdfd78af_15"
 - "1.15.1--r44hdfd78af_16"
description: "shpc-registry automated BioContainers addition for bioconductor-cmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cmap", "latest": {"1.15.1--r44hdfd78af_16": "sha256:85094bf35373347381789f4d48104b2e5dd5ec57fac690a4c869bb60b9c8899e"}, "tags": {"1.15.1--r40hdfd78af_9": "sha256:e9bbaa68cc1d35e8c91394485bab68b3c82f6803c5a41470cb973d0a6bafe702", "1.15.1--r41hdfd78af_12": "sha256:edd28b1613447880bf593f3e7ab7930b2792c275d8a484b825a8e4c81f6eaaa9", "1.15.1--r42hdfd78af_13": "sha256:f7f9e5efd4603c909648557e38fb64264b106f0622219c83627f55630dffaaa6", "1.15.1--r43hdfd78af_14": "sha256:eac984f01cf9e7876e37d5f32b1a575d4c8bad2c8e0ebf59ec6b9efafa550c8f", "1.15.1--r43hdfd78af_15": "sha256:e38028367e78880d8719134efc4db55542501e283352d3accd1b5ad3a97c3d3f", "1.15.1--r44hdfd78af_16": "sha256:85094bf35373347381789f4d48104b2e5dd5ec57fac690a4c869bb60b9c8899e"}, "docker": "quay.io/biocontainers/bioconductor-cmap", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cmap.
shpc-registry automated BioContainers addition for bioconductor-cmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap:1.15.1--r44hdfd78af_16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cmap/1.15.1--r44hdfd78af_16
$ module help quay.io/biocontainers/bioconductor-cmap/1.15.1--r44hdfd78af_16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cmap-inspect-deffile:

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