---
layout: container
name:  "quay.io/biocontainers/bioconductor-ace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ace/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ace/container.yaml"
updated_at: "2025-05-27 11:21:33.363562"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ace"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ace"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ace", "latest": {"1.24.0--r44hdfd78af_0": "sha256:278e65c0c67b75df998c7fecbd3c63e366f6fc63ced3ad9f80079588b1483dc2"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:37cbec082420e12b938097e5a85c58a9af363eddea19e237a584250e0f40ec6b", "1.16.0--r42hdfd78af_0": "sha256:ca2a4707ead145926f9acf9ae17486ed346328ec1e7c9b769d07cc603f68db27", "1.12.0--r41hdfd78af_0": "sha256:0cad9d2484df7652236e238763cf8bc8192cd3d83f5265aea4dc4a91d8a5543b", "1.10.0--r41hdfd78af_0": "sha256:0a44ed18f2dcba64584c37f02fdc2e587446e3eb988dbd2ac81418cc0e168613", "1.18.0--r43hdfd78af_0": "sha256:e2ed4235619deac7350753f2b53fbeb23d10cff7b8d973f5d63d3c2007c7b170", "1.20.0--r43hdfd78af_0": "sha256:9cc9525fcf7cdd1a9c495410db90bb40cffaf2073a60b8959a73e2d932f337cc", "1.24.0--r44hdfd78af_0": "sha256:278e65c0c67b75df998c7fecbd3c63e366f6fc63ced3ad9f80079588b1483dc2"}, "docker": "quay.io/biocontainers/bioconductor-ace", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ace.
shpc-registry automated BioContainers addition for bioconductor-ace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ace:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ace/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ace/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ace-inspect-deffile:

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