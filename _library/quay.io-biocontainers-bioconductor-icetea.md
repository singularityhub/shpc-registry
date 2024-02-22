---
layout: container
name:  "quay.io/biocontainers/bioconductor-icetea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-icetea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-icetea/container.yaml"
updated_at: "2024-02-22 02:45:01.928352"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-icetea"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.1--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-icetea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-icetea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-icetea", "latest": {"1.20.0--r43hdfd78af_0": "sha256:da19485e8fb40a69c309f325bd5abf217f05c562ba83e5bf1cdf5dd617bd942d"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:7f4b6438cf9eeab3b2d8ea63668d5789700f19ffb270ab4f129794a7dcd66c41", "1.16.0--r42hdfd78af_0": "sha256:1e6692a6dcd24903cfdb6f09f95792e9f254cf993842f55dddd715cf45a1160e", "1.12.0--r41hdfd78af_0": "sha256:1515c28f3b59393aec4dd0043482376ddc4e6962479ba4054fa5c3cc5840948b", "1.10.0--r41hdfd78af_0": "sha256:b91b763ebe657b5eab84346115eb4043e47c55b56b68a1922a4f7def0c6d17cd", "1.18.1--r43hdfd78af_0": "sha256:d8d2fddd60e36c01a0c506ac38556f00ae005f1bd15c0952cf02b5768c2fc6ae", "1.20.0--r43hdfd78af_0": "sha256:da19485e8fb40a69c309f325bd5abf217f05c562ba83e5bf1cdf5dd617bd942d"}, "docker": "quay.io/biocontainers/bioconductor-icetea", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-icetea.
shpc-registry automated BioContainers addition for bioconductor-icetea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-icetea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-icetea:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-icetea/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-icetea/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-icetea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icetea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icetea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-icetea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-icetea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-icetea-inspect-deffile:

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