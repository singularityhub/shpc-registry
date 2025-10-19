---
layout: container
name:  "quay.io/biocontainers/bioconductor-cghmcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cghmcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cghmcr/container.yaml"
updated_at: "2025-10-19 04:01:18.980161"
latest: "1.64.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cghmcr"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.64.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cghmcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cghmcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cghmcr", "latest": {"1.64.0--r44hdfd78af_0": "sha256:649cca9d51a8fd9d570ab2b06d4c411c97a607926e6b3ae6085b728497f7fa4e"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:e28e37b1d0bb6a7a0bbbe8bfc535685a20d7dc751952cb9320e8b20dccdd68b7", "1.56.0--r42hdfd78af_0": "sha256:81fd2bcae73db44a8e1128ba2eaf69ed846eaf4d9d0ca5a70af5143d7e6382d2", "1.58.0--r43hdfd78af_0": "sha256:8df6b4045d4e3ee1cdf28f8097a080f721bf4b480c67e8bfdd407d7b077e2619", "1.60.0--r43hdfd78af_0": "sha256:cd7fcb85b46e2805fee3cbaa8ccc62200ee26df0f9ed9d5adbebdbdbec5e1508", "1.64.0--r44hdfd78af_0": "sha256:649cca9d51a8fd9d570ab2b06d4c411c97a607926e6b3ae6085b728497f7fa4e"}, "docker": "quay.io/biocontainers/bioconductor-cghmcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cghmcr.
shpc-registry automated BioContainers addition for bioconductor-cghmcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cghmcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cghmcr:1.64.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cghmcr/1.64.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cghmcr/1.64.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cghmcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghmcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghmcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cghmcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cghmcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cghmcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cghmcr

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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