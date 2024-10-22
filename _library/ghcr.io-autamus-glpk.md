---
layout: container
name:  "ghcr.io/autamus/glpk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/glpk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/glpk/container.yaml"
updated_at: "2024-10-22 02:53:21.859685"
latest: "4.65"
container_url: "https://github.com/orgs/autamus/packages/container/package/glpk"
aliases:
 - "glpsol"
versions:
 - "4.65"
 - "latest"
description: "The GLPK package is a set of routines written in ANSI C and organized in the form of a callable library. This package is intended for solving large-scale linear programming (LP), mixed integer linear programming (MIP), and other related problems."
config: {"docker": "ghcr.io/autamus/glpk", "url": "https://github.com/orgs/autamus/packages/container/package/glpk", "maintainer": "@vsoch", "description": "The GLPK package is a set of routines written in ANSI C and organized in the form of a callable library. This package is intended for solving large-scale linear programming (LP), mixed integer linear programming (MIP), and other related problems.", "latest": {"4.65": "sha256:76c79d26c63d0d5f084b5ddf792f12894822779886953df37c0f83f6fbe154fa"}, "tags": {"4.65": "sha256:76c79d26c63d0d5f084b5ddf792f12894822779886953df37c0f83f6fbe154fa", "latest": "sha256:76c79d26c63d0d5f084b5ddf792f12894822779886953df37c0f83f6fbe154fa"}, "aliases": {"glpsol": "/opt/view/bin/glpsol"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/glpk.
The GLPK package is a set of routines written in ANSI C and organized in the form of a callable library. This package is intended for solving large-scale linear programming (LP), mixed integer linear programming (MIP), and other related problems.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/glpk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/glpk:4.65
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/glpk/4.65
$ module help ghcr.io/autamus/glpk/4.65
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### glpk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### glpk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### glpk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### glpk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### glpk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### glpk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /opt/view/bin/glpsol
$ podman run --it --rm --entrypoint /opt/view/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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