---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmap370k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmap370k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmap370k/container.yaml"
updated_at: "2025-09-11 05:20:18.845897"
latest: "1.0.1--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmap370k"

versions:
 - "1.0.1--r41hdfd78af_9"
 - "1.0.1--r42hdfd78af_10"
 - "1.0.1--r43hdfd78af_11"
 - "1.0.1--r43hdfd78af_12"
 - "1.0.1--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmap370k"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmap370k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmap370k", "latest": {"1.0.1--r44hdfd78af_13": "sha256:8967bd57f2b9f23ddf53cffd60c60c0634ba94e7620856f69c347a82c023a3d8"}, "tags": {"1.0.1--r41hdfd78af_9": "sha256:146630de4755a052ca987bfe7230a4dd0694627bf3bfaddbb04313ed498da934", "1.0.1--r42hdfd78af_10": "sha256:e806da61fea8d352d0c2eb5c61802ed527598eed4b71502877f57ca0e4b2ec4b", "1.0.1--r43hdfd78af_11": "sha256:7e0c0e26a9969f272da46630ae3f0142c74b950793fc191949aca491e93b8a7e", "1.0.1--r43hdfd78af_12": "sha256:a2a6abdbf629f3b90a480e52e0e79c67fcf6d421832b6454b07a8778b009a63c", "1.0.1--r44hdfd78af_13": "sha256:8967bd57f2b9f23ddf53cffd60c60c0634ba94e7620856f69c347a82c023a3d8"}, "docker": "quay.io/biocontainers/bioconductor-hapmap370k"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmap370k.
shpc-registry automated BioContainers addition for bioconductor-hapmap370k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap370k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap370k:1.0.1--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmap370k/1.0.1--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hapmap370k/1.0.1--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmap370k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap370k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap370k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmap370k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmap370k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmap370k-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmap370k

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