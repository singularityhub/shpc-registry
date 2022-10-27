---
layout: container
name:  "quay.io/biocontainers/delegation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/delegation/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/delegation/container.yaml"
updated_at: "2022-10-27 00:35:40.694922"
latest: "1.1--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/delegation"

versions:
 - "1.1--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for delegation"
config: {"url": "https://biocontainers.pro/tools/delegation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for delegation", "latest": {"1.1--pyh864c0ab_1": "sha256:efa44a8df448ac74f2f550cff635ba3077f314156f5326719c7fb3b814ff6b3b"}, "tags": {"1.1--pyh864c0ab_1": "sha256:efa44a8df448ac74f2f550cff635ba3077f314156f5326719c7fb3b814ff6b3b"}, "docker": "quay.io/biocontainers/delegation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/delegation.
shpc-registry automated BioContainers addition for delegation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/delegation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/delegation:1.1--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/delegation/1.1--pyh864c0ab_1
$ module help quay.io/biocontainers/delegation/1.1--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### delegation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### delegation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### delegation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### delegation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### delegation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### delegation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### delegation

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