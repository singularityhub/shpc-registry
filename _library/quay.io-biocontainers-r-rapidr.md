---
layout: container
name:  "quay.io/biocontainers/r-rapidr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rapidr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rapidr/container.yaml"
updated_at: "2023-10-10 02:42:22.770583"
latest: "0.1.1--r43h3121a25_9"
container_url: "https://biocontainers.pro/tools/r-rapidr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.1--r41h3121a25_7"
 - "0.1.1--r42h3121a25_8"
 - "0.1.1--r43h3121a25_9"
description: "shpc-registry automated BioContainers addition for r-rapidr"
config: {"url": "https://biocontainers.pro/tools/r-rapidr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rapidr", "latest": {"0.1.1--r43h3121a25_9": "sha256:d5913af83bb8130239b71cf0f276cad8d112587f763643ceee513f487230fe71"}, "tags": {"0.1.1--r41h3121a25_7": "sha256:fa874f319efedb270427fae1188208601ecd5730d5ba7ecf9336b587336a6a7b", "0.1.1--r42h3121a25_8": "sha256:15a6fd6c7bfcf3d1f7b908880962c5be8212bd94a21a14591e02494f18e6af6c", "0.1.1--r43h3121a25_9": "sha256:d5913af83bb8130239b71cf0f276cad8d112587f763643ceee513f487230fe71"}, "docker": "quay.io/biocontainers/r-rapidr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rapidr.
shpc-registry automated BioContainers addition for r-rapidr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rapidr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rapidr:0.1.1--r43h3121a25_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rapidr/0.1.1--r43h3121a25_9
$ module help quay.io/biocontainers/r-rapidr/0.1.1--r43h3121a25_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rapidr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rapidr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rapidr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rapidr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rapidr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rapidr-inspect-deffile:

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