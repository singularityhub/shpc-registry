---
layout: container
name:  "quay.io/biocontainers/bioconductor-pqsfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pqsfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pqsfinder/container.yaml"
updated_at: "2023-03-27 03:03:56.890492"
latest: "2.14.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pqsfinder"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41h399db7b_0"
 - "2.14.0--r42hc247a5b_0"
 - "2.10.1--r41hc247a5b_1"
description: "shpc-registry automated BioContainers addition for bioconductor-pqsfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pqsfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pqsfinder", "latest": {"2.14.0--r42hc247a5b_0": "sha256:f67ec7eb4b6d56a669de393dfdb866468045e6cc719014fba8aa26e6cedccb7f"}, "tags": {"2.8.0--r41h399db7b_0": "sha256:8aad930cd2d6e83611a29924a09a14d979823f82a4d28f3a2cf5f65cf2eaa55e", "2.14.0--r42hc247a5b_0": "sha256:f67ec7eb4b6d56a669de393dfdb866468045e6cc719014fba8aa26e6cedccb7f", "2.10.1--r41hc247a5b_1": "sha256:e4fbe764d874c0103556ccdcfd45d6c3ae8c24ae06e872a302d1e973288ca153"}, "docker": "quay.io/biocontainers/bioconductor-pqsfinder", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pqsfinder.
shpc-registry automated BioContainers addition for bioconductor-pqsfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pqsfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pqsfinder:2.14.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pqsfinder/2.14.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-pqsfinder/2.14.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pqsfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pqsfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pqsfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pqsfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pqsfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pqsfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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