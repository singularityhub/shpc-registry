---
layout: container
name:  "quay.io/biocontainers/bioconductor-fastqcleaner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fastqcleaner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fastqcleaner/container.yaml"
updated_at: "2025-09-25 07:26:08.373172"
latest: "1.24.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fastqcleaner"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_1"
 - "1.12.0--r41hc247a5b_2"
 - "1.10.0--r41h399db7b_0"
 - "1.16.0--r42hc247a5b_0"
 - "1.16.0--r42hf17093f_1"
 - "1.18.0--r43hf17093f_0"
 - "1.20.0--r43hf17093f_0"
 - "1.20.0--r43hf17093f_1"
 - "1.24.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fastqcleaner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fastqcleaner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fastqcleaner", "latest": {"1.24.0--r44he5774e6_0": "sha256:724bc4881c3a925917c9034ed3600ce3174efe649860904d453ff8698bc4e7da"}, "tags": {"1.8.0--r40h399db7b_1": "sha256:2996ffdae5f9c2c339e9c35694a00cbabb9e656f1967c706b922772b740ade4e", "1.12.0--r41hc247a5b_2": "sha256:6f33e10e87101f517e70355bc7d9c27aa8821a520e5a23dda35f4a254dcf6237", "1.10.0--r41h399db7b_0": "sha256:4629f8934985022417b969623a46e0e33bc6ffef6738ed66a349ff82a1287bc1", "1.16.0--r42hc247a5b_0": "sha256:d28f2a26705c5b8466377a7c1f4f3712312988151b18dcc8654f79a5765c4e01", "1.16.0--r42hf17093f_1": "sha256:a75bb4ac318edb4099fb28e18e026d2be03a7c014e0ef1687a9d6912c4456475", "1.18.0--r43hf17093f_0": "sha256:bdec0a5b0e2d2191bf1ed83ed31aaffd0a26400b29a218b4177b748005957300", "1.20.0--r43hf17093f_0": "sha256:0d2caa7fd62329bda98b4275b47d8adeec234daef16923c5d1905d11e94f1396", "1.20.0--r43hf17093f_1": "sha256:d87b0c0870c862e4d61c996c39f13566859a7d1dc5c0e013d59a00f050371ef1", "1.24.0--r44he5774e6_0": "sha256:724bc4881c3a925917c9034ed3600ce3174efe649860904d453ff8698bc4e7da"}, "docker": "quay.io/biocontainers/bioconductor-fastqcleaner", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fastqcleaner.
shpc-registry automated BioContainers addition for bioconductor-fastqcleaner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fastqcleaner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fastqcleaner:1.24.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fastqcleaner/1.24.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-fastqcleaner/1.24.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fastqcleaner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fastqcleaner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fastqcleaner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fastqcleaner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fastqcleaner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fastqcleaner-inspect-deffile:

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