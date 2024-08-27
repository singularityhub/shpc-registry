---
layout: container
name:  "quay.io/biocontainers/bioconductor-timeseriesexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-timeseriesexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-timeseriesexperiment/container.yaml"
updated_at: "2024-08-27 06:03:45.187579"
latest: "1.12.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-timeseriesexperiment"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-timeseriesexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-timeseriesexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-timeseriesexperiment", "latest": {"1.12.0--r41hdfd78af_0": "sha256:54fd85db5ce3c2cabd7335cdc99d0f3d3173440ccbce39fc50c41bda75f2c011"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:01961a5377c756748aa3cb2474008f65632500821e9f55d5a88b7fce7178ac6b", "1.12.0--r41hdfd78af_0": "sha256:54fd85db5ce3c2cabd7335cdc99d0f3d3173440ccbce39fc50c41bda75f2c011", "1.10.0--r41hdfd78af_0": "sha256:f091a4bf6a98692827c73d24ac31cd3ca637c15e176ebb3693927fede41d7890"}, "docker": "quay.io/biocontainers/bioconductor-timeseriesexperiment", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-timeseriesexperiment.
shpc-registry automated BioContainers addition for bioconductor-timeseriesexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-timeseriesexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-timeseriesexperiment:1.12.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-timeseriesexperiment/1.12.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-timeseriesexperiment/1.12.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-timeseriesexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timeseriesexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timeseriesexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-timeseriesexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-timeseriesexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-timeseriesexperiment-inspect-deffile:

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