---
layout: container
name:  "quay.io/biocontainers/bioconductor-strandcheckr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-strandcheckr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-strandcheckr/container.yaml"
updated_at: "2024-02-01 02:45:39.752970"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-strandcheckr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-strandcheckr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-strandcheckr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-strandcheckr", "latest": {"1.20.0--r43hdfd78af_0": "sha256:19082158060a9abc8884cb9eba2a700c2d477705d2b7937c5c5efdcf06f8260a"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:d589b767d949ff44c1ffd68462dd4e7d5234860d7059bd0bf9764b80d8e116b1", "1.16.0--r42hdfd78af_0": "sha256:1a0f358dfe477eb5aeb2d9b058f32d23b11bfc6a9c2d07468916a6e9c2a800e6", "1.12.0--r41hdfd78af_0": "sha256:78a88d84bc0d9ebe02e1f18c7a3bc3449dce0166684e0dd105afd5c21060ceea", "1.10.0--r41hdfd78af_0": "sha256:f8ad531bde19aa2b99228b2ec4f2832f7f0ce5ba45cdae92df7fd46c6a42458a", "1.18.0--r43hdfd78af_0": "sha256:afa0521863a19006e5ec9fcc3a2fcd7b0d0b86c2a7dfe12664d95f96512b4791", "1.20.0--r43hdfd78af_0": "sha256:19082158060a9abc8884cb9eba2a700c2d477705d2b7937c5c5efdcf06f8260a"}, "docker": "quay.io/biocontainers/bioconductor-strandcheckr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-strandcheckr.
shpc-registry automated BioContainers addition for bioconductor-strandcheckr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-strandcheckr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-strandcheckr:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-strandcheckr/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-strandcheckr/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-strandcheckr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-strandcheckr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-strandcheckr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-strandcheckr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-strandcheckr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-strandcheckr-inspect-deffile:

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