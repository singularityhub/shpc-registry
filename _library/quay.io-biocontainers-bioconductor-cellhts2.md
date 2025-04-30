---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellhts2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellhts2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellhts2/container.yaml"
updated_at: "2025-04-30 03:17:15.027575"
latest: "2.66.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellhts2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.56.0--r41hdfd78af_0"
 - "2.62.0--r42hdfd78af_0"
 - "2.64.0--r43hdfd78af_0"
 - "2.66.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellhts2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellhts2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellhts2", "latest": {"2.66.0--r43hdfd78af_0": "sha256:8bbca7a163f745e060489e4d9dbbf175d8d8cf73c602fbaa22b654c7c0bbeb54"}, "tags": {"2.56.0--r41hdfd78af_0": "sha256:41d610c3ff499607611867c36288730eec913b0a444010e10e2ceffa8744f180", "2.62.0--r42hdfd78af_0": "sha256:2f6641e54c747e63767f16f01664244d04fd1428a6a9bf0fcb827e0d5c64c6b7", "2.64.0--r43hdfd78af_0": "sha256:72c1dee327037ecb7f4882478367c40e74e5e9a649a8389db662b5b0d6044d24", "2.66.0--r43hdfd78af_0": "sha256:8bbca7a163f745e060489e4d9dbbf175d8d8cf73c602fbaa22b654c7c0bbeb54"}, "docker": "quay.io/biocontainers/bioconductor-cellhts2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellhts2.
shpc-registry automated BioContainers addition for bioconductor-cellhts2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellhts2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellhts2:2.66.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellhts2/2.66.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellhts2/2.66.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellhts2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellhts2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellhts2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellhts2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellhts2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellhts2-inspect-deffile:

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