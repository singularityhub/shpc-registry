---
layout: container
name:  "quay.io/biocontainers/bioconductor-hicdatahumanimr90"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hicdatahumanimr90/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hicdatahumanimr90/container.yaml"
updated_at: "2022-11-18 00:48:39.701555"
latest: "1.17.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hicdatahumanimr90"
aliases:
 - ".bioconductor-hicdatahumanimr90-post-link.sh"
 - ".bioconductor-hicdatahumanimr90-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hicdatahumanimr90"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hicdatahumanimr90", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hicdatahumanimr90", "latest": {"1.17.0--r42hdfd78af_0": "sha256:ec4153cf40374eb8c01891802b384ad9f8a8834432a3b1704e21053d42e43955"}, "tags": {"1.9.0--r40_0": "sha256:4b9ffd74d0632411440597d5af1ac298cf68d69442a08681374a58fe6250df8d", "1.17.0--r42hdfd78af_0": "sha256:ec4153cf40374eb8c01891802b384ad9f8a8834432a3b1704e21053d42e43955", "1.14.0--r41hdfd78af_1": "sha256:eb21ee867869c04dd932e8e07d92e9979302867cdfee7385b67d03f3f1001ef1", "1.12.0--r41hdfd78af_0": "sha256:cfde7095cb659894509ffcc139c896d3a437b4b77dcbdec23b4205abb3f15e5f", "1.10.0--r40hdfd78af_1": "sha256:79680d1bb7e7e3c562a300d76fd276a053024cd53e3d6224f241a15861e5a008"}, "docker": "quay.io/biocontainers/bioconductor-hicdatahumanimr90", "aliases": {".bioconductor-hicdatahumanimr90-post-link.sh": "/usr/local/bin/.bioconductor-hicdatahumanimr90-post-link.sh", ".bioconductor-hicdatahumanimr90-pre-unlink.sh": "/usr/local/bin/.bioconductor-hicdatahumanimr90-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hicdatahumanimr90.
shpc-registry automated BioContainers addition for bioconductor-hicdatahumanimr90
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hicdatahumanimr90
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hicdatahumanimr90:1.17.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hicdatahumanimr90/1.17.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hicdatahumanimr90/1.17.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hicdatahumanimr90-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicdatahumanimr90-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicdatahumanimr90-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hicdatahumanimr90-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hicdatahumanimr90-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hicdatahumanimr90-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-hicdatahumanimr90-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-hicdatahumanimr90-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-hicdatahumanimr90-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-hicdatahumanimr90-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-hicdatahumanimr90-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-hicdatahumanimr90-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-hicdatahumanimr90-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-hicdatahumanimr90-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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