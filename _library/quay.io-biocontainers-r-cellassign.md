---
layout: container
name:  "quay.io/biocontainers/r-cellassign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cellassign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cellassign/container.yaml"
updated_at: "2024-05-05 02:55:31.504418"
latest: "0.99.2--r43hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-cellassign"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.99.2--r41hdfd78af_4"
 - "0.99.2--r42hdfd78af_5"
 - "0.99.2--r43hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-cellassign"
config: {"url": "https://biocontainers.pro/tools/r-cellassign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-cellassign", "latest": {"0.99.2--r43hdfd78af_6": "sha256:786958527c2fc82d402e3b698ff7bb29d134d4f17f3a91ffea56bd4712cc4e4d"}, "tags": {"0.99.2--r41hdfd78af_4": "sha256:c24eb236dbb89e44d621731bf7f1d375c69304e9e236424dadd2c689cd671507", "0.99.2--r42hdfd78af_5": "sha256:3ddf619a3ac5458eafc04be873061d65287304cb2b4e694e24624f9767a5170c", "0.99.2--r43hdfd78af_6": "sha256:786958527c2fc82d402e3b698ff7bb29d134d4f17f3a91ffea56bd4712cc4e4d"}, "docker": "quay.io/biocontainers/r-cellassign", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cellassign.
shpc-registry automated BioContainers addition for r-cellassign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cellassign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cellassign:0.99.2--r43hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cellassign/0.99.2--r43hdfd78af_6
$ module help quay.io/biocontainers/r-cellassign/0.99.2--r43hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cellassign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cellassign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cellassign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cellassign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cellassign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cellassign-inspect-deffile:

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