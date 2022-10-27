---
layout: container
name:  "quay.io/biocontainers/itsx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/itsx/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/itsx/container.yaml"
updated_at: "2022-10-27 00:46:17.030826"
latest: "1.1b--2"
container_url: "https://biocontainers.pro/tools/itsx"
aliases:
 - "ITSx"
versions:
 - "1.1b--2"
description: "shpc-registry automated BioContainers addition for itsx"
config: {"url": "https://biocontainers.pro/tools/itsx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for itsx", "latest": {"1.1b--2": "sha256:460ad79eea1aebb5be6a640c7c9103833e4d2df1596f3471fd78f79c95ad1429"}, "tags": {"1.1b--2": "sha256:460ad79eea1aebb5be6a640c7c9103833e4d2df1596f3471fd78f79c95ad1429"}, "docker": "quay.io/biocontainers/itsx", "aliases": {"ITSx": "/usr/local/bin/ITSx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/itsx.
shpc-registry automated BioContainers addition for itsx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/itsx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/itsx:1.1b--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/itsx/1.1b--2
$ module help quay.io/biocontainers/itsx/1.1b--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### itsx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### itsx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### itsx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### itsx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### itsx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### itsx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ITSx

```bash
$ singularity exec <container> /usr/local/bin/ITSx
$ podman run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
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