---
layout: container
name:  "ghcr.io/autamus/alps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/alps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/alps/container.yaml"
updated_at: "2025-10-10 03:02:49.986962"
latest: "2.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/alps"
aliases:
 - "alpspython"
versions:
 - "2.3.0"
 - "latest"
description: "Algorithms and Libraries for Physics Simulations."
config: {"docker": "ghcr.io/autamus/alps", "url": "https://github.com/orgs/autamus/packages/container/package/alps", "maintainer": "@vsoch", "description": "Algorithms and Libraries for Physics Simulations.", "latest": {"2.3.0": "sha256:475f8c97e26c19750dbfa005169a8b3dcb080075fc4e1280c5914efe3dbb2214"}, "tags": {"2.3.0": "sha256:475f8c97e26c19750dbfa005169a8b3dcb080075fc4e1280c5914efe3dbb2214", "latest": "sha256:475f8c97e26c19750dbfa005169a8b3dcb080075fc4e1280c5914efe3dbb2214"}, "aliases": {"alpspython": "/opt/view/bin/alpspython"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/alps.
Algorithms and Libraries for Physics Simulations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/alps
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/alps:2.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/alps/2.3.0
$ module help ghcr.io/autamus/alps/2.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alpspython

```bash
$ singularity exec <container> /opt/view/bin/alpspython
$ podman run --it --rm --entrypoint /opt/view/bin/alpspython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/alpspython   -v ${PWD} -w ${PWD} <container> -c " $@"
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