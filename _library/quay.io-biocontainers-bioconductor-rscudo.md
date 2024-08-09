---
layout: container
name:  "quay.io/biocontainers/bioconductor-rscudo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rscudo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rscudo/container.yaml"
updated_at: "2024-08-09 02:55:24.909478"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rscudo"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rscudo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rscudo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rscudo", "latest": {"1.18.0--r43hdfd78af_0": "sha256:3d1429a723cc1f733bd27ccf67120649bfc02e2d5536501ba11e56a24b0b65fc"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:2d45e50a4e99b4be80e0cc82f82a5c62ae5424c1c55c0ffd756b953a12fc218f", "1.14.0--r42hdfd78af_0": "sha256:2efc202bd1ccfb81f1be1c874b869371d7c2ae087575e3df6e68f052a384a6b5", "1.10.0--r41hdfd78af_0": "sha256:858e303aabe8e5cc9d774b083a1c9cadb8b549b2ed367c657dbe2f85eda54167", "1.16.0--r43hdfd78af_0": "sha256:89655486b0a361790979655b8994f815480ee581b0b448bcb3a021c13eb226ad", "1.18.0--r43hdfd78af_0": "sha256:3d1429a723cc1f733bd27ccf67120649bfc02e2d5536501ba11e56a24b0b65fc"}, "docker": "quay.io/biocontainers/bioconductor-rscudo", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rscudo.
shpc-registry automated BioContainers addition for bioconductor-rscudo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rscudo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rscudo:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rscudo/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rscudo/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rscudo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rscudo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rscudo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rscudo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rscudo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rscudo-inspect-deffile:

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