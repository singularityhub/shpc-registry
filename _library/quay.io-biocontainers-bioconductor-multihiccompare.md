---
layout: container
name:  "quay.io/biocontainers/bioconductor-multihiccompare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multihiccompare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multihiccompare/container.yaml"
updated_at: "2024-05-28 03:17:43.806246"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multihiccompare"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.1--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multihiccompare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multihiccompare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multihiccompare", "latest": {"1.20.0--r43hdfd78af_0": "sha256:4087264e39d61696de04ebd17f2774c2112b73a4b23b1e9503765cf797b4e4c4"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:18677d0a6343e180b478f6fc19aaea1ae25be8976ba47d4a4bfced1c9bd3d8c0", "1.16.0--r42hdfd78af_0": "sha256:533fb5f6caf64baadccd2ca9007be700fc0e6b831f07d59de97a0a9265d12a28", "1.12.0--r41hdfd78af_0": "sha256:1b3b80c902d749f73ef78de012dbef45e133ec1a6566c48565e2877f41330a74", "1.10.0--r41hdfd78af_0": "sha256:61bfbd877216a24335d8d0904dc296bf7cd25cf7907fd331a87c0f2643edaa56", "1.18.1--r43hdfd78af_0": "sha256:f5a0d2936b2ca50d08f242b977bbbcb77eac677c9d6fae7a81db5f08e2ad1324", "1.20.0--r43hdfd78af_0": "sha256:4087264e39d61696de04ebd17f2774c2112b73a4b23b1e9503765cf797b4e4c4"}, "docker": "quay.io/biocontainers/bioconductor-multihiccompare", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multihiccompare.
shpc-registry automated BioContainers addition for bioconductor-multihiccompare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multihiccompare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multihiccompare:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multihiccompare/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multihiccompare/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multihiccompare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multihiccompare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multihiccompare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multihiccompare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multihiccompare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multihiccompare-inspect-deffile:

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