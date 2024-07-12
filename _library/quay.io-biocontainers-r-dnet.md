---
layout: container
name:  "quay.io/biocontainers/r-dnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-dnet/container.yaml"
updated_at: "2024-07-12 02:35:27.614421"
latest: "1.1.7--r43h3342da4_5"
container_url: "https://biocontainers.pro/tools/r-dnet"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.7--r41h3342da4_3"
 - "1.1.7--r42h3342da4_4"
 - "1.1.7--r43h3342da4_5"
description: "shpc-registry automated BioContainers addition for r-dnet"
config: {"url": "https://biocontainers.pro/tools/r-dnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-dnet", "latest": {"1.1.7--r43h3342da4_5": "sha256:2e9c4f06d5dfca87f5d0dfaa8d0b971381876b5d50e78947312691dfd6686e81"}, "tags": {"1.1.7--r41h3342da4_3": "sha256:01cfc7637677e1abaa2c9ff1e1f6de7f13819a21131ed4deb7658488da4fb5f5", "1.1.7--r42h3342da4_4": "sha256:b9a3178e1e773c517bf6836bfd36ed394ccfa6c20ac4ce5a3eb09dbe46980105", "1.1.7--r43h3342da4_5": "sha256:2e9c4f06d5dfca87f5d0dfaa8d0b971381876b5d50e78947312691dfd6686e81"}, "docker": "quay.io/biocontainers/r-dnet", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dnet.
shpc-registry automated BioContainers addition for r-dnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dnet:1.1.7--r43h3342da4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dnet/1.1.7--r43h3342da4_5
$ module help quay.io/biocontainers/r-dnet/1.1.7--r43h3342da4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dnet-inspect-deffile:

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