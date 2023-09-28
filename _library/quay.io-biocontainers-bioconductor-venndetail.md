---
layout: container
name:  "quay.io/biocontainers/bioconductor-venndetail"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-venndetail/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-venndetail/container.yaml"
updated_at: "2023-09-28 03:36:17.668004"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-venndetail"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-venndetail"
config: {"url": "https://biocontainers.pro/tools/bioconductor-venndetail", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-venndetail", "latest": {"1.16.0--r43hdfd78af_0": "sha256:25e0ba4a5e5de218c2c44d36a7ef8df555f0d19c1cddd486dc7c622a3ff90928"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:85bf8cedb7ceb2b075e07f95f73d36a7cef6f6f1d37103835630b82e0cb898d9", "1.14.0--r42hdfd78af_0": "sha256:4b189b7d12c33e5deb5165e7375058c24feea365c94d9373f588d4e9f3bdee43", "1.10.0--r41hdfd78af_0": "sha256:7f184345b374a0424ad6933529d9193f72ddc97448ab01ffb9ef82028cad41d9", "1.16.0--r43hdfd78af_0": "sha256:25e0ba4a5e5de218c2c44d36a7ef8df555f0d19c1cddd486dc7c622a3ff90928"}, "docker": "quay.io/biocontainers/bioconductor-venndetail", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-venndetail.
shpc-registry automated BioContainers addition for bioconductor-venndetail
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-venndetail
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-venndetail:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-venndetail/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-venndetail/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-venndetail-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-venndetail-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-venndetail-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-venndetail-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-venndetail-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-venndetail-inspect-deffile:

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