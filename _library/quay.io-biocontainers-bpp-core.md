---
layout: container
name:  "quay.io/biocontainers/bpp-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bpp-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bpp-core/container.yaml"
updated_at: "2025-04-08 03:41:25.548609"
latest: "2.4.1--h9f5acd7_6"
container_url: "https://biocontainers.pro/tools/bpp-core"

versions:
 - "2.4.1--h9f5acd7_4"
 - "2.4.1--h9f5acd7_6"
description: "shpc-registry automated BioContainers addition for bpp-core"
config: {"url": "https://biocontainers.pro/tools/bpp-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bpp-core", "latest": {"2.4.1--h9f5acd7_6": "sha256:b9d2b4ddb00c16cbe2448b5e8725336e91f4c9102c778bd7bf6536a15975e555"}, "tags": {"2.4.1--h9f5acd7_4": "sha256:18bf85db6e9a85269ccc2272901af7f0c997c17a2d0f8b9d0e6710c2b330357f", "2.4.1--h9f5acd7_6": "sha256:b9d2b4ddb00c16cbe2448b5e8725336e91f4c9102c778bd7bf6536a15975e555"}, "docker": "quay.io/biocontainers/bpp-core"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bpp-core.
shpc-registry automated BioContainers addition for bpp-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bpp-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bpp-core:2.4.1--h9f5acd7_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bpp-core/2.4.1--h9f5acd7_6
$ module help quay.io/biocontainers/bpp-core/2.4.1--h9f5acd7_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bpp-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bpp-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bpp-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bpp-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bpp-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bpp-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bpp-core

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