---
layout: container
name:  "quay.io/biocontainers/r-png"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-png/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-png/container.yaml"
updated_at: "2022-10-27 00:32:11.555702"
latest: "0.1.7--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-png"

versions:
 - "0.1.7--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-png"
config: {"url": "https://biocontainers.pro/tools/r-png", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-png", "latest": {"0.1.7--r3.2.2_0": "sha256:b8d6f0c230db70c701ebba6154c978aa03d3bbf211ee75f4dc624efd3d61c5c5"}, "tags": {"0.1.7--r3.2.2_0": "sha256:b8d6f0c230db70c701ebba6154c978aa03d3bbf211ee75f4dc624efd3d61c5c5"}, "docker": "quay.io/biocontainers/r-png"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-png.
shpc-registry automated BioContainers addition for r-png
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-png
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-png:0.1.7--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-png/0.1.7--r3.2.2_0
$ module help quay.io/biocontainers/r-png/0.1.7--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-png-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-png-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-png-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-png-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-png-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-png-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-png

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