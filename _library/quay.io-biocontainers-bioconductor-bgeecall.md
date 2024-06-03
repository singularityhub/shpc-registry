---
layout: container
name:  "quay.io/biocontainers/bioconductor-bgeecall"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bgeecall/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bgeecall/container.yaml"
updated_at: "2024-06-03 03:00:20.786326"
latest: "1.18.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bgeecall"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bgeecall"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bgeecall", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bgeecall", "latest": {"1.18.1--r43hdfd78af_0": "sha256:c70305dbe1872a35b98d48783bb1279dff82b7ba954c03b2d2ff874be9995929"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:6c9146084e0f9a8463007cd43958a7265e3adb81115eb118f7ac2bddfc630556", "1.14.0--r42hdfd78af_0": "sha256:2cfc72e0afcf63cb0ede877a70f2efab40137dfea4b43f9822cad768b76b8874", "1.10.0--r41hdfd78af_0": "sha256:61b1a5512d39439ba9f4b6928e6b41f6c6651babb729cd6ec1651cb3790983cd", "1.16.0--r43hdfd78af_0": "sha256:9e160e5363fd89add48e852fc57d11cbe4454e81305187136c5127816f79c2b1", "1.18.1--r43hdfd78af_0": "sha256:c70305dbe1872a35b98d48783bb1279dff82b7ba954c03b2d2ff874be9995929"}, "docker": "quay.io/biocontainers/bioconductor-bgeecall", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bgeecall.
shpc-registry automated BioContainers addition for bioconductor-bgeecall
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bgeecall
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bgeecall:1.18.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bgeecall/1.18.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bgeecall/1.18.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bgeecall-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgeecall-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgeecall-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bgeecall-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bgeecall-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bgeecall-inspect-deffile:

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