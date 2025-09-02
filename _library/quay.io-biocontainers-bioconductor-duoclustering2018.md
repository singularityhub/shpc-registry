---
layout: container
name:  "quay.io/biocontainers/bioconductor-duoclustering2018"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-duoclustering2018/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-duoclustering2018/container.yaml"
updated_at: "2025-09-02 03:10:43.712984"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-duoclustering2018"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-duoclustering2018"
config: {"url": "https://biocontainers.pro/tools/bioconductor-duoclustering2018", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-duoclustering2018", "latest": {"1.24.0--r44hdfd78af_0": "sha256:b498f766d82b90dbe3ea15972d5ffa30427701692de9783bd2d7d67d7bc168ef"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:83ae9e0b916cac4eeeb10d6e973fff2af28731a387b89bf8642b87e2b389c8b4", "1.16.0--r42hdfd78af_0": "sha256:b5e7257210d46a711dfed4686604324b65f7cd645a3f42c5894e2a4d5b0b690e", "1.12.0--r41hdfd78af_1": "sha256:5ccbfa5a7d8b3db1ede9a9b80f09fa250ac7bf03ab3857fa8017bd7fad6018e1", "1.10.0--r41hdfd78af_0": "sha256:b995d542878b2e3a48363830eadcf78bda52d179536122d1e943074981057a7c", "1.18.0--r43hdfd78af_0": "sha256:8fc783543e3817ee55c43fe5bd51e86249e936b96c964ecf5f7cfa1a84a54f8e", "1.20.0--r43hdfd78af_0": "sha256:485c5f5c68ad900adf0d8ac91985ca72c3987061ca0887ccf47ef61b595c8a42", "1.24.0--r44hdfd78af_0": "sha256:b498f766d82b90dbe3ea15972d5ffa30427701692de9783bd2d7d67d7bc168ef"}, "docker": "quay.io/biocontainers/bioconductor-duoclustering2018", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-duoclustering2018.
shpc-registry automated BioContainers addition for bioconductor-duoclustering2018
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-duoclustering2018
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-duoclustering2018:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-duoclustering2018/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-duoclustering2018/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-duoclustering2018-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-duoclustering2018-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-duoclustering2018-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-duoclustering2018-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-duoclustering2018-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-duoclustering2018-inspect-deffile:

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