---
layout: container
name:  "quay.io/biocontainers/bioconductor-reb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reb/container.yaml"
updated_at: "2022-10-27 01:14:06.463667"
latest: "1.65.0--r40h037d062_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reb"

versions:
 - "1.65.0--r40h037d062_0"
description: "shpc-registry automated BioContainers addition for bioconductor-reb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-reb", "latest": {"1.65.0--r40h037d062_0": "sha256:8869550f1a7ad395722d95a9199f53f750ec44d2c329929a977d4b7f7a33f7a2"}, "tags": {"1.65.0--r40h037d062_0": "sha256:8869550f1a7ad395722d95a9199f53f750ec44d2c329929a977d4b7f7a33f7a2"}, "docker": "quay.io/biocontainers/bioconductor-reb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reb.
shpc-registry automated BioContainers addition for bioconductor-reb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reb:1.65.0--r40h037d062_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reb/1.65.0--r40h037d062_0
$ module help quay.io/biocontainers/bioconductor-reb/1.65.0--r40h037d062_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-reb

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