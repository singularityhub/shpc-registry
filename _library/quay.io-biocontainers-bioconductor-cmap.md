---
layout: container
name:  "quay.io/biocontainers/bioconductor-cmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cmap/container.yaml"
updated_at: "2022-11-21 13:08:45.606683"
latest: "1.15.1--r41hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-cmap"
aliases:
 - ".bioconductor-cmap-post-link.sh"
 - ".bioconductor-cmap-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.15.1--r40hdfd78af_9"
 - "1.15.1--r41hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-cmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cmap", "latest": {"1.15.1--r41hdfd78af_12": "sha256:edd28b1613447880bf593f3e7ab7930b2792c275d8a484b825a8e4c81f6eaaa9"}, "tags": {"1.15.1--r40hdfd78af_9": "sha256:e9bbaa68cc1d35e8c91394485bab68b3c82f6803c5a41470cb973d0a6bafe702", "1.15.1--r41hdfd78af_12": "sha256:edd28b1613447880bf593f3e7ab7930b2792c275d8a484b825a8e4c81f6eaaa9"}, "docker": "quay.io/biocontainers/bioconductor-cmap", "aliases": {".bioconductor-cmap-post-link.sh": "/usr/local/bin/.bioconductor-cmap-post-link.sh", ".bioconductor-cmap-pre-unlink.sh": "/usr/local/bin/.bioconductor-cmap-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cmap.
shpc-registry automated BioContainers addition for bioconductor-cmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap:1.15.1--r41hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cmap/1.15.1--r41hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-cmap/1.15.1--r41hdfd78af_12
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


#### .bioconductor-cmap-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-cmap-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-cmap-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-cmap-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-cmap-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-cmap-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-cmap-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-cmap-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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