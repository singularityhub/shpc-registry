---
layout: container
name:  "singularityhub/singularity-deploy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/singularityhub/singularity-deploy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/singularityhub/singularity-deploy/container.yaml"
updated_at: "2024-03-14 02:21:31.163303"
latest: "salad"
container_url: "https://github.com/singularityhub/singularity-deploy"
aliases:
 - "salad"
versions:
 - "salad"
description: "Example shpc container using Singularity Deploy, build and serve from GitHub releases."
config: {"gh": "singularityhub/singularity-deploy", "url": "https://github.com/singularityhub/singularity-deploy", "maintainer": "@vsoch", "description": "Example shpc container using Singularity Deploy, build and serve from GitHub releases.", "latest": {"salad": "0.0.12"}, "tags": {"salad": "0.0.12"}, "aliases": {"salad": "/code/salad"}}
---

This module is a singularity container wrapper for singularityhub/singularity-deploy.
Example shpc container using Singularity Deploy, build and serve from GitHub releases.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install singularityhub/singularity-deploy
```

Or a specific version:

```bash
$ shpc install singularityhub/singularity-deploy:salad
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load singularityhub/singularity-deploy/salad
$ module help singularityhub/singularity-deploy/salad
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### singularity-deploy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### singularity-deploy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### singularity-deploy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### singularity-deploy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### singularity-deploy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### singularity-deploy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### salad

```bash
$ singularity exec <container> /code/salad
$ podman run --it --rm --entrypoint /code/salad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /code/salad   -v ${PWD} -w ${PWD} <container> -c " $@"
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