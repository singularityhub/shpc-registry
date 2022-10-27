---
layout: container
name:  "quay.io/biocontainers/bioconductor-gdsarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gdsarray/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gdsarray/container.yaml"
updated_at: "2022-10-27 00:21:03.356164"
latest: "1.8.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gdsarray"

versions:
 - "1.8.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gdsarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gdsarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gdsarray", "latest": {"1.8.0--r40_0": "sha256:64208985e7e71ce882f62448175fca9e52e41749f100439b104fcaac7837cda4"}, "tags": {"1.8.0--r40_0": "sha256:64208985e7e71ce882f62448175fca9e52e41749f100439b104fcaac7837cda4"}, "docker": "quay.io/biocontainers/bioconductor-gdsarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gdsarray.
shpc-registry automated BioContainers addition for bioconductor-gdsarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gdsarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gdsarray:1.8.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gdsarray/1.8.0--r40_0
$ module help quay.io/biocontainers/bioconductor-gdsarray/1.8.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gdsarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gdsarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gdsarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gdsarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gdsarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gdsarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gdsarray

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