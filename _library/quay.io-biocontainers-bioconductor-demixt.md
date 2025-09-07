---
layout: container
name:  "quay.io/biocontainers/bioconductor-demixt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-demixt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-demixt/container.yaml"
updated_at: "2025-09-07 03:10:49.612352"
latest: "1.22.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-demixt"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.16.0--r43hf17093f_1"
 - "1.22.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-demixt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-demixt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-demixt", "latest": {"1.22.0--r44he5774e6_0": "sha256:d72c3d4f41376d698accc94b48a80a8b6e0f31f6a25b89b6a2c42e80010af5f4"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:7053c195625e35fb9271587a830bf6512827379f85641d5dc6ae3d531940a0b2", "1.14.0--r42hc247a5b_0": "sha256:0a1a2b9e8d6d34bd0e23cd7887c7820801f307b2e7190554fd1c02b54935c4ab", "1.10.0--r41hc247a5b_2": "sha256:6075a01d0574669ba1f386992d7a844ac4a6788e119369188f32b6d95192ed3d", "1.14.0--r42hf17093f_1": "sha256:49ec6fb1c0ae672835cec56296765f0160c10977ddd413b37cd61308bf574519", "1.16.0--r43hf17093f_0": "sha256:3aec6e47099352c49a4a54ac2d80df58774569301ba988153d874c012127f9f3", "1.16.0--r43hf17093f_1": "sha256:cd0604fae3dd9e6d9f16b65eaa05e60091b8d40b59daf093d0b21881058b92a5", "1.22.0--r44he5774e6_0": "sha256:d72c3d4f41376d698accc94b48a80a8b6e0f31f6a25b89b6a2c42e80010af5f4"}, "docker": "quay.io/biocontainers/bioconductor-demixt", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-demixt.
shpc-registry automated BioContainers addition for bioconductor-demixt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-demixt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-demixt:1.22.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-demixt/1.22.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-demixt/1.22.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-demixt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demixt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demixt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-demixt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-demixt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-demixt-inspect-deffile:

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