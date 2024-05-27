---
layout: container
name:  "quay.io/biocontainers/bioconductor-metnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metnet/container.yaml"
updated_at: "2024-05-27 03:29:33.057005"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metnet"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metnet", "latest": {"1.20.0--r43hdfd78af_0": "sha256:12ee5f97a31ecb81429c2c2b3df4fcf67239b63dc53c4979afe3e3a74b2cd4e2"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:90a43429c6dc68809710f4143c22468b466b2f7c2d358ce3745944bfb6ab4682", "1.16.0--r42hdfd78af_0": "sha256:eb9f01336c518e8a4dcafbe416d8a6c460b5cc2cb105e2d7415e828e16bf9ae6", "1.12.0--r41hdfd78af_0": "sha256:c3fff91aabd2ce39209cc11a0dded6149b5e2df2bb2e27378419e227d181f626", "1.18.0--r43hdfd78af_0": "sha256:b3ac5aa1aa4f9023237bdbb0ec72944a59e90fc700e69ea36d0959361817a0f0", "1.20.0--r43hdfd78af_0": "sha256:12ee5f97a31ecb81429c2c2b3df4fcf67239b63dc53c4979afe3e3a74b2cd4e2"}, "docker": "quay.io/biocontainers/bioconductor-metnet", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metnet.
shpc-registry automated BioContainers addition for bioconductor-metnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metnet:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metnet/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metnet/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metnet-inspect-deffile:

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