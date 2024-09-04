---
layout: container
name:  "quay.io/biocontainers/bioconductor-turbonorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-turbonorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-turbonorm/container.yaml"
updated_at: "2024-09-04 03:05:27.410922"
latest: "1.50.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-turbonorm"

versions:
 - "1.42.0--r41hc0cfd56_2"
 - "1.46.0--r42hc0cfd56_0"
 - "1.46.0--r42ha9d7317_1"
 - "1.48.0--r43ha9d7317_0"
 - "1.50.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-turbonorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-turbonorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-turbonorm", "latest": {"1.50.0--r43ha9d7317_0": "sha256:36f18c36cbe4e17917fdcf440733bd3ab85ab461b6b423be2651c250a319e161"}, "tags": {"1.42.0--r41hc0cfd56_2": "sha256:6c8c83fb3f1bfdc51bdfdd03c289fffb2ed70bbc9b88c1a70f53fd291cb3ad59", "1.46.0--r42hc0cfd56_0": "sha256:7639459e855ff0ad59e9f0ca8dc56a09f342305023d882a23588c7b1b9e05511", "1.46.0--r42ha9d7317_1": "sha256:9f5fd72c96aa7cc0a61bd39e6d4c0d8701a9fddc4d09bfe0255016c9ee646788", "1.48.0--r43ha9d7317_0": "sha256:7dc6598cc80147f35d2a89730a5395df9b224ced7bf8da4dcd892638ef5990a8", "1.50.0--r43ha9d7317_0": "sha256:36f18c36cbe4e17917fdcf440733bd3ab85ab461b6b423be2651c250a319e161"}, "docker": "quay.io/biocontainers/bioconductor-turbonorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-turbonorm.
shpc-registry automated BioContainers addition for bioconductor-turbonorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-turbonorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-turbonorm:1.50.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-turbonorm/1.50.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-turbonorm/1.50.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-turbonorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-turbonorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-turbonorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-turbonorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-turbonorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-turbonorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-turbonorm

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