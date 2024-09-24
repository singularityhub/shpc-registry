---
layout: container
name:  "quay.io/biocontainers/bioconductor-cordon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cordon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cordon/container.yaml"
updated_at: "2024-09-24 03:18:25.179385"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cordon"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cordon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cordon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cordon", "latest": {"1.20.0--r43hdfd78af_0": "sha256:7713b64d38678f5dc27a7f6178fb9866516f2234d9d1cd35e4287329113bdaae"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:d9b6f118dda0d5c9d67528e7083092313384d6b4e198434fce507c470fd4c9ce", "1.16.0--r42hdfd78af_0": "sha256:8d1eed886f26a06acffb9c7fe8d4f7661b2f43e4d30e8b922ea7edaacaf2954a", "1.12.0--r41hdfd78af_0": "sha256:def3bf2ad0b724a92a5644c39f735983ef2d5e453d5d1a2254b4c64a6ed8b78a", "1.10.0--r41hdfd78af_0": "sha256:5b3c7e9d79f9183f6d933d173b9589f991d93a14ffeb5cefc5431c15d8662cb5", "1.18.0--r43hdfd78af_0": "sha256:4155ea70a42d79e30082b50a44eebaa7f815f6b87f457b90a6b9e29f663fd27e", "1.20.0--r43hdfd78af_0": "sha256:7713b64d38678f5dc27a7f6178fb9866516f2234d9d1cd35e4287329113bdaae"}, "docker": "quay.io/biocontainers/bioconductor-cordon", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cordon.
shpc-registry automated BioContainers addition for bioconductor-cordon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cordon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cordon:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cordon/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cordon/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cordon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cordon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cordon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cordon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cordon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cordon-inspect-deffile:

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