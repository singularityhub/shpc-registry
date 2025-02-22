---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhesusprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhesusprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhesusprobe/container.yaml"
updated_at: "2025-02-22 02:52:22.142997"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rhesusprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rhesusprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhesusprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhesusprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:dce66225af29ca9b0902906a4b5fb72c675c59dc500bfccce9c2a268a892fa7e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0032667df49fc7e5f7ddb10fab0ccd0b1f4c80a5ab8940f15b459b86d001cfed", "2.18.0--r42hdfd78af_10": "sha256:073f4252fb6d339f8cd82b72a06362edaddeee2a8f2f7fb72bb911f5dbbd3ec1", "2.18.0--r43hdfd78af_11": "sha256:1675cc67b1f2b77ff1af9d4224c1f134747863437b3aac976d6d9c60d96532ef", "2.18.0--r43hdfd78af_12": "sha256:0cd2d9ec407d26569438616100674e10f1a387f198cb00add3a6e472ba38b87f", "2.18.0--r44hdfd78af_13": "sha256:dce66225af29ca9b0902906a4b5fb72c675c59dc500bfccce9c2a268a892fa7e"}, "docker": "quay.io/biocontainers/bioconductor-rhesusprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhesusprobe.
shpc-registry automated BioContainers addition for bioconductor-rhesusprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesusprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesusprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhesusprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rhesusprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhesusprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesusprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesusprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhesusprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhesusprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhesusprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rhesusprobe

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