---
layout: container
name:  "quay.io/biocontainers/r-taxonomizr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-taxonomizr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-taxonomizr/container.yaml"
updated_at: "2022-10-27 01:04:11.298515"
latest: "0.7.1--r40hdf9a8c9_0"
container_url: "https://biocontainers.pro/tools/r-taxonomizr"

versions:
 - "0.7.1--r40hdf9a8c9_0"
description: "shpc-registry automated BioContainers addition for r-taxonomizr"
config: {"url": "https://biocontainers.pro/tools/r-taxonomizr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-taxonomizr", "latest": {"0.7.1--r40hdf9a8c9_0": "sha256:d7bed21e5b814210dc8d7a89a4e0409c9d796934d8da4f2ccca8b30a60f89c0e"}, "tags": {"0.7.1--r40hdf9a8c9_0": "sha256:d7bed21e5b814210dc8d7a89a4e0409c9d796934d8da4f2ccca8b30a60f89c0e"}, "docker": "quay.io/biocontainers/r-taxonomizr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-taxonomizr.
shpc-registry automated BioContainers addition for r-taxonomizr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-taxonomizr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-taxonomizr:0.7.1--r40hdf9a8c9_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-taxonomizr/0.7.1--r40hdf9a8c9_0
$ module help quay.io/biocontainers/r-taxonomizr/0.7.1--r40hdf9a8c9_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-taxonomizr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-taxonomizr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-taxonomizr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-taxonomizr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-taxonomizr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-taxonomizr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-taxonomizr

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