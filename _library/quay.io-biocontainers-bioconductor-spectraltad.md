---
layout: container
name:  "quay.io/biocontainers/bioconductor-spectraltad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spectraltad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spectraltad/container.yaml"
updated_at: "2025-01-29 03:13:48.094609"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spectraltad"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spectraltad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spectraltad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spectraltad", "latest": {"1.22.0--r44hdfd78af_0": "sha256:2bbdf5c83252e82ed1003b40dd2d9b181bfc8c1fbecf3669866868c9f87c1d9b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4a906e8185d7249a67d79d13cc82ee7e3cc6f40a902a5d567929133eac5f94da", "1.14.0--r42hdfd78af_0": "sha256:8e009a718ec0876b95e2515eb909319ad5ca081c522570ed05a235225d1e8540", "1.10.0--r41hdfd78af_0": "sha256:d964b718dbb08d0edd628fd5cf87dae2f491f21c9b3b32814bf64bf3aaf2261b", "1.16.0--r43hdfd78af_0": "sha256:e50630c01ae2747c627d78f84ce858cc3c3912d4f3aa7bfb3dcd80b4a8a54889", "1.18.0--r43hdfd78af_0": "sha256:8b72f864f9f3f708b45c069e65fb4492b07b8190822e30425388b9730bbc54a2", "1.22.0--r44hdfd78af_0": "sha256:2bbdf5c83252e82ed1003b40dd2d9b181bfc8c1fbecf3669866868c9f87c1d9b"}, "docker": "quay.io/biocontainers/bioconductor-spectraltad", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spectraltad.
shpc-registry automated BioContainers addition for bioconductor-spectraltad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spectraltad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spectraltad:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spectraltad/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spectraltad/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spectraltad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spectraltad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spectraltad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spectraltad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spectraltad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spectraltad-inspect-deffile:

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