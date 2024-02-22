---
layout: container
name:  "vanessa/salad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/vanessa/salad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/vanessa/salad/container.yaml"
updated_at: "2024-02-22 03:34:27.008094"
latest: "latest"
container_url: "https://hub.docker.com/r/vanessa/salad"
aliases:
 - "salad"
versions:
 - "latest"
description: "A container all about fork and spoon puns."
config: {"docker": "vanessa/salad", "url": "https://hub.docker.com/r/vanessa/salad", "maintainer": "@vsoch", "description": "A container all about fork and spoon puns.", "filter": ["^(?!.*add_github-actions).*$"], "latest": {"latest": "sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db"}, "tags": {"latest": "sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db"}, "aliases": {"salad": "/code/salad"}, "docker_scripts": {"fork": "docker_fork.sh"}, "singularity_scripts": {"fork": "singularity_fork.sh"}, "env": {"maintainer": "vsoch"}}
---

This module is a singularity container wrapper for vanessa/salad.
A container all about fork and spoon puns.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install vanessa/salad
```

Or a specific version:

```bash
$ shpc install vanessa/salad:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load vanessa/salad/latest
$ module help vanessa/salad/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### salad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### salad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### salad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### salad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### salad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### salad-inspect-deffile:

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