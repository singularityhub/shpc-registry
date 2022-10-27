---
layout: container
name:  "quay.io/biocontainers/bioconductor-tfea.chip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tfea.chip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tfea.chip/container.yaml"
updated_at: "2022-10-27 00:42:04.474987"
latest: "1.8.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tfea.chip"

versions:
 - "1.8.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tfea.chip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tfea.chip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tfea.chip", "latest": {"1.8.0--r40_0": "sha256:4c4407505e36645eada6e683f6377280155443bce56fd9d9311029c363601c05"}, "tags": {"1.8.0--r40_0": "sha256:4c4407505e36645eada6e683f6377280155443bce56fd9d9311029c363601c05"}, "docker": "quay.io/biocontainers/bioconductor-tfea.chip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tfea.chip.
shpc-registry automated BioContainers addition for bioconductor-tfea.chip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tfea.chip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tfea.chip:1.8.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tfea.chip/1.8.0--r40_0
$ module help quay.io/biocontainers/bioconductor-tfea.chip/1.8.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tfea.chip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfea.chip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfea.chip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tfea.chip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tfea.chip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tfea.chip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tfea.chip

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