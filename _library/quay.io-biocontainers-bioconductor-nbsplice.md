---
layout: container
name:  "quay.io/biocontainers/bioconductor-nbsplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nbsplice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nbsplice/container.yaml"
updated_at: "2024-06-17 02:54:30.744190"
latest: "1.15.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nbsplice"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nbsplice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nbsplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nbsplice", "latest": {"1.15.0--r42hdfd78af_0": "sha256:e2e5a6c75a6d4cf6910368cd55eeaf0d7c8b7d92d0774adf3ea51733fead1fc8"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:c1c61c4ab750fd05e09594fee380c71121bca76b224b50c411cc1021d5dc22bb", "1.15.0--r42hdfd78af_0": "sha256:e2e5a6c75a6d4cf6910368cd55eeaf0d7c8b7d92d0774adf3ea51733fead1fc8", "1.12.0--r41hdfd78af_0": "sha256:e83f62cbc6063deb37765156eb0321a34d4f8874b70e6bafba3b68bebbbdeebc", "1.10.0--r41hdfd78af_0": "sha256:ecf7258957a62776620856a45fa09c01ae3a8c8c69ffd5676b83b5525d1fb10e"}, "docker": "quay.io/biocontainers/bioconductor-nbsplice", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nbsplice.
shpc-registry automated BioContainers addition for bioconductor-nbsplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nbsplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nbsplice:1.15.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nbsplice/1.15.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nbsplice/1.15.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nbsplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nbsplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nbsplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nbsplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nbsplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nbsplice-inspect-deffile:

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