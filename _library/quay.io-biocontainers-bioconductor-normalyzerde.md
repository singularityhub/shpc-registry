---
layout: container
name:  "quay.io/biocontainers/bioconductor-normalyzerde"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-normalyzerde/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-normalyzerde/container.yaml"
updated_at: "2023-02-23 03:16:15.850933"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-normalyzerde"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-normalyzerde"
config: {"url": "https://biocontainers.pro/tools/bioconductor-normalyzerde", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-normalyzerde", "latest": {"1.16.0--r42hdfd78af_0": "sha256:ecf06def94ba4bfddd63310354b5b7e9cf2e39ecbdbe8051a97f034d974c711b"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:90686d98fa3cff795f8b781bf7090468f883aee5dcc796f0d8a955224bf8653a", "1.12.0--r41hdfd78af_0": "sha256:eecd6e09323b90456133fe14d35ae228e45ec61397c4af7dc79d0cb1261b9e9e", "1.10.0--r41hdfd78af_0": "sha256:64a1ce5e5d9bf288157ac7a971aac8d9f30859a0f807143db5a7b4b53a1ba5cd", "1.16.0--r42hdfd78af_0": "sha256:ecf06def94ba4bfddd63310354b5b7e9cf2e39ecbdbe8051a97f034d974c711b"}, "docker": "quay.io/biocontainers/bioconductor-normalyzerde", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-normalyzerde.
shpc-registry automated BioContainers addition for bioconductor-normalyzerde
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-normalyzerde
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-normalyzerde:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-normalyzerde/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-normalyzerde/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-normalyzerde-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normalyzerde-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normalyzerde-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-normalyzerde-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-normalyzerde-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-normalyzerde-inspect-deffile:

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