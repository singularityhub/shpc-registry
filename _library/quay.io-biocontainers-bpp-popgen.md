---
layout: container
name:  "quay.io/biocontainers/bpp-popgen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bpp-popgen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bpp-popgen/container.yaml"
updated_at: "2025-05-23 03:21:22.907820"
latest: "2.4.1--h9948957_5"
container_url: "https://biocontainers.pro/tools/bpp-popgen"

versions:
 - "2.4.1--h9f5acd7_3"
 - "2.4.1--h4ac6f70_4"
 - "2.4.1--h9948957_5"
description: "shpc-registry automated BioContainers addition for bpp-popgen"
config: {"url": "https://biocontainers.pro/tools/bpp-popgen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bpp-popgen", "latest": {"2.4.1--h9948957_5": "sha256:ed1ecb5ee82465cea64652b1c0716f359d88d1c6891cac057dcdd1210a94ff5f"}, "tags": {"2.4.1--h9f5acd7_3": "sha256:e0d077bbd4951f9f27a4460d613e3229f06dd2b089d856a01bd325f6ac607fe6", "2.4.1--h4ac6f70_4": "sha256:01460edba08258896628a582fe036603dbc82f19c3126ed668954c4c5c95fb35", "2.4.1--h9948957_5": "sha256:ed1ecb5ee82465cea64652b1c0716f359d88d1c6891cac057dcdd1210a94ff5f"}, "docker": "quay.io/biocontainers/bpp-popgen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bpp-popgen.
shpc-registry automated BioContainers addition for bpp-popgen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bpp-popgen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bpp-popgen:2.4.1--h9948957_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bpp-popgen/2.4.1--h9948957_5
$ module help quay.io/biocontainers/bpp-popgen/2.4.1--h9948957_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bpp-popgen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bpp-popgen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bpp-popgen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bpp-popgen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bpp-popgen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bpp-popgen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bpp-popgen

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