---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylcc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylcc/container.yaml"
updated_at: "2025-03-23 03:21:17.041486"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylcc"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylcc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylcc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylcc", "latest": {"1.20.0--r44hdfd78af_0": "sha256:f48cdd9de1674652368be2b459d5fed6bb0a86876a87a8623a462df0340b2405"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:d789fbdb9a6bc8e20b5c0b3ff0a20c8f5d24589f6822c4b5958cff847235766c", "1.12.0--r42hdfd78af_0": "sha256:790560142e4453ece024a018e98b61d623f9f063c2d5d237ae6e1bd4bae48e63", "1.14.0--r43hdfd78af_0": "sha256:52690fd749889ce1408a9f0ee863d80aefc01550721954effd04960dc374725f", "1.16.0--r43hdfd78af_0": "sha256:a3a128f9a626dd7af5be36385bc449952d5a24f22888a1888671dace501180ae", "1.20.0--r44hdfd78af_0": "sha256:f48cdd9de1674652368be2b459d5fed6bb0a86876a87a8623a462df0340b2405"}, "docker": "quay.io/biocontainers/bioconductor-methylcc", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylcc.
shpc-registry automated BioContainers addition for bioconductor-methylcc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylcc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylcc:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylcc/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylcc/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylcc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylcc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylcc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylcc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylcc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylcc-inspect-deffile:

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