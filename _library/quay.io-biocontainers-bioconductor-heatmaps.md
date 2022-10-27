---
layout: container
name:  "quay.io/biocontainers/bioconductor-heatmaps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-heatmaps/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-heatmaps/container.yaml"
updated_at: "2022-10-27 00:20:07.421963"
latest: "1.8.0--r36_1"
container_url: "https://biocontainers.pro/tools/bioconductor-heatmaps"

versions:
 - "1.8.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-heatmaps"
config: {"url": "https://biocontainers.pro/tools/bioconductor-heatmaps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-heatmaps", "latest": {"1.8.0--r36_1": "sha256:d0cdbe17b7eb6595ad73c356d714553f4a112ce66b2b6220f025bc075834c430"}, "tags": {"1.8.0--r36_1": "sha256:d0cdbe17b7eb6595ad73c356d714553f4a112ce66b2b6220f025bc075834c430"}, "docker": "quay.io/biocontainers/bioconductor-heatmaps"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-heatmaps.
shpc-registry automated BioContainers addition for bioconductor-heatmaps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-heatmaps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-heatmaps:1.8.0--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-heatmaps/1.8.0--r36_1
$ module help quay.io/biocontainers/bioconductor-heatmaps/1.8.0--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-heatmaps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heatmaps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heatmaps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-heatmaps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-heatmaps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-heatmaps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-heatmaps

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