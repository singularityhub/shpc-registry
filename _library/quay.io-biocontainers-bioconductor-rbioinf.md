---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbioinf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbioinf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbioinf/container.yaml"
updated_at: "2023-09-30 03:07:23.810893"
latest: "1.60.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rbioinf"

versions:
 - "1.54.0--r41hc0cfd56_2"
 - "1.58.0--r42hc0cfd56_0"
 - "1.58.0--r42ha9d7317_1"
 - "1.60.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rbioinf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbioinf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbioinf", "latest": {"1.60.0--r43ha9d7317_0": "sha256:86a1fa90c8d477f81545979c65c2d20cdb02926be3be6d6de8a8d09e3f94ed1a"}, "tags": {"1.54.0--r41hc0cfd56_2": "sha256:631191850d3edd75f715a58c0a8e4eed3adaf293e362095a76d08839ba16bab2", "1.58.0--r42hc0cfd56_0": "sha256:12534567c0aa0dcfbc3d7e89572dbe0ae21ec91fb139d7678e71f7b6317bfc72", "1.58.0--r42ha9d7317_1": "sha256:8209760fa1ecd0035fa3817102418c0436c53d07e9b452398684144de02d6727", "1.60.0--r43ha9d7317_0": "sha256:86a1fa90c8d477f81545979c65c2d20cdb02926be3be6d6de8a8d09e3f94ed1a"}, "docker": "quay.io/biocontainers/bioconductor-rbioinf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbioinf.
shpc-registry automated BioContainers addition for bioconductor-rbioinf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbioinf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbioinf:1.60.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbioinf/1.60.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-rbioinf/1.60.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbioinf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbioinf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbioinf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbioinf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbioinf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbioinf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbioinf

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