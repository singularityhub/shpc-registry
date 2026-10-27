---
layout: container
name:  "quay.io/biocontainers/fastnlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastnlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastnlr/container.yaml"
updated_at: "2026-10-27 07:44:52.102517"
latest: "1.4.1--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/fastnlr"
aliases:
 - "fastnlr"
versions:
 - "1.4.1--hfa8f182_0"
description: "singularity registry hpc automated addition for fastnlr"
config: {"url": "https://biocontainers.pro/tools/fastnlr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastnlr", "latest": {"1.4.1--hfa8f182_0": "sha256:39aa4026da4f2eb79029436b30a8b497b2b78df0919c1e96754765eb14e6b91b"}, "tags": {"1.4.1--hfa8f182_0": "sha256:39aa4026da4f2eb79029436b30a8b497b2b78df0919c1e96754765eb14e6b91b"}, "docker": "quay.io/biocontainers/fastnlr", "aliases": {"fastnlr": "/usr/local/bin/fastnlr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastnlr.
singularity registry hpc automated addition for fastnlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastnlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastnlr:1.4.1--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastnlr/1.4.1--hfa8f182_0
$ module help quay.io/biocontainers/fastnlr/1.4.1--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastnlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastnlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastnlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastnlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastnlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastnlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastnlr

```bash
$ singularity exec <container> /usr/local/bin/fastnlr
$ podman run --it --rm --entrypoint /usr/local/bin/fastnlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastnlr   -v ${PWD} -w ${PWD} <container> -c " $@"
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