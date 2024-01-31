---
layout: container
name:  "quay.io/biocontainers/r-isogene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-isogene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-isogene/container.yaml"
updated_at: "2024-01-31 02:42:07.495978"
latest: "1.0_24--r43h3342da4_7"
container_url: "https://biocontainers.pro/tools/r-isogene"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0_24--r41h3342da4_5"
 - "1.0_24--r42h3342da4_6"
 - "1.0_24--r43h3342da4_7"
description: "shpc-registry automated BioContainers addition for r-isogene"
config: {"url": "https://biocontainers.pro/tools/r-isogene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-isogene", "latest": {"1.0_24--r43h3342da4_7": "sha256:15b771775fcafa509c855516ced761ad4229542aabe10d19aeed0c3304ef028e"}, "tags": {"1.0_24--r41h3342da4_5": "sha256:1ed6ea6b917ccca7ac38a8f095bf8db9b441c9b19c1802c99c7248adb44c2a68", "1.0_24--r42h3342da4_6": "sha256:a525b99984c1b83904c9870c7e8b3efd509a123c30aebc04b85e3e14cb468da5", "1.0_24--r43h3342da4_7": "sha256:15b771775fcafa509c855516ced761ad4229542aabe10d19aeed0c3304ef028e"}, "docker": "quay.io/biocontainers/r-isogene", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-isogene.
shpc-registry automated BioContainers addition for r-isogene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-isogene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-isogene:1.0_24--r43h3342da4_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-isogene/1.0_24--r43h3342da4_7
$ module help quay.io/biocontainers/r-isogene/1.0_24--r43h3342da4_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-isogene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-isogene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-isogene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-isogene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-isogene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-isogene-inspect-deffile:

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