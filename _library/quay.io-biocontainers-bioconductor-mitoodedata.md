---
layout: container
name:  "quay.io/biocontainers/bioconductor-mitoodedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mitoodedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mitoodedata/container.yaml"
updated_at: "2023-09-09 02:26:27.596220"
latest: "1.26.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mitoodedata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.26.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mitoodedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mitoodedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mitoodedata", "latest": {"1.26.0--r40hdfd78af_1": "sha256:cf4884f01cf4e7fbfd1847964992e82e778e697cb2ed4939c6b8255110e053ea"}, "tags": {"1.26.0--r40hdfd78af_1": "sha256:cf4884f01cf4e7fbfd1847964992e82e778e697cb2ed4939c6b8255110e053ea"}, "docker": "quay.io/biocontainers/bioconductor-mitoodedata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mitoodedata.
shpc-registry automated BioContainers addition for bioconductor-mitoodedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mitoodedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mitoodedata:1.26.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mitoodedata/1.26.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-mitoodedata/1.26.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mitoodedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitoodedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitoodedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mitoodedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mitoodedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mitoodedata-inspect-deffile:

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