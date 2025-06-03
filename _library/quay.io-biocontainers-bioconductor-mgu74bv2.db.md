---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74bv2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74bv2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74bv2.db/container.yaml"
updated_at: "2025-06-03 03:34:27.138662"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74bv2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74bv2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:ddd78459d7e508cfd4ed2884114722f18370cc9bb79e2a6354e64e8310290828"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:e0089bd7cafaf66a2b39f496392efaeee3b0fbdf34e7f3b60a7b330703a8da8d", "3.13.0--r42hdfd78af_2": "sha256:5faff7564518705128dbffb93f6c08659c04951d1e2912cc2a754af07088e46a", "3.13.0--r43hdfd78af_3": "sha256:157dbbb39d34cc2becfbe2ad2dc6a63fc0865ba9fbbb96624c1b6c6b0c7c7a63", "3.13.0--r43hdfd78af_4": "sha256:79142f6593e99151646ca33d6649eb31664346660d378267436be49785122c73", "3.13.0--r44hdfd78af_5": "sha256:ddd78459d7e508cfd4ed2884114722f18370cc9bb79e2a6354e64e8310290828"}, "docker": "quay.io/biocontainers/bioconductor-mgu74bv2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74bv2.db.
shpc-registry automated BioContainers addition for bioconductor-mgu74bv2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74bv2.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mgu74bv2.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74bv2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74bv2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74bv2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74bv2.db-inspect-deffile:

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