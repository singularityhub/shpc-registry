---
layout: container
name:  "quay.io/biocontainers/gctb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gctb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gctb/container.yaml"
updated_at: "2025-09-08 05:26:39.534309"
latest: "2.0--h503566f_4"
container_url: "https://biocontainers.pro/tools/gctb"
aliases:
 - "gctb"
versions:
 - "2.0--hec16e2b_0"
 - "2.0--h031d066_2"
 - "2.0--h7b50bb2_3"
 - "2.0--h503566f_4"
description: "singularity registry hpc automated addition for gctb"
config: {"url": "https://biocontainers.pro/tools/gctb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gctb", "latest": {"2.0--h503566f_4": "sha256:1276c54b2c5d7da89508b77afa733ee882e160f82857e05192401c5ec8e2c7fb"}, "tags": {"2.0--hec16e2b_0": "sha256:e43572f640df477ed441c770ffe645b43d075b9abed060eb579915bdec97d2a8", "2.0--h031d066_2": "sha256:d05efac776e958b32da3cb593c829bd24249908b80ebfc93172e62eb74979d53", "2.0--h7b50bb2_3": "sha256:f179926f49de57f6b4895ad37889f95288d6ef98b6b425e854939ed3ce5b7ead", "2.0--h503566f_4": "sha256:1276c54b2c5d7da89508b77afa733ee882e160f82857e05192401c5ec8e2c7fb"}, "docker": "quay.io/biocontainers/gctb", "aliases": {"gctb": "/usr/local/bin/gctb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gctb.
singularity registry hpc automated addition for gctb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gctb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gctb:2.0--h503566f_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gctb/2.0--h503566f_4
$ module help quay.io/biocontainers/gctb/2.0--h503566f_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gctb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gctb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gctb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gctb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gctb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gctb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gctb

```bash
$ singularity exec <container> /usr/local/bin/gctb
$ podman run --it --rm --entrypoint /usr/local/bin/gctb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gctb   -v ${PWD} -w ${PWD} <container> -c " $@"
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