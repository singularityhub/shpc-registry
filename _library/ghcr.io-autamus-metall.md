---
layout: container
name:  "ghcr.io/autamus/metall"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/metall/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/metall/container.yaml"
updated_at: "2025-08-10 04:38:08.029536"
latest: "0.21"
container_url: "https://github.com/orgs/autamus/packages/container/package/metall"

versions:
 - "0.13"
 - "0.15"
 - "0.16"
 - "0.17"
 - "0.18"
 - "latest"
 - "0.21"
description: "A Persistent Memory Allocator For Data-Centric Analytics"
config: {"docker": "ghcr.io/autamus/metall", "url": "https://github.com/orgs/autamus/packages/container/package/metall", "maintainer": "@vsoch", "description": "A Persistent Memory Allocator For Data-Centric Analytics", "latest": {"0.21": "sha256:e272b8485e7fd86017e706363f814cf15107c15f01c5a56800ce100e8694bd5a"}, "tags": {"0.13": "sha256:38b265f335af401fb19f8839cb923e5d7236da7d5c8e88571180ac846ed4674b", "0.15": "sha256:e38dee252c235ad3a894fc15fbd7c141dfd3c91004aeb1118fc80c18ab46517e", "0.16": "sha256:982b182bbaabb05ca2d0e32e5fa3bfda3134a76e92dc39f383c6c544f5d7ed5d", "0.17": "sha256:4e9599ba5172626c91c4bf16cc0fb855da2ee807f23719a7fe07dbf5c9afde69", "0.18": "sha256:4d4e8c403c58ebcd04c22910d8cf4ddbc3b3008e373f2c1706a1f69399969187", "latest": "sha256:e272b8485e7fd86017e706363f814cf15107c15f01c5a56800ce100e8694bd5a", "0.21": "sha256:e272b8485e7fd86017e706363f814cf15107c15f01c5a56800ce100e8694bd5a"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/metall.
A Persistent Memory Allocator For Data-Centric Analytics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/metall
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/metall:0.21
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/metall/0.21
$ module help ghcr.io/autamus/metall/0.21
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metall-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metall-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metall-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metall-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metall-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metall-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### metall

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