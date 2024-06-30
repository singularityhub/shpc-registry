---
layout: container
name:  "quay.io/biocontainers/bioconductor-beclear"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beclear/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beclear/container.yaml"
updated_at: "2024-06-30 03:23:14.205094"
latest: "2.18.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-beclear"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41h399db7b_0"
 - "2.14.0--r42hc247a5b_0"
 - "2.10.0--r41hc247a5b_2"
 - "2.14.0--r42hf17093f_1"
 - "2.16.0--r43hf17093f_0"
 - "2.18.0--r43hf17093f_0"
 - "2.18.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-beclear"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beclear", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beclear", "latest": {"2.18.0--r43hf17093f_1": "sha256:aac403097e355819942e247970baf6bce49ee0d385757e0e240f027ef23ad347"}, "tags": {"2.8.0--r41h399db7b_0": "sha256:1f935f7433b9cda2a8620fe7252a010a71a995cefb30e79bed1417e1e1bae19e", "2.14.0--r42hc247a5b_0": "sha256:39b11b8e8a1f3c9071a6126311c71333aa55473af0642165c37dcea6ef1ba40d", "2.10.0--r41hc247a5b_2": "sha256:4a377e7169dba2f2bfaff74b4acbfb35e22c71b5ebb44424f69648bbd114a784", "2.14.0--r42hf17093f_1": "sha256:5d828d9412d7ac3462bcbef71f263758e1c771e3a864887acc0a7e08746674ff", "2.16.0--r43hf17093f_0": "sha256:907df7f339afa4a94b0d2d55c7778e4f4bb9c6b70250a24303af414ffeb47e58", "2.18.0--r43hf17093f_0": "sha256:20d1153536d39a7cbc0ea61ffdafa1497583e585da501dd3c5f65910ee6b17ee", "2.18.0--r43hf17093f_1": "sha256:aac403097e355819942e247970baf6bce49ee0d385757e0e240f027ef23ad347"}, "docker": "quay.io/biocontainers/bioconductor-beclear", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beclear.
shpc-registry automated BioContainers addition for bioconductor-beclear
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beclear
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beclear:2.18.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beclear/2.18.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-beclear/2.18.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beclear-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beclear-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beclear-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beclear-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beclear-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beclear-inspect-deffile:

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