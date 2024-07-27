---
layout: container
name:  "quay.io/biocontainers/bioconductor-globalancova"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-globalancova/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-globalancova/container.yaml"
updated_at: "2024-07-27 03:12:05.557649"
latest: "4.20.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-globalancova"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "4.8.0--r40hd029910_1"
 - "4.16.0--r42hc0cfd56_0"
 - "4.12.0--r41hc0cfd56_2"
 - "4.10.0--r41hd029910_0"
 - "4.16.0--r42ha9d7317_1"
 - "4.18.0--r43ha9d7317_0"
 - "4.20.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-globalancova"
config: {"url": "https://biocontainers.pro/tools/bioconductor-globalancova", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-globalancova", "latest": {"4.20.0--r43ha9d7317_0": "sha256:7d1c261aebfe7b5c0b30a1fb3ad2301034a2dc136debb399c7658c436a78769c"}, "tags": {"4.8.0--r40hd029910_1": "sha256:48fa31b9abc9c639ffe18c956bf9cfc4edd3d59502cd6394ba55c5d34ba3439f", "4.16.0--r42hc0cfd56_0": "sha256:e77e6ab8f53f5850c8d7289ffcc2cc474eadd66a15293f0537cf0120214f9702", "4.12.0--r41hc0cfd56_2": "sha256:778cc304a4c36ad072eaf43416d49ed9db07009219130d4f84cbfcb832155a32", "4.10.0--r41hd029910_0": "sha256:1012fd44ec127ec6368902cc4fd45bec8f302c94131cd63d2eccb05ea247e30b", "4.16.0--r42ha9d7317_1": "sha256:304e467341f7dc11b0b1723414f5596f62bc59fd6fcff613e453f0e279f4d219", "4.18.0--r43ha9d7317_0": "sha256:1021a7c6eefde28ec43f329bce4cb12c28271ccec4d2aa7d72df709d0c249627", "4.20.0--r43ha9d7317_0": "sha256:7d1c261aebfe7b5c0b30a1fb3ad2301034a2dc136debb399c7658c436a78769c"}, "docker": "quay.io/biocontainers/bioconductor-globalancova", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-globalancova.
shpc-registry automated BioContainers addition for bioconductor-globalancova
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-globalancova
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-globalancova:4.20.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-globalancova/4.20.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-globalancova/4.20.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-globalancova-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globalancova-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globalancova-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-globalancova-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-globalancova-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-globalancova-inspect-deffile:

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