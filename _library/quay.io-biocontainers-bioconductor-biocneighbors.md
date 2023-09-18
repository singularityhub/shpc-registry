---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocneighbors"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocneighbors/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocneighbors/container.yaml"
updated_at: "2023-09-18 03:10:14.689111"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocneighbors"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.2--r40h399db7b_0"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.0--r41hc247a5b_2"
 - "1.10.0--r41h399db7b_0"
 - "1.16.0--r42hf17093f_1"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocneighbors"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocneighbors", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocneighbors", "latest": {"1.18.0--r43hf17093f_0": "sha256:21f35722cbe9c6e85cf91057fd6399025ebeaa08bfa2bb0e80faa4ee2e71f3c8"}, "tags": {"1.8.2--r40h399db7b_0": "sha256:d3e81972b2b3d74b4c292e52d535bd08a40a48f61eb3ff64391ec50d79a6a265", "1.16.0--r42hc247a5b_0": "sha256:4583e2dec513d165cc21f2ff476096305c9e8dbee77dc51ce3bebcabe5ad71c0", "1.12.0--r41hc247a5b_2": "sha256:ffca3b986cb9704d45360f7ed7bfc021fe7618cf1b92096493aacac912768830", "1.10.0--r41h399db7b_0": "sha256:3c07064dfb14c9cb8160b003c4e25548bfe93e75e54d75719513b9785d81fd98", "1.16.0--r42hf17093f_1": "sha256:8c59b8837d29b742fbeb2331294cd4f25d6b1296e79927d3424e28ebb1af488c", "1.18.0--r43hf17093f_0": "sha256:21f35722cbe9c6e85cf91057fd6399025ebeaa08bfa2bb0e80faa4ee2e71f3c8"}, "docker": "quay.io/biocontainers/bioconductor-biocneighbors", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocneighbors.
shpc-registry automated BioContainers addition for bioconductor-biocneighbors
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocneighbors
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocneighbors:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocneighbors/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-biocneighbors/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocneighbors-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocneighbors-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocneighbors-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocneighbors-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocneighbors-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocneighbors-inspect-deffile:

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