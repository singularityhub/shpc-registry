---
layout: container
name:  "quay.io/biocontainers/annonars"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/annonars/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/annonars/container.yaml"
updated_at: "2023-06-06 03:39:33.510867"
latest: "0.5.0--h63738d7_0"
container_url: "https://biocontainers.pro/tools/annonars"
aliases:
 - "annonars"
versions:
 - "0.5.0--h63738d7_0"
description: "singularity registry hpc automated addition for annonars"
config: {"url": "https://biocontainers.pro/tools/annonars", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for annonars", "latest": {"0.5.0--h63738d7_0": "sha256:5c330116a257365c8c35ef82850d493137dd6c0dd3fbb2d113eabf356409491e"}, "tags": {"0.5.0--h63738d7_0": "sha256:5c330116a257365c8c35ef82850d493137dd6c0dd3fbb2d113eabf356409491e"}, "docker": "quay.io/biocontainers/annonars", "aliases": {"annonars": "/usr/local/bin/annonars"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/annonars.
singularity registry hpc automated addition for annonars
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/annonars
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/annonars:0.5.0--h63738d7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/annonars/0.5.0--h63738d7_0
$ module help quay.io/biocontainers/annonars/0.5.0--h63738d7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### annonars-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### annonars-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### annonars-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### annonars-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### annonars-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### annonars-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annonars

```bash
$ singularity exec <container> /usr/local/bin/annonars
$ podman run --it --rm --entrypoint /usr/local/bin/annonars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annonars   -v ${PWD} -w ${PWD} <container> -c " $@"
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