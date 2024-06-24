---
layout: container
name:  "quay.io/biocontainers/bioconductor-foldgo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-foldgo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-foldgo/container.yaml"
updated_at: "2024-06-24 03:03:41.462360"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-foldgo"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-foldgo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-foldgo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-foldgo", "latest": {"1.18.0--r43hdfd78af_0": "sha256:5f01490538a8c7e316ae8b66614e60e09942572513654e75753c81460dee6b22"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:9e7166bf7b4886d85667c9c4b7d13e59150bdb42475290b903d1437780f4bbae", "1.16.0--r42hdfd78af_0": "sha256:632b69fd43b880b77e44593c07e5442aed7ad32f295001d7f93ea5f382e463a8", "1.12.0--r41hdfd78af_0": "sha256:37036bd38397f87f38e0fe1241302938adaa97e8070a282ceda67ab0945baddc", "1.10.0--r41hdfd78af_0": "sha256:20717cfbd1faa7dd9fe69a2635a8ce24d03f1e3a7d02c03baa0eca9093167cae", "1.18.0--r43hdfd78af_0": "sha256:5f01490538a8c7e316ae8b66614e60e09942572513654e75753c81460dee6b22"}, "docker": "quay.io/biocontainers/bioconductor-foldgo", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-foldgo.
shpc-registry automated BioContainers addition for bioconductor-foldgo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-foldgo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-foldgo:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-foldgo/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-foldgo/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-foldgo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-foldgo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-foldgo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-foldgo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-foldgo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-foldgo-inspect-deffile:

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