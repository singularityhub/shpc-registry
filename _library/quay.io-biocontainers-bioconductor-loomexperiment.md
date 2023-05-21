---
layout: container
name:  "quay.io/biocontainers/bioconductor-loomexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-loomexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-loomexperiment/container.yaml"
updated_at: "2023-05-21 02:50:57.715830"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-loomexperiment"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.1--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-loomexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-loomexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-loomexperiment", "latest": {"1.16.0--r42hdfd78af_0": "sha256:62d4e98af0ceb5cd30441331373a1efc8e5ca132e1159245280996e5e02ea4bc"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:1fbfa4e02edb29aae320bf632f2aa1145424995cf45e15ced943088584acec46", "1.16.0--r42hdfd78af_0": "sha256:62d4e98af0ceb5cd30441331373a1efc8e5ca132e1159245280996e5e02ea4bc", "1.12.0--r41hdfd78af_0": "sha256:06545208a1fb07b39e6986d7a973cf35b53fa23e734c808a1df5b7cb7c4a8be8", "1.10.1--r41hdfd78af_0": "sha256:cf269c56b758cca08d940399f3d8a5edf26e238bb04e6710ec1ff77978e4cf7e"}, "docker": "quay.io/biocontainers/bioconductor-loomexperiment", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-loomexperiment.
shpc-registry automated BioContainers addition for bioconductor-loomexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-loomexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-loomexperiment:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-loomexperiment/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-loomexperiment/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-loomexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-loomexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-loomexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-loomexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-loomexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-loomexperiment-inspect-deffile:

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