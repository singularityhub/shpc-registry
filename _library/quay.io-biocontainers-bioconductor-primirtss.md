---
layout: container
name:  "quay.io/biocontainers/bioconductor-primirtss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-primirtss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-primirtss/container.yaml"
updated_at: "2025-08-18 03:42:04.292321"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-primirtss"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-primirtss"
config: {"url": "https://biocontainers.pro/tools/bioconductor-primirtss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-primirtss", "latest": {"1.24.0--r44hdfd78af_0": "sha256:f9e38d520afa74116e7c0f3d06568134a4f55ec32c5628d4c167e82a386a4428"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:0e59aaa20e8d7f16e781aa8930fb8e81684da30abef594ec2415381b8a4a0418", "1.16.0--r42hdfd78af_0": "sha256:946fa41dde9461d3d1bea261081a89485e2f97e3787700e9f30a99350240511a", "1.12.0--r41hdfd78af_0": "sha256:5ed164129ce09d50411cf57f2697e9861db27e6ea3eaf5676f18e272a64847cc", "1.10.0--r41hdfd78af_0": "sha256:e219d8d3e1601ab54369b49274baaa5e7d9d0523149701bc90eea99b3cfb4eae", "1.18.0--r43hdfd78af_0": "sha256:cb2a5ddef87895ee0c331a7f2dde942861cd6dfa19005f6339f5e5f92c5bf6d4", "1.20.0--r43hdfd78af_0": "sha256:67a74b90b71ea792f7b823975a2da601205676633c851c0aff0784e228e07b60", "1.24.0--r44hdfd78af_0": "sha256:f9e38d520afa74116e7c0f3d06568134a4f55ec32c5628d4c167e82a386a4428"}, "docker": "quay.io/biocontainers/bioconductor-primirtss", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-primirtss.
shpc-registry automated BioContainers addition for bioconductor-primirtss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-primirtss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-primirtss:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-primirtss/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-primirtss/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-primirtss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primirtss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primirtss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-primirtss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-primirtss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-primirtss-inspect-deffile:

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