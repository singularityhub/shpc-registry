---
layout: container
name:  "quay.io/biocontainers/plantcv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plantcv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plantcv/container.yaml"
updated_at: "2025-08-05 04:37:19.955794"
latest: "3.8.0--py_0"
container_url: "https://biocontainers.pro/tools/plantcv"

versions:
 - "3.8.0--py_0"
description: "shpc-registry automated BioContainers addition for plantcv"
config: {"url": "https://biocontainers.pro/tools/plantcv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plantcv", "latest": {"3.8.0--py_0": "sha256:0bded2c50939b7c1aa20b6be37e0b671c4e54bed406d976f3668311eb970ae26"}, "tags": {"3.8.0--py_0": "sha256:0bded2c50939b7c1aa20b6be37e0b671c4e54bed406d976f3668311eb970ae26"}, "docker": "quay.io/biocontainers/plantcv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/plantcv.
shpc-registry automated BioContainers addition for plantcv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plantcv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plantcv:3.8.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plantcv/3.8.0--py_0
$ module help quay.io/biocontainers/plantcv/3.8.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plantcv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plantcv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plantcv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plantcv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plantcv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plantcv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### plantcv

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