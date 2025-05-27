---
layout: container
name:  "quay.io/biocontainers/icount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/icount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/icount/container.yaml"
updated_at: "2025-05-27 11:21:11.046648"
latest: "2.0.0--py_1"
container_url: "https://biocontainers.pro/tools/icount"

versions:
 - "2.0.0--py_1"
description: "shpc-registry automated BioContainers addition for icount"
config: {"url": "https://biocontainers.pro/tools/icount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for icount", "latest": {"2.0.0--py_1": "sha256:50d5f3cbcd7d7196c5be555ff59c973bfcd6edc8bac2d23a25e690773a54646e"}, "tags": {"2.0.0--py_1": "sha256:50d5f3cbcd7d7196c5be555ff59c973bfcd6edc8bac2d23a25e690773a54646e"}, "docker": "quay.io/biocontainers/icount"}
---

This module is a singularity container wrapper for quay.io/biocontainers/icount.
shpc-registry automated BioContainers addition for icount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/icount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/icount:2.0.0--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/icount/2.0.0--py_1
$ module help quay.io/biocontainers/icount/2.0.0--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### icount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### icount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### icount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### icount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### icount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### icount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### icount

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