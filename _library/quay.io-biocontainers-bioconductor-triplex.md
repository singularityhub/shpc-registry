---
layout: container
name:  "quay.io/biocontainers/bioconductor-triplex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-triplex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-triplex/container.yaml"
updated_at: "2023-08-11 02:51:47.823863"
latest: "1.40.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-triplex"

versions:
 - "1.34.0--r41hc0cfd56_2"
 - "1.38.0--r42hc0cfd56_0"
 - "1.38.0--r42ha9d7317_1"
 - "1.40.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-triplex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-triplex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-triplex", "latest": {"1.40.0--r43ha9d7317_0": "sha256:d397f6590666a5bd0fea2b7676e2d2baaa6233c34943e16e6f09b49ea86d8f24"}, "tags": {"1.34.0--r41hc0cfd56_2": "sha256:4707a4abd583efb9de5100cec5b617208e82d7695d5ddba7cd1d5ae146a5d067", "1.38.0--r42hc0cfd56_0": "sha256:e6b0b5a0b8011e2ddca8fc33bd133b4a6da7c8a87b81497ba66d7c6f628ccafc", "1.38.0--r42ha9d7317_1": "sha256:7d4725371cbd4ae1252a0f135552a33edd478f7a55bac7673a6d633a7daf794c", "1.40.0--r43ha9d7317_0": "sha256:d397f6590666a5bd0fea2b7676e2d2baaa6233c34943e16e6f09b49ea86d8f24"}, "docker": "quay.io/biocontainers/bioconductor-triplex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-triplex.
shpc-registry automated BioContainers addition for bioconductor-triplex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-triplex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-triplex:1.40.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-triplex/1.40.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-triplex/1.40.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-triplex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-triplex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-triplex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-triplex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-triplex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-triplex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-triplex

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