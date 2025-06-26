---
layout: container
name:  "ghcr.io/autamus/superlu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/superlu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/superlu/container.yaml"
updated_at: "2025-06-26 03:21:17.561767"
latest: "5.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/superlu"

versions:
 - "5.2.2"
 - "5.3.0"
 - "latest"
description: "SuperLU is a general purpose library for the direct solution of large, sparse, nonsymmetric systems of linear equations on high performance machines."
config: {"docker": "ghcr.io/autamus/superlu", "url": "https://github.com/orgs/autamus/packages/container/package/superlu", "maintainer": "@vsoch", "description": "SuperLU is a general purpose library for the direct solution of large, sparse, nonsymmetric systems of linear equations on high performance machines.", "latest": {"5.3.0": "sha256:5d151dc6b33254970a71698104ba61648eb3159ed0b4cce8d2f1c13d5f2c011f"}, "tags": {"5.2.2": "sha256:31e2968aa8503840fceae8c81c5b7b197483b1a787d6a9488535ddd511cc787d", "5.3.0": "sha256:5d151dc6b33254970a71698104ba61648eb3159ed0b4cce8d2f1c13d5f2c011f", "latest": "sha256:5d151dc6b33254970a71698104ba61648eb3159ed0b4cce8d2f1c13d5f2c011f"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/superlu.
SuperLU is a general purpose library for the direct solution of large, sparse, nonsymmetric systems of linear equations on high performance machines.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/superlu
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/superlu:5.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/superlu/5.3.0
$ module help ghcr.io/autamus/superlu/5.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### superlu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### superlu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### superlu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### superlu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### superlu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### superlu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### superlu

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