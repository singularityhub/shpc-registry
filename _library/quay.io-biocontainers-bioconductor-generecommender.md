---
layout: container
name:  "quay.io/biocontainers/bioconductor-generecommender"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-generecommender/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-generecommender/container.yaml"
updated_at: "2025-10-21 03:11:24.736945"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-generecommender"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-generecommender"
config: {"url": "https://biocontainers.pro/tools/bioconductor-generecommender", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-generecommender", "latest": {"1.78.0--r44hdfd78af_0": "sha256:af8539fb000931e45527ffb46245f60921dd669e5a38aac82243f926dcc03fb3"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:d5ad1bf6fcc002b1a0fb1be5ced715fa4f092990d5893ab612eb70f636b947b5", "1.70.0--r42hdfd78af_0": "sha256:d4627b0aa00d9a262f7db3071a4828273da9589d334d72c2e3964f0988384a0b", "1.72.0--r43hdfd78af_0": "sha256:883cdb0a6ce723541e01467cdc087d8cedd957504d4ab5c0c60201dfac461ad1", "1.74.0--r43hdfd78af_0": "sha256:1990ad109b4951d60042cb2d6c73e6546f6b00ae1131da910fdc3f9058a5f298", "1.78.0--r44hdfd78af_0": "sha256:af8539fb000931e45527ffb46245f60921dd669e5a38aac82243f926dcc03fb3"}, "docker": "quay.io/biocontainers/bioconductor-generecommender"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-generecommender.
shpc-registry automated BioContainers addition for bioconductor-generecommender
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-generecommender
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-generecommender:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-generecommender/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-generecommender/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-generecommender-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-generecommender-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-generecommender-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-generecommender-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-generecommender-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-generecommender-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-generecommender

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