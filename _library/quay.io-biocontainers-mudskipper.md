---
layout: container
name:  "quay.io/biocontainers/mudskipper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mudskipper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mudskipper/container.yaml"
updated_at: "2025-02-17 03:07:39.082509"
latest: "0.1.0--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/mudskipper"
aliases:
 - "mudskipper"
versions:
 - "0.1.0--h9f5acd7_1"
description: "singularity registry hpc automated addition for mudskipper"
config: {"url": "https://biocontainers.pro/tools/mudskipper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mudskipper", "latest": {"0.1.0--h9f5acd7_1": "sha256:44d752e96ea11a3033b580df81088ab75c0d908b04eda5e09427e97b750a8a59"}, "tags": {"0.1.0--h9f5acd7_1": "sha256:44d752e96ea11a3033b580df81088ab75c0d908b04eda5e09427e97b750a8a59"}, "docker": "quay.io/biocontainers/mudskipper", "aliases": {"mudskipper": "/usr/local/bin/mudskipper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mudskipper.
singularity registry hpc automated addition for mudskipper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mudskipper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mudskipper:0.1.0--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mudskipper/0.1.0--h9f5acd7_1
$ module help quay.io/biocontainers/mudskipper/0.1.0--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mudskipper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mudskipper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mudskipper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mudskipper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mudskipper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mudskipper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mudskipper

```bash
$ singularity exec <container> /usr/local/bin/mudskipper
$ podman run --it --rm --entrypoint /usr/local/bin/mudskipper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mudskipper   -v ${PWD} -w ${PWD} <container> -c " $@"
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