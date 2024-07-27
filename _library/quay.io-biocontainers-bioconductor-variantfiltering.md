---
layout: container
name:  "quay.io/biocontainers/bioconductor-variantfiltering"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-variantfiltering/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-variantfiltering/container.yaml"
updated_at: "2024-07-27 03:17:34.158555"
latest: "1.36.1--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-variantfiltering"

versions:
 - "1.30.0--r41hc0cfd56_2"
 - "1.34.0--r42hc0cfd56_0"
 - "1.34.0--r42ha9d7317_1"
 - "1.36.1--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-variantfiltering"
config: {"url": "https://biocontainers.pro/tools/bioconductor-variantfiltering", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-variantfiltering", "latest": {"1.36.1--r43ha9d7317_0": "sha256:354da49d02e8708bbe8caf02dd1758e1f42f583ba87848d095c557210775c61f"}, "tags": {"1.30.0--r41hc0cfd56_2": "sha256:47a2d3c1c783b0b4bbd5af9d328786c99002c3cb30eb310e9fc84251c5697f18", "1.34.0--r42hc0cfd56_0": "sha256:4f52c2dcc890ab5866ef041c00ea15c7dc11160a3e59cdcb08e93b802d87511a", "1.34.0--r42ha9d7317_1": "sha256:1eb3eb9ff7986db5cafa5637f0d1849153999fb18b32ba5d64ff55d834c8a749", "1.36.1--r43ha9d7317_0": "sha256:354da49d02e8708bbe8caf02dd1758e1f42f583ba87848d095c557210775c61f"}, "docker": "quay.io/biocontainers/bioconductor-variantfiltering"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-variantfiltering.
shpc-registry automated BioContainers addition for bioconductor-variantfiltering
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-variantfiltering
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-variantfiltering:1.36.1--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-variantfiltering/1.36.1--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-variantfiltering/1.36.1--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-variantfiltering-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantfiltering-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantfiltering-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-variantfiltering-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-variantfiltering-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-variantfiltering-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-variantfiltering

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