---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnagilentdesign028282.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnagilentdesign028282.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnagilentdesign028282.db/container.yaml"
updated_at: "2023-12-03 02:41:49.248871"
latest: "3.2.3--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-rnagilentdesign028282.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-rnagilentdesign028282.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnagilentdesign028282.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnagilentdesign028282.db", "latest": {"3.2.3--r43hdfd78af_11": "sha256:c1448f71def48b82ffbf72cee2bcdb9366550e2c922b52f986b2d1232ece6197"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:025cf6e90502f19b18bbd4f8e041b68d713a9a893d0b817f8ff30c880795d6f4", "3.2.3--r42hdfd78af_10": "sha256:ebce38d2e1b50a1d55db739d7f71fb0c6e0db52ae389d5d8b0a972b06926d6b1", "3.2.3--r43hdfd78af_11": "sha256:c1448f71def48b82ffbf72cee2bcdb9366550e2c922b52f986b2d1232ece6197"}, "docker": "quay.io/biocontainers/bioconductor-rnagilentdesign028282.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnagilentdesign028282.db.
shpc-registry automated BioContainers addition for bioconductor-rnagilentdesign028282.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnagilentdesign028282.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnagilentdesign028282.db:3.2.3--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnagilentdesign028282.db/3.2.3--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-rnagilentdesign028282.db/3.2.3--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnagilentdesign028282.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnagilentdesign028282.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnagilentdesign028282.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnagilentdesign028282.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnagilentdesign028282.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnagilentdesign028282.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnagilentdesign028282.db

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