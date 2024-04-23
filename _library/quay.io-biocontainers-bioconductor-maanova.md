---
layout: container
name:  "quay.io/biocontainers/bioconductor-maanova"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maanova/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maanova/container.yaml"
updated_at: "2024-04-23 02:50:15.730646"
latest: "1.68.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-maanova"

versions:
 - "1.64.0--r41hc0cfd56_2"
 - "1.68.0--r42hc0cfd56_0"
 - "1.68.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-maanova"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maanova", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maanova", "latest": {"1.68.0--r42ha9d7317_1": "sha256:f7568445d270473b1534f3fc3a18f8a4018c4eef15d459096441ba241236df99"}, "tags": {"1.64.0--r41hc0cfd56_2": "sha256:a9c06bea9e2d63dc496ea56c686a5ef677a6b9045adfc2ce0fecc7bb3b61a590", "1.68.0--r42hc0cfd56_0": "sha256:5a168ab4319637b67b9a66d356b60b7a0816e5a2e58017d7156c9a1930fcd210", "1.68.0--r42ha9d7317_1": "sha256:f7568445d270473b1534f3fc3a18f8a4018c4eef15d459096441ba241236df99"}, "docker": "quay.io/biocontainers/bioconductor-maanova"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maanova.
shpc-registry automated BioContainers addition for bioconductor-maanova
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maanova
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maanova:1.68.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maanova/1.68.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-maanova/1.68.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maanova-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maanova-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maanova-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maanova-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maanova-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maanova-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maanova

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