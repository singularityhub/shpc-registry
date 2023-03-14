---
layout: container
name:  "quay.io/biocontainers/bioconductor-bamsignals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bamsignals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bamsignals/container.yaml"
updated_at: "2023-03-14 02:57:05.302478"
latest: "1.30.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bamsignals"

versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bamsignals"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bamsignals", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bamsignals", "latest": {"1.30.0--r42hc247a5b_0": "sha256:9e034e37b3b8c3442198a100acae14b78b4b318d6d948795c8b813cf657e62e2"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:d01915ae50dcaf030eb3cc4ebc52e709699d1fb3c54897a7c386b50a4b7fb573", "1.30.0--r42hc247a5b_0": "sha256:9e034e37b3b8c3442198a100acae14b78b4b318d6d948795c8b813cf657e62e2"}, "docker": "quay.io/biocontainers/bioconductor-bamsignals"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bamsignals.
shpc-registry automated BioContainers addition for bioconductor-bamsignals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bamsignals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bamsignals:1.30.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bamsignals/1.30.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-bamsignals/1.30.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bamsignals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bamsignals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bamsignals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bamsignals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bamsignals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bamsignals-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bamsignals

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