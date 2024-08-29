---
layout: container
name:  "quay.io/biocontainers/bioconductor-oveseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oveseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oveseg/container.yaml"
updated_at: "2024-08-29 03:03:50.911949"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oveseg"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oveseg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oveseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oveseg", "latest": {"1.18.0--r43hf17093f_0": "sha256:9f8c3675d275dd4bf299169862ce4995a9c97c9aea9c8cf3f0fc73e3485fdd48"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:28244a27b87310cbbf8eb9d1cd1aa877b156cf8bd3a5e1117ebb5c6ff63cecd0", "1.14.0--r42hc247a5b_0": "sha256:282ae98621862e791422d84fcf3b21ef9cf854b28530d9cefb76621d09f3d7ef", "1.10.0--r41hc247a5b_2": "sha256:fcfabd82cdb553aafff0ab95ea80ac63f8845bfda05d600e180ee601b184089a", "1.14.0--r42hf17093f_1": "sha256:2c0e1fee757399ea1f6a80e7126a8ba287aa68594a6565c1cb8947251d8e7eb6", "1.16.0--r43hf17093f_0": "sha256:ebcb17f4af157006243a7d004a734cfcf9eb735d4ba0ce43bb32c0f081826644", "1.18.0--r43hf17093f_0": "sha256:9f8c3675d275dd4bf299169862ce4995a9c97c9aea9c8cf3f0fc73e3485fdd48"}, "docker": "quay.io/biocontainers/bioconductor-oveseg", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oveseg.
shpc-registry automated BioContainers addition for bioconductor-oveseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oveseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oveseg:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oveseg/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-oveseg/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oveseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oveseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oveseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oveseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oveseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oveseg-inspect-deffile:

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