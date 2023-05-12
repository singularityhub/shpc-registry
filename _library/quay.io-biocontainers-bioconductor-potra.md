---
layout: container
name:  "quay.io/biocontainers/bioconductor-potra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-potra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-potra/container.yaml"
updated_at: "2023-05-12 03:01:30.751079"
latest: "1.13.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-potra"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.7.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-potra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-potra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-potra", "latest": {"1.13.0--r42hdfd78af_0": "sha256:4f1bc3e4386e85d73beb5b8a9001a78ea979023a064d70715622cacab4539ff0"}, "tags": {"1.7.0--r41hdfd78af_0": "sha256:646d9a88c2a5920305d2cac63ec44f0f1e3554a30407962edcc29d9deffe6737", "1.10.0--r41hdfd78af_0": "sha256:24a3ab746b236bd4aade3033477fff7034dfcc7d63e14ffa895ac70751c596df", "1.13.0--r42hdfd78af_0": "sha256:4f1bc3e4386e85d73beb5b8a9001a78ea979023a064d70715622cacab4539ff0"}, "docker": "quay.io/biocontainers/bioconductor-potra", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-potra.
shpc-registry automated BioContainers addition for bioconductor-potra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-potra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-potra:1.13.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-potra/1.13.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-potra/1.13.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-potra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-potra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-potra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-potra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-potra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-potra-inspect-deffile:

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