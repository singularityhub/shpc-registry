---
layout: container
name:  "ghcr.io/autamus/slepc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/slepc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/slepc/container.yaml"
updated_at: "2025-09-21 03:09:38.572385"
latest: "3.18.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/slepc"

versions:
 - "3.15.1"
 - "3.16.0"
 - "3.16.1"
 - "3.15.2"
 - "latest"
 - "3.18.1"
description: "Scalable Library for Eigenvalue Problem Computations."
config: {"docker": "ghcr.io/autamus/slepc", "url": "https://github.com/orgs/autamus/packages/container/package/slepc", "maintainer": "@vsoch", "description": "Scalable Library for Eigenvalue Problem Computations.", "latest": {"3.18.1": "sha256:a9d14dd173afaf00126e8f04058ed23661f588e05d9bf39d69f60705e222f158"}, "tags": {"3.15.1": "sha256:811d519414a4336d65ff4373cc9e0177deecd493702c7b32e5f08b3e91846047", "3.16.0": "sha256:43057b8923b8b15f7f365ae41b1859efd1e9718eee569fd6417f387a5a5a2a89", "3.16.1": "sha256:996170bda838c208b42d8c97fe3d5003b125802bf94e952476ab871bc1c5958a", "3.15.2": "sha256:94dcc33b55e6e5e1ab85eea811ed1096c3e822866689821549561b81665fb4fd", "latest": "sha256:a9d14dd173afaf00126e8f04058ed23661f588e05d9bf39d69f60705e222f158", "3.18.1": "sha256:a9d14dd173afaf00126e8f04058ed23661f588e05d9bf39d69f60705e222f158"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/slepc.
Scalable Library for Eigenvalue Problem Computations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/slepc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/slepc:3.18.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/slepc/3.18.1
$ module help ghcr.io/autamus/slepc/3.18.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slepc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slepc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slepc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slepc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slepc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slepc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### slepc

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