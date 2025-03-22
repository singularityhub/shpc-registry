---
layout: container
name:  "ghcr.io/autamus/argobots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/argobots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/argobots/container.yaml"
updated_at: "2025-03-22 03:46:20.449757"
latest: "1.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/argobots"

versions:
 - "1.1"
 - "latest"
description: "A lightweight runtime system that supports integrated computation and data movement with massive concurrency."
config: {"docker": "ghcr.io/autamus/argobots", "url": "https://github.com/orgs/autamus/packages/container/package/argobots", "maintainer": "@vsoch", "description": "A lightweight runtime system that supports integrated computation and data movement with massive concurrency.", "latest": {"1.1": "sha256:85bd765f4ea2ecc92afe71d7c12fd286d6c0814e060519d3be1d88f0cbb14021"}, "tags": {"1.1": "sha256:85bd765f4ea2ecc92afe71d7c12fd286d6c0814e060519d3be1d88f0cbb14021", "latest": "sha256:85bd765f4ea2ecc92afe71d7c12fd286d6c0814e060519d3be1d88f0cbb14021"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/argobots.
A lightweight runtime system that supports integrated computation and data movement with massive concurrency.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/argobots
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/argobots:1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/argobots/1.1
$ module help ghcr.io/autamus/argobots/1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### argobots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### argobots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### argobots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### argobots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### argobots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### argobots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### argobots

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