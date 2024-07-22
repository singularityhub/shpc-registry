---
layout: container
name:  "quay.io/biocontainers/r-jackstraw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-jackstraw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-jackstraw/container.yaml"
updated_at: "2024-07-22 03:47:40.225448"
latest: "1.3.9--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-jackstraw"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.3--r41h3342da4_6"
 - "1.3.8--r42h3342da4_0"
 - "1.3.8--r43h3342da4_1"
 - "1.3.9--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-jackstraw"
config: {"url": "https://biocontainers.pro/tools/r-jackstraw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-jackstraw", "latest": {"1.3.9--r43h3342da4_0": "sha256:3cb4a450786b73f3eb77208f1894a5d8a1a867065b77987da6f2857651aa50c7"}, "tags": {"1.3--r41h3342da4_6": "sha256:aa8bd336170013f82c5d94fe243272b85cc5ba8ddaee7200fa6deaa6f9cd2a54", "1.3.8--r42h3342da4_0": "sha256:8a395e7a2d4be58a5450ff0033e94de1016770d244dff22b99e3cdfae8cc4ee7", "1.3.8--r43h3342da4_1": "sha256:c0e4e52b7b93faed9c2c7e7c07a55b5de2b98b8f93645df1ee3108d5fc1a6493", "1.3.9--r43h3342da4_0": "sha256:3cb4a450786b73f3eb77208f1894a5d8a1a867065b77987da6f2857651aa50c7"}, "docker": "quay.io/biocontainers/r-jackstraw", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-jackstraw.
shpc-registry automated BioContainers addition for r-jackstraw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-jackstraw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-jackstraw:1.3.9--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-jackstraw/1.3.9--r43h3342da4_0
$ module help quay.io/biocontainers/r-jackstraw/1.3.9--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-jackstraw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-jackstraw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-jackstraw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-jackstraw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-jackstraw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-jackstraw-inspect-deffile:

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