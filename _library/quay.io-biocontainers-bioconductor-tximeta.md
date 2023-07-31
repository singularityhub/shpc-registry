---
layout: container
name:  "quay.io/biocontainers/bioconductor-tximeta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tximeta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tximeta/container.yaml"
updated_at: "2023-07-31 03:27:46.291117"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tximeta"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.4--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tximeta"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tximeta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tximeta", "latest": {"1.16.0--r42hdfd78af_0": "sha256:cf4638831755ec9f847dc454394cd37226914c09c7cafcc404d1e2163afe751b"}, "tags": {"1.8.4--r40hdfd78af_0": "sha256:84285e575ff948971eea7975a7495a1495f7217666ef615854d3dfaa2f5028f0", "1.16.0--r42hdfd78af_0": "sha256:cf4638831755ec9f847dc454394cd37226914c09c7cafcc404d1e2163afe751b", "1.14.0--r41hdfd78af_0": "sha256:e6985222319ca1d3076c2a966a6d154404441c3f74977a5b1da8ad0efc131be6", "1.12.0--r41hdfd78af_0": "sha256:75a91f805e30083d1ffe30ba220e6c02d9e1034c622caed785a56fec0dccb9b0", "1.10.0--r41hdfd78af_0": "sha256:2b0060c6ef28e4970aaba5c3fb6e573807849846550dbde5621669230ebaaa62"}, "docker": "quay.io/biocontainers/bioconductor-tximeta", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tximeta.
shpc-registry automated BioContainers addition for bioconductor-tximeta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tximeta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tximeta:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tximeta/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tximeta/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tximeta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximeta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximeta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tximeta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tximeta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tximeta-inspect-deffile:

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