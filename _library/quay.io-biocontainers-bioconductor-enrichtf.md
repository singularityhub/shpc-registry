---
layout: container
name:  "quay.io/biocontainers/bioconductor-enrichtf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enrichtf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enrichtf/container.yaml"
updated_at: "2025-05-08 05:21:15.423254"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enrichtf"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enrichtf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enrichtf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enrichtf", "latest": {"1.18.0--r43hdfd78af_0": "sha256:e6e65b21e12f4a151f6df05e7b60016161bda8aff72fd889917e8865772b2b0a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e5f7c9840a9d1bfea2f08052ecce917bf7e2ad33f0c505eddbaeb41f18121353", "1.14.0--r42hdfd78af_0": "sha256:8f683c57ddbe8ae4b304c4e587cc7b83a689fb0eb65d6249c1c7b15bab75b8a5", "1.10.0--r41hdfd78af_0": "sha256:b1bf232c52d04efe0ab5fe841e0539152c2132011d6708f3e2c2c0f90d968974", "1.16.0--r43hdfd78af_0": "sha256:b87c1fb8241b2c70c0e8ae95d4be76db695250f847ecb939154afd7f5134273e", "1.18.0--r43hdfd78af_0": "sha256:e6e65b21e12f4a151f6df05e7b60016161bda8aff72fd889917e8865772b2b0a"}, "docker": "quay.io/biocontainers/bioconductor-enrichtf", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enrichtf.
shpc-registry automated BioContainers addition for bioconductor-enrichtf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichtf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichtf:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enrichtf/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-enrichtf/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enrichtf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichtf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichtf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enrichtf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enrichtf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enrichtf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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