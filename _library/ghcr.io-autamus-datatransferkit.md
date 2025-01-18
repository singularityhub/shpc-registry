---
layout: container
name:  "ghcr.io/autamus/datatransferkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/datatransferkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/datatransferkit/container.yaml"
updated_at: "2025-01-18 02:41:27.233343"
latest: "3.1.rc.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/datatransferkit"

versions:
 - "3.1.rc.2"
 - "latest"
description: "DataTransferKit is an open-source software library of parallel solution transfer services for multiphysics simulations"
config: {"docker": "ghcr.io/autamus/datatransferkit", "url": "https://github.com/orgs/autamus/packages/container/package/datatransferkit", "maintainer": "@vsoch", "description": "DataTransferKit is an open-source software library of parallel solution transfer services for multiphysics simulations", "latest": {"3.1.rc.2": "sha256:f3207ac76a9961c1768dbce234636a5c02ba6b1a495442d4027bccd00f18c1c7"}, "tags": {"3.1.rc.2": "sha256:f3207ac76a9961c1768dbce234636a5c02ba6b1a495442d4027bccd00f18c1c7", "latest": "sha256:f3207ac76a9961c1768dbce234636a5c02ba6b1a495442d4027bccd00f18c1c7"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/datatransferkit.
DataTransferKit is an open-source software library of parallel solution transfer services for multiphysics simulations
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/datatransferkit
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/datatransferkit:3.1.rc.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/datatransferkit/3.1.rc.2
$ module help ghcr.io/autamus/datatransferkit/3.1.rc.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### datatransferkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### datatransferkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### datatransferkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### datatransferkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### datatransferkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### datatransferkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### datatransferkit

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