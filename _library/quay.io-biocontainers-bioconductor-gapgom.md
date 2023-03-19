---
layout: container
name:  "quay.io/biocontainers/bioconductor-gapgom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gapgom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gapgom/container.yaml"
updated_at: "2023-03-19 14:09:44.443339"
latest: "1.10.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gapgom"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gapgom"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gapgom", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gapgom", "latest": {"1.10.0--r41hdfd78af_0": "sha256:56c6d33a3ac5ede9328b3ca8ea6d7e9fbea72ebc04e53365d212b41f92b073d8"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:bda891c0ca33afe92f3176702cff09df7d014da054cc6a040443e3bc6e9ea463", "1.10.0--r41hdfd78af_0": "sha256:56c6d33a3ac5ede9328b3ca8ea6d7e9fbea72ebc04e53365d212b41f92b073d8"}, "docker": "quay.io/biocontainers/bioconductor-gapgom", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gapgom.
shpc-registry automated BioContainers addition for bioconductor-gapgom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gapgom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gapgom:1.10.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gapgom/1.10.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gapgom/1.10.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gapgom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gapgom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gapgom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gapgom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gapgom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gapgom-inspect-deffile:

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