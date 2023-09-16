---
layout: container
name:  "quay.io/biocontainers/bioconductor-tissuetreg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tissuetreg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tissuetreg/container.yaml"
updated_at: "2023-09-16 02:52:47.305819"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tissuetreg"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tissuetreg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tissuetreg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tissuetreg", "latest": {"1.20.0--r43hdfd78af_0": "sha256:deebf71f6940e7096bd1e34da0518fd7442ee3ccc320d90609dc3fc57000ded2"}, "tags": {"1.9.0--r40_0": "sha256:081fa4ca20a6b746ec4c5ec7d0af5769aa814d6be35746496b92f44f7a3f26e6", "1.17.0--r42hdfd78af_0": "sha256:558dfcefc46517011e098a50fdb7bfd119d2b8f69f0ea96b58a0b005381f0ff7", "1.14.0--r41hdfd78af_1": "sha256:409fed527f027002341f24598e3c379918bd359ef9c447aa32492a22aaa0e238", "1.12.0--r41hdfd78af_0": "sha256:a0ce459e07845349dcb14715215359a6cd7a7b9a532283245f50e8cb988c902f", "1.10.0--r40hdfd78af_1": "sha256:38168225d09d458780a1c8bfe3d63cca6969d58d6d722d47a575ebc979daf247", "1.20.0--r43hdfd78af_0": "sha256:deebf71f6940e7096bd1e34da0518fd7442ee3ccc320d90609dc3fc57000ded2"}, "docker": "quay.io/biocontainers/bioconductor-tissuetreg", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tissuetreg.
shpc-registry automated BioContainers addition for bioconductor-tissuetreg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tissuetreg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tissuetreg:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tissuetreg/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tissuetreg/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tissuetreg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tissuetreg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tissuetreg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tissuetreg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tissuetreg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tissuetreg-inspect-deffile:

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