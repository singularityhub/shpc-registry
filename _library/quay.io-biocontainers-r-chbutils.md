---
layout: container
name:  "quay.io/biocontainers/r-chbutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-chbutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-chbutils/container.yaml"
updated_at: "2023-06-19 03:15:48.234090"
latest: "0.1_2017_10_26--r42hdfd78af_5"
container_url: "https://biocontainers.pro/tools/r-chbutils"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1_2017_10_26--r41hdfd78af_4"
 - "0.1_2017_10_26--r42hdfd78af_5"
description: "shpc-registry automated BioContainers addition for r-chbutils"
config: {"url": "https://biocontainers.pro/tools/r-chbutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-chbutils", "latest": {"0.1_2017_10_26--r42hdfd78af_5": "sha256:feec0e448536adb9956e54f9d8cfba060cb04a5422b5e50da5f04cfb80c32c1e"}, "tags": {"0.1_2017_10_26--r41hdfd78af_4": "sha256:23dfec9157de0a36e5586f4e4565c2a4735685148c4e833cf3d8adbb3f39dbcc", "0.1_2017_10_26--r42hdfd78af_5": "sha256:feec0e448536adb9956e54f9d8cfba060cb04a5422b5e50da5f04cfb80c32c1e"}, "docker": "quay.io/biocontainers/r-chbutils", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-chbutils.
shpc-registry automated BioContainers addition for r-chbutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-chbutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-chbutils:0.1_2017_10_26--r42hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-chbutils/0.1_2017_10_26--r42hdfd78af_5
$ module help quay.io/biocontainers/r-chbutils/0.1_2017_10_26--r42hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-chbutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-chbutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-chbutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-chbutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-chbutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-chbutils-inspect-deffile:

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