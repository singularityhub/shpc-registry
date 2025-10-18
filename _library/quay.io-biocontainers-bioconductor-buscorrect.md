---
layout: container
name:  "quay.io/biocontainers/bioconductor-buscorrect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-buscorrect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-buscorrect/container.yaml"
updated_at: "2025-10-18 03:33:56.078829"
latest: "1.24.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-buscorrect"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hd029910_1"
 - "1.16.0--r42hc0cfd56_0"
 - "1.12.0--r41hc0cfd56_2"
 - "1.10.0--r41hd029910_0"
 - "1.16.0--r42ha9d7317_1"
 - "1.18.0--r43ha9d7317_0"
 - "1.20.0--r43ha9d7317_0"
 - "1.20.0--r43ha9d7317_1"
 - "1.24.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-buscorrect"
config: {"url": "https://biocontainers.pro/tools/bioconductor-buscorrect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-buscorrect", "latest": {"1.24.0--r44h3df3fcb_0": "sha256:74188ab61ca703ce93609c9b60ec1f5ac8f5c8a68b61da871b778c281aea00bf"}, "tags": {"1.8.0--r40hd029910_1": "sha256:a37dec7d691c3678797d7e44698507c158e3afef82ccd02e62f65a63115cbf38", "1.16.0--r42hc0cfd56_0": "sha256:9d1066a8070a70235ee591ffa6a3fcf2599322bd046067e542f8bce23d45c6b8", "1.12.0--r41hc0cfd56_2": "sha256:2b7133817bc614b6174a62e612f2f50240bcd5d73079bc00820084c36d62448c", "1.10.0--r41hd029910_0": "sha256:be154f75842a6f5a53fbeaf6ab2d66deb9d878f67c6565a81987f6342910890f", "1.16.0--r42ha9d7317_1": "sha256:173d0525fa0da9896b0090dae60a649f881471f3debc6ef73866749117ab7051", "1.18.0--r43ha9d7317_0": "sha256:189d85fc8798966b77589796c4165712053de31c76d2419be85e41a66141909a", "1.20.0--r43ha9d7317_0": "sha256:20d845faba8c16969b02669555463bd4aa27e111dd1cac01572e5d7f65948bfb", "1.20.0--r43ha9d7317_1": "sha256:ee4a3f353646a7655d04f22040f9f814c1dfc57faaa96c6cce756e9b9a51b834", "1.24.0--r44h3df3fcb_0": "sha256:74188ab61ca703ce93609c9b60ec1f5ac8f5c8a68b61da871b778c281aea00bf"}, "docker": "quay.io/biocontainers/bioconductor-buscorrect", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-buscorrect.
shpc-registry automated BioContainers addition for bioconductor-buscorrect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-buscorrect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-buscorrect:1.24.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-buscorrect/1.24.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-buscorrect/1.24.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-buscorrect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-buscorrect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-buscorrect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-buscorrect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-buscorrect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-buscorrect-inspect-deffile:

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