---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu11ksubacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu11ksubacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu11ksubacdf/container.yaml"
updated_at: "2025-05-26 12:13:45.555517"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mu11ksubacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mu11ksubacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu11ksubacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu11ksubacdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:0d33fcb9559cf5726dba69f3c2c69c37b86ff5f6b657caffa81dd2d1e65e997b"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d3b71794750d0bce6d0a3ad627e5072b87640f0ddee768a2518c49e6114822ba", "2.18.0--r42hdfd78af_10": "sha256:a3a800ee818d35cb820d6fc224f614ed70d02f545b562ba4f6910527eb436dfd", "2.18.0--r43hdfd78af_11": "sha256:d22edc0f8b467d42bd02bb7f3300ad8d3f90fbcf9992af76e9eec3922cdbc996", "2.18.0--r43hdfd78af_12": "sha256:d5c3e1b46a9da340e0107f81e60266a7c3b7a2500ba06f085b2777aa6b9745e3", "2.18.0--r44hdfd78af_13": "sha256:0d33fcb9559cf5726dba69f3c2c69c37b86ff5f6b657caffa81dd2d1e65e997b"}, "docker": "quay.io/biocontainers/bioconductor-mu11ksubacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu11ksubacdf.
shpc-registry automated BioContainers addition for bioconductor-mu11ksubacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubacdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu11ksubacdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mu11ksubacdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu11ksubacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu11ksubacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu11ksubacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu11ksubacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu11ksubacdf

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