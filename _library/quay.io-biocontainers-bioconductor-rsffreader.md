---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsffreader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsffreader/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsffreader/container.yaml"
updated_at: "2022-10-27 01:02:11.681907"
latest: "0.31.0--r36h516909a_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rsffreader"

versions:
 - "0.31.0--r36h516909a_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rsffreader"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsffreader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsffreader", "latest": {"0.31.0--r36h516909a_1": "sha256:7518267eed9c72657e7c2f1fe19c3efd3687dc8388ab588e90737a43435f0fff"}, "tags": {"0.31.0--r36h516909a_1": "sha256:7518267eed9c72657e7c2f1fe19c3efd3687dc8388ab588e90737a43435f0fff"}, "docker": "quay.io/biocontainers/bioconductor-rsffreader"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsffreader.
shpc-registry automated BioContainers addition for bioconductor-rsffreader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsffreader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsffreader:0.31.0--r36h516909a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsffreader/0.31.0--r36h516909a_1
$ module help quay.io/biocontainers/bioconductor-rsffreader/0.31.0--r36h516909a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsffreader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsffreader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsffreader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsffreader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsffreader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsffreader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsffreader

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