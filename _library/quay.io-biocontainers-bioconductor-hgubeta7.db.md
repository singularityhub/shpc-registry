---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgubeta7.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgubeta7.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgubeta7.db/container.yaml"
updated_at: "2025-12-13 03:37:36.004779"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgubeta7.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgubeta7.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgubeta7.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgubeta7.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:b2b917826558e4452ed056694a503bb4313538ae0080bf3fb1dc1c5128888037"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:85e2b59334604681fd059738c930d14c9f8ee93905ee95609c3e44ed0c4a516c", "3.2.3--r42hdfd78af_10": "sha256:67a04ed5667db7b97f61bf1ba88d5ecca0c2f615b668c485758aa0236d74d5fa", "3.2.3--r43hdfd78af_11": "sha256:1cffe3ed9e6d515a4ea99024644d7f04ab7a9b3f9d6f4d24c10313448c0ab0a1", "3.2.3--r43hdfd78af_12": "sha256:4bf24a0cf0833f75e835b681849f0032714e0abed97f88b4af3c64c2860be6d3", "3.2.3--r44hdfd78af_13": "sha256:b2b917826558e4452ed056694a503bb4313538ae0080bf3fb1dc1c5128888037"}, "docker": "quay.io/biocontainers/bioconductor-hgubeta7.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgubeta7.db.
shpc-registry automated BioContainers addition for bioconductor-hgubeta7.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgubeta7.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgubeta7.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgubeta7.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgubeta7.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgubeta7.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgubeta7.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgubeta7.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgubeta7.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgubeta7.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgubeta7.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgubeta7.db

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