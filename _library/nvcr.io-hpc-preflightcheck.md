---
layout: container
name:  "nvcr.io/hpc/preflightcheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/preflightcheck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/hpc/preflightcheck/container.yaml"
updated_at: "2025-08-21 06:07:58.553128"
latest: "20.11"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:preflightcheck"

versions:
 - "20.11"
description: "The Pre-Flight Check container verifies that the container runtime is setup correctly for GPUs and InfiniBand."
config: {"docker": "nvcr.io/hpc/preflightcheck", "latest": {"20.11": "sha256:8aba0b9dd1c724cd2973ff288cf056f0aae84c3c3ef9dbccddaf4771356cc93e"}, "tags": {"20.11": "sha256:8aba0b9dd1c724cd2973ff288cf056f0aae84c3c3ef9dbccddaf4771356cc93e"}, "filter": ["24*"], "maintainer": "@vsoch", "url": "https://ngc.nvidia.com/catalog/containers/hpc:preflightcheck", "description": "The Pre-Flight Check container verifies that the container runtime is setup correctly for GPUs and InfiniBand.", "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/hpc/preflightcheck.
The Pre-Flight Check container verifies that the container runtime is setup correctly for GPUs and InfiniBand.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/preflightcheck
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/preflightcheck:20.11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/preflightcheck/20.11
$ module help nvcr.io/hpc/preflightcheck/20.11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### preflightcheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### preflightcheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### preflightcheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### preflightcheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### preflightcheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### preflightcheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### preflightcheck

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