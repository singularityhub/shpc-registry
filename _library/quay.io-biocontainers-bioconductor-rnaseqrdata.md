---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqrdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqrdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqrdata/container.yaml"
updated_at: "2025-08-24 03:29:17.529306"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqrdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqrdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqrdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqrdata", "latest": {"1.16.0--r42hdfd78af_0": "sha256:c6c9b7e7dd6ba5071ee3612af5bce50bbea28ea6576665749aefa2ecbd9f9283"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:0d1c4c1334598b027b016f03c30fae3ce0948b834490989310e05e159a5332fc", "1.16.0--r42hdfd78af_0": "sha256:c6c9b7e7dd6ba5071ee3612af5bce50bbea28ea6576665749aefa2ecbd9f9283", "1.12.0--r41hdfd78af_1": "sha256:f9aafe9397a4dd4fb92d89629c88aebab8f6a20ded1a21a71c4c0454c580dada", "1.10.0--r41hdfd78af_0": "sha256:16fa67aa9f5228fc1a2a2e4363e03574686eea47e50d85c202e0ddc883f2e510"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqrdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqrdata.
shpc-registry automated BioContainers addition for bioconductor-rnaseqrdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqrdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqrdata:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqrdata/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaseqrdata/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqrdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqrdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqrdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqrdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqrdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqrdata-inspect-deffile:

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