---
layout: container
name:  "quay.io/biocontainers/gloome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gloome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gloome/container.yaml"
updated_at: "2024-06-26 03:02:39.893200"
latest: "VR01.266--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/gloome"
aliases:
 - "gainLoss"
versions:
 - "VR01.266--h9f5acd7_1"
 - "VR01.266--h9f5acd7_2"
 - "VR01.266--h4ac6f70_3"
description: "singularity registry hpc automated addition for gloome"
config: {"url": "https://biocontainers.pro/tools/gloome", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gloome", "latest": {"VR01.266--h4ac6f70_3": "sha256:b751012bb79eaad5edcd762246f1f9821f8a7d3b6e91c354208862f153395c2f"}, "tags": {"VR01.266--h9f5acd7_1": "sha256:64b163645b6c960368ac6b2eff22515ed6ba7052878b52d5b047d52cdd2379a9", "VR01.266--h9f5acd7_2": "sha256:46b57c837437bdcc2c82b7056dae7ee429b2c02d59d4b7fe24ef1a9402fec5e6", "VR01.266--h4ac6f70_3": "sha256:b751012bb79eaad5edcd762246f1f9821f8a7d3b6e91c354208862f153395c2f"}, "docker": "quay.io/biocontainers/gloome", "aliases": {"gainLoss": "/usr/local/bin/gainLoss"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gloome.
singularity registry hpc automated addition for gloome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gloome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gloome:VR01.266--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gloome/VR01.266--h4ac6f70_3
$ module help quay.io/biocontainers/gloome/VR01.266--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gloome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gloome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gloome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gloome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gloome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gloome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gainLoss

```bash
$ singularity exec <container> /usr/local/bin/gainLoss
$ podman run --it --rm --entrypoint /usr/local/bin/gainLoss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gainLoss   -v ${PWD} -w ${PWD} <container> -c " $@"
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