---
layout: container
name:  "quay.io/biocontainers/equirep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/equirep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/equirep/container.yaml"
updated_at: "2025-05-14 03:44:05.299426"
latest: "1.0.0--h9948957_0"
container_url: "https://biocontainers.pro/tools/equirep"
aliases:
 - "EquiRep"
versions:
 - "1.0.0--h9948957_0"
description: "singularity registry hpc automated addition for equirep"
config: {"url": "https://biocontainers.pro/tools/equirep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for equirep", "latest": {"1.0.0--h9948957_0": "sha256:71e502ce177ac87f48609bfdec23bc0ee0284609b1f316e01f311a16225e4e3f"}, "tags": {"1.0.0--h9948957_0": "sha256:71e502ce177ac87f48609bfdec23bc0ee0284609b1f316e01f311a16225e4e3f"}, "docker": "quay.io/biocontainers/equirep", "aliases": {"EquiRep": "/usr/local/bin/EquiRep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/equirep.
singularity registry hpc automated addition for equirep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/equirep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/equirep:1.0.0--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/equirep/1.0.0--h9948957_0
$ module help quay.io/biocontainers/equirep/1.0.0--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### equirep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### equirep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### equirep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### equirep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### equirep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### equirep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EquiRep

```bash
$ singularity exec <container> /usr/local/bin/EquiRep
$ podman run --it --rm --entrypoint /usr/local/bin/EquiRep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EquiRep   -v ${PWD} -w ${PWD} <container> -c " $@"
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