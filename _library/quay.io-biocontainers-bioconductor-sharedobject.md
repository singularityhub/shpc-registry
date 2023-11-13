---
layout: container
name:  "quay.io/biocontainers/bioconductor-sharedobject"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sharedobject/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sharedobject/container.yaml"
updated_at: "2023-11-13 02:39:26.213219"
latest: "1.12.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-sharedobject"

versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-sharedobject"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sharedobject", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sharedobject", "latest": {"1.12.0--r42hf17093f_1": "sha256:442469d43c1aaab50d97545d1d5603c285cb86c918a8a3842e1afad0d1a72a7e"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:3a776b57ef04f6d7f56c91011c4fa27b69fc832ad2a2d3b037ae8f6e40f5810c", "1.12.0--r42hc247a5b_0": "sha256:f9ddc2c7dfdb9c42c781a0f718e31afb0005a0231e8acdba223231f0729fdb7c", "1.12.0--r42hf17093f_1": "sha256:442469d43c1aaab50d97545d1d5603c285cb86c918a8a3842e1afad0d1a72a7e"}, "docker": "quay.io/biocontainers/bioconductor-sharedobject"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sharedobject.
shpc-registry automated BioContainers addition for bioconductor-sharedobject
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sharedobject
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sharedobject:1.12.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sharedobject/1.12.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-sharedobject/1.12.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sharedobject-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sharedobject-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sharedobject-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sharedobject-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sharedobject-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sharedobject-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sharedobject

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