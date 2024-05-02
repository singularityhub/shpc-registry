---
layout: container
name:  "quay.io/biocontainers/r-cp4p"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cp4p/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cp4p/container.yaml"
updated_at: "2024-05-02 03:08:58.239026"
latest: "0.3.6--r43h3342da4_6"
container_url: "https://biocontainers.pro/tools/r-cp4p"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.3.6--r41h3342da4_4"
 - "0.3.6--r42h3342da4_5"
 - "0.3.6--r43h3342da4_6"
description: "shpc-registry automated BioContainers addition for r-cp4p"
config: {"url": "https://biocontainers.pro/tools/r-cp4p", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-cp4p", "latest": {"0.3.6--r43h3342da4_6": "sha256:f2ffb07fcf7d01cc9a0cb362ef936660a9be8e0c757c4afa91501ab142c860f0"}, "tags": {"0.3.6--r41h3342da4_4": "sha256:7c93e540b020cd74e4a4d67f2aeae19933137a75252381c305fa122a6f3e4bd0", "0.3.6--r42h3342da4_5": "sha256:18d25b3f9333aaa04e9b42b4a53eb5d9dada6f7b89d222a4756cd83384b58a12", "0.3.6--r43h3342da4_6": "sha256:f2ffb07fcf7d01cc9a0cb362ef936660a9be8e0c757c4afa91501ab142c860f0"}, "docker": "quay.io/biocontainers/r-cp4p", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cp4p.
shpc-registry automated BioContainers addition for r-cp4p
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cp4p
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cp4p:0.3.6--r43h3342da4_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cp4p/0.3.6--r43h3342da4_6
$ module help quay.io/biocontainers/r-cp4p/0.3.6--r43h3342da4_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cp4p-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cp4p-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cp4p-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cp4p-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cp4p-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cp4p-inspect-deffile:

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