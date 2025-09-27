---
layout: container
name:  "quay.io/biocontainers/bioconductor-pram"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pram/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pram/container.yaml"
updated_at: "2025-09-27 03:37:38.052603"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pram"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pram"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pram", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pram", "latest": {"1.22.0--r44hdfd78af_0": "sha256:5297f6b4172ce3349683ae09427b20940a4a486553419ce9d9c2521ac8c67a29"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:7e0eb2f63d3927a39488157ce292c984f6aaeae5dbb74115ad0db4e85d9dfb77", "1.10.0--r41hdfd78af_0": "sha256:a1b36aeb6802a6b67ef0b11612a1bafd567ff7dd897d5baf415c7e9d13f36d89", "1.14.0--r42hdfd78af_0": "sha256:919589275a3d6e602fff3fa2bfd0d59c04bd42b18b58a66ee0cab7de6b3f62ff", "1.16.0--r43hdfd78af_0": "sha256:c64a0ad854889c70fce03b1d2680ca1a4a59361b3d430fb7c2e432703699da7d", "1.18.0--r43hdfd78af_0": "sha256:5897bd74885fbd9168856faf2172b0ff9d005c7c20435b52ab27bd76e51b93eb", "1.22.0--r44hdfd78af_0": "sha256:5297f6b4172ce3349683ae09427b20940a4a486553419ce9d9c2521ac8c67a29"}, "docker": "quay.io/biocontainers/bioconductor-pram", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pram.
shpc-registry automated BioContainers addition for bioconductor-pram
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pram
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pram:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pram/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pram/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pram-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pram-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pram-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pram-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pram-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pram-inspect-deffile:

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