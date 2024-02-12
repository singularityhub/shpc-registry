---
layout: container
name:  "quay.io/biocontainers/bioconductor-modstrings"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-modstrings/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-modstrings/container.yaml"
updated_at: "2024-02-12 02:59:16.835371"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-modstrings"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-modstrings"
config: {"url": "https://biocontainers.pro/tools/bioconductor-modstrings", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-modstrings", "latest": {"1.18.0--r43hdfd78af_0": "sha256:9596433c18f332717392743d05a9405e0d3189acc8f6effb4e03c95f2ccbf9e2"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:1f8d6a297c6273424676bc4c52972d74620763c18e0a496ef900c50f4076d0af", "1.14.0--r42hdfd78af_0": "sha256:0e6b0876c32ece4d60f67a8534a45294b311fea77f965c31a007d58bfb036e05", "1.10.0--r41hdfd78af_0": "sha256:921f415d2786267bd074ed3258c0371bbf1efa188efd73ed00644d89c52ef911", "1.16.0--r43hdfd78af_0": "sha256:dfcb0d6014532805f4d99227ed40e4ea5f2470300a85aad0bf897240d9bed93e", "1.18.0--r43hdfd78af_0": "sha256:9596433c18f332717392743d05a9405e0d3189acc8f6effb4e03c95f2ccbf9e2"}, "docker": "quay.io/biocontainers/bioconductor-modstrings", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-modstrings.
shpc-registry automated BioContainers addition for bioconductor-modstrings
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-modstrings
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-modstrings:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-modstrings/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-modstrings/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-modstrings-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-modstrings-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-modstrings-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-modstrings-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-modstrings-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-modstrings-inspect-deffile:

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