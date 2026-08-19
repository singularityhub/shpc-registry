---
layout: container
name:  "quay.io/biocontainers/gxfkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gxfkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gxfkit/container.yaml"
updated_at: "2026-08-19 03:51:53.391737"
latest: "0.0.2--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/gxfkit"
aliases:
 - "gxfkit"
versions:
 - "0.0.1--hfa8f182_0"
 - "0.0.2--hfa8f182_0"
description: "singularity registry hpc automated addition for gxfkit"
config: {"url": "https://biocontainers.pro/tools/gxfkit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gxfkit", "latest": {"0.0.2--hfa8f182_0": "sha256:8c0f13b8baa3235d513a72cf9f26dd1a848727535e1cfbcc853c2617dd21fdfe"}, "tags": {"0.0.1--hfa8f182_0": "sha256:042441c7909b53a43194060e49d374a572bd243ebeb677ac8a8deee2394868d2", "0.0.2--hfa8f182_0": "sha256:8c0f13b8baa3235d513a72cf9f26dd1a848727535e1cfbcc853c2617dd21fdfe"}, "docker": "quay.io/biocontainers/gxfkit", "aliases": {"gxfkit": "/usr/local/bin/gxfkit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gxfkit.
singularity registry hpc automated addition for gxfkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gxfkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gxfkit:0.0.2--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gxfkit/0.0.2--hfa8f182_0
$ module help quay.io/biocontainers/gxfkit/0.0.2--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gxfkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gxfkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gxfkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gxfkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gxfkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gxfkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gxfkit

```bash
$ singularity exec <container> /usr/local/bin/gxfkit
$ podman run --it --rm --entrypoint /usr/local/bin/gxfkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gxfkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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