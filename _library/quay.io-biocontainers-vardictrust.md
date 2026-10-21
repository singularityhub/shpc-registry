---
layout: container
name:  "quay.io/biocontainers/vardictrust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vardictrust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vardictrust/container.yaml"
updated_at: "2026-10-21 08:08:12.816869"
latest: "1.0.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/vardictrust"
aliases:
 - "vardictrust"
versions:
 - "1.0.0--hfa8f182_0"
description: "singularity registry hpc automated addition for vardictrust"
config: {"url": "https://biocontainers.pro/tools/vardictrust", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vardictrust", "latest": {"1.0.0--hfa8f182_0": "sha256:b7f4c0615eaf3875ead8f531ea84277924b3610d823342145b3d483c6defdc01"}, "tags": {"1.0.0--hfa8f182_0": "sha256:b7f4c0615eaf3875ead8f531ea84277924b3610d823342145b3d483c6defdc01"}, "docker": "quay.io/biocontainers/vardictrust", "aliases": {"vardictrust": "/usr/local/bin/vardictrust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vardictrust.
singularity registry hpc automated addition for vardictrust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vardictrust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vardictrust:1.0.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vardictrust/1.0.0--hfa8f182_0
$ module help quay.io/biocontainers/vardictrust/1.0.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vardictrust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vardictrust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vardictrust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vardictrust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vardictrust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vardictrust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vardictrust

```bash
$ singularity exec <container> /usr/local/bin/vardictrust
$ podman run --it --rm --entrypoint /usr/local/bin/vardictrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vardictrust   -v ${PWD} -w ${PWD} <container> -c " $@"
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