---
layout: container
name:  "quay.io/biocontainers/r-empiricalfdr.deseq2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-empiricalfdr.deseq2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-empiricalfdr.deseq2/container.yaml"
updated_at: "2022-11-03 01:06:38.857636"
latest: "1.0.3--r41h3121a25_8"
container_url: "https://biocontainers.pro/tools/r-empiricalfdr.deseq2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.3--r41h3121a25_8"
description: "shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2"
config: {"url": "https://biocontainers.pro/tools/r-empiricalfdr.deseq2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2", "latest": {"1.0.3--r41h3121a25_8": "sha256:fceeedc1f2d94f63e5f1a9a12a03ed0ca5c3e3875c25060716b8d2b61dd9fadc"}, "tags": {"1.0.3--r41h3121a25_8": "sha256:fceeedc1f2d94f63e5f1a9a12a03ed0ca5c3e3875c25060716b8d2b61dd9fadc"}, "docker": "quay.io/biocontainers/r-empiricalfdr.deseq2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-empiricalfdr.deseq2.
shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-empiricalfdr.deseq2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-empiricalfdr.deseq2:1.0.3--r41h3121a25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-empiricalfdr.deseq2/1.0.3--r41h3121a25_8
$ module help quay.io/biocontainers/r-empiricalfdr.deseq2/1.0.3--r41h3121a25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-empiricalfdr.deseq2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-empiricalfdr.deseq2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-empiricalfdr.deseq2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-empiricalfdr.deseq2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-empiricalfdr.deseq2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-empiricalfdr.deseq2-inspect-deffile:

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