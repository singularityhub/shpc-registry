---
layout: container
name:  "quay.io/biocontainers/bioconductor-ioniser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ioniser/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ioniser/container.yaml"
updated_at: "2022-10-27 00:31:37.026494"
latest: "2.8.0--r36_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ioniser"

versions:
 - "2.8.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ioniser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ioniser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ioniser", "latest": {"2.8.0--r36_1": "sha256:08e6f60502cea1b5e09e21dee7314d2d8cb6a2c6fc3c62e9338e1c01d4d5dd7d"}, "tags": {"2.8.0--r36_1": "sha256:08e6f60502cea1b5e09e21dee7314d2d8cb6a2c6fc3c62e9338e1c01d4d5dd7d"}, "docker": "quay.io/biocontainers/bioconductor-ioniser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ioniser.
shpc-registry automated BioContainers addition for bioconductor-ioniser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ioniser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ioniser:2.8.0--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ioniser/2.8.0--r36_1
$ module help quay.io/biocontainers/bioconductor-ioniser/2.8.0--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ioniser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ioniser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ioniser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ioniser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ioniser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ioniser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ioniser

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