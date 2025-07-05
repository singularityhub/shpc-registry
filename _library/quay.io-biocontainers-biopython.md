---
layout: container
name:  "quay.io/biocontainers/biopython"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biopython/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biopython/container.yaml"
updated_at: "2025-07-05 03:18:40.149268"
latest: "1.81"
container_url: "https://biocontainers.pro/tools/biopython"

versions:
 - "1.70--np112py36_1"
 - "1.78"
 - "1.76"
 - "1.75"
 - "1.81"
 - "1.79"
description: "shpc-registry automated BioContainers addition for biopython"
config: {"url": "https://biocontainers.pro/tools/biopython", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biopython", "latest": {"1.81": "sha256:10d755c731c82a22d91fc346f338ba47d5fd4f3b357828f5bbc903c9be865614"}, "tags": {"1.70--np112py36_1": "sha256:ebeefa970033653f1b3deb9b428f6ede3a9f628bee7a4a2b1194b2d2e0be1346", "1.78": "sha256:8bdeb52fb15b5f61c40292f73d85a3a77cda4bbd95d29e710ddaad7a6bf76720", "1.76": "sha256:b0204cf662a3d858f6c28627124b83ed6f564e2b156b8788092f2dd9256c9290", "1.75": "sha256:fa2c959d7b17b27dd1d3ca3dcc18ac4002f971d1731d57ddcdbd204afab90dba", "1.81": "sha256:10d755c731c82a22d91fc346f338ba47d5fd4f3b357828f5bbc903c9be865614", "1.79": "sha256:937556be7fd782859ece3138e0b8beae3f4645ae8c8fcf304bd56d06084ae37b"}, "docker": "quay.io/biocontainers/biopython"}
---

This module is a singularity container wrapper for quay.io/biocontainers/biopython.
shpc-registry automated BioContainers addition for biopython
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biopython
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biopython:1.81
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biopython/1.81
$ module help quay.io/biocontainers/biopython/1.81
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biopython-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biopython-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biopython-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biopython-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biopython-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biopython-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### biopython

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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