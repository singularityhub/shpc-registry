---
layout: container
name:  "quay.io/biocontainers/r-shaman"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-shaman/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-shaman/container.yaml"
updated_at: "2024-11-28 03:24:49.556105"
latest: "2.0--r43hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-shaman"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.0--r41hdfd78af_4"
 - "2.0--r42hdfd78af_5"
 - "2.0--r43hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-shaman"
config: {"url": "https://biocontainers.pro/tools/r-shaman", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-shaman", "latest": {"2.0--r43hdfd78af_6": "sha256:6f01259f74aae67ce1c0346f5bb4429211c7b5e531f42253ac492dfd7ec4096d"}, "tags": {"2.0--r41hdfd78af_4": "sha256:62cea04adac401b2f54635cde6ae6434637fc7c2c87eab04a5a02614f9dea757", "2.0--r42hdfd78af_5": "sha256:adb121c69553532c3345e0142ca13d7663c5e369d711a7bfd9dd7032c033a385", "2.0--r43hdfd78af_6": "sha256:6f01259f74aae67ce1c0346f5bb4429211c7b5e531f42253ac492dfd7ec4096d"}, "docker": "quay.io/biocontainers/r-shaman", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-shaman.
shpc-registry automated BioContainers addition for r-shaman
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-shaman
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-shaman:2.0--r43hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-shaman/2.0--r43hdfd78af_6
$ module help quay.io/biocontainers/r-shaman/2.0--r43hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-shaman-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-shaman-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-shaman-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-shaman-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-shaman-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-shaman-inspect-deffile:

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