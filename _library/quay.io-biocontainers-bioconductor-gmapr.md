---
layout: container
name:  "quay.io/biocontainers/bioconductor-gmapr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gmapr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gmapr/container.yaml"
updated_at: "2025-08-24 03:45:00.222045"
latest: "1.48.0--r44h15a9599_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gmapr"

versions:
 - "1.36.0--r41hc0cfd56_2"
 - "1.40.0--r42hc0cfd56_0"
 - "1.40.0--r42ha9d7317_1"
 - "1.42.0--r43ha9d7317_0"
 - "1.44.0--r43ha9d7317_0"
 - "1.44.0--r43ha9d7317_1"
 - "1.48.0--r44h15a9599_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gmapr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gmapr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gmapr", "latest": {"1.48.0--r44h15a9599_0": "sha256:caa0870019d8ae1d6c5dba766fa7914e1d9fa76f67693544d0da8f44d5894fcb"}, "tags": {"1.36.0--r41hc0cfd56_2": "sha256:5b6fcab399519f0e29b38c316246c4159c1722bd7fad36645e9ede4c6298673d", "1.40.0--r42hc0cfd56_0": "sha256:2cdbf64e47eb9c4080a7a8318e44745a25a49daafeecd04b2872ee52f540d689", "1.40.0--r42ha9d7317_1": "sha256:d1dfea5c0c26727c2569b8a01cebf2a1a050fac1cff72215eb388b4c60a7089d", "1.42.0--r43ha9d7317_0": "sha256:44ad69c2c457523cb05e1c7f0a8bed60c3b8f174fd4ef6bf33e3da032b254625", "1.44.0--r43ha9d7317_0": "sha256:58299e91aa2f79776e2ab698d5d0ebd898bb6a6c4ac561f4d98fe0e9626cd772", "1.44.0--r43ha9d7317_1": "sha256:f6ef195b547e282445191d76369c09cc1daca7a58508e26fffd082a5c9e7c17a", "1.48.0--r44h15a9599_0": "sha256:caa0870019d8ae1d6c5dba766fa7914e1d9fa76f67693544d0da8f44d5894fcb"}, "docker": "quay.io/biocontainers/bioconductor-gmapr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gmapr.
shpc-registry automated BioContainers addition for bioconductor-gmapr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gmapr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gmapr:1.48.0--r44h15a9599_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gmapr/1.48.0--r44h15a9599_0
$ module help quay.io/biocontainers/bioconductor-gmapr/1.48.0--r44h15a9599_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gmapr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmapr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmapr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gmapr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gmapr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gmapr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gmapr

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