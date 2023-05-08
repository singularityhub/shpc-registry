---
layout: container
name:  "quay.io/biocontainers/bioconductor-oct4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oct4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oct4/container.yaml"
updated_at: "2023-05-08 04:04:55.375230"
latest: "1.13.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oct4"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.13.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oct4"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oct4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oct4", "latest": {"1.13.0--r42hdfd78af_0": "sha256:85633a5835760f8966ca4cca6419f273ba298fed3d5fc41b6a40b5a6cd008ffd"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:73a49bec10fa4164f6a98ba6883c2e4ca80075369a11e1df138a2eb499d397fa", "1.10.0--r41hdfd78af_1": "sha256:3ae7545121dc8999620116b2e27bc4d6d28c4444dfa0735ef8ed39f0bdc303d6", "1.13.0--r42hdfd78af_0": "sha256:85633a5835760f8966ca4cca6419f273ba298fed3d5fc41b6a40b5a6cd008ffd"}, "docker": "quay.io/biocontainers/bioconductor-oct4", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oct4.
shpc-registry automated BioContainers addition for bioconductor-oct4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oct4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oct4:1.13.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oct4/1.13.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-oct4/1.13.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oct4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oct4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oct4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oct4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oct4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oct4-inspect-deffile:

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