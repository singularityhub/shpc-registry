---
layout: container
name:  "quay.io/biocontainers/pypints"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pypints/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pypints/container.yaml"
updated_at: "2022-10-27 00:34:11.524647"
latest: "1.1.8--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pypints"
aliases:
 - "pints_boundary_extender"
 - "pints_caller"
 - "pints_normalizer"
 - "pints_visualizer"
versions:
 - "1.1.8--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for pypints"
config: {"url": "https://biocontainers.pro/tools/pypints", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pypints", "latest": {"1.1.8--pyh7cba7a3_0": "sha256:c2a0f88405540b7849707f7ed898c142eabadcb4fd666c45315c497a79fa6b44"}, "tags": {"1.1.8--pyh7cba7a3_0": "sha256:c2a0f88405540b7849707f7ed898c142eabadcb4fd666c45315c497a79fa6b44"}, "docker": "quay.io/biocontainers/pypints", "aliases": {"pints_boundary_extender": "/usr/local/bin/pints_boundary_extender", "pints_caller": "/usr/local/bin/pints_caller", "pints_normalizer": "/usr/local/bin/pints_normalizer", "pints_visualizer": "/usr/local/bin/pints_visualizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pypints.
shpc-registry automated BioContainers addition for pypints
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pypints
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pypints:1.1.8--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pypints/1.1.8--pyh7cba7a3_0
$ module help quay.io/biocontainers/pypints/1.1.8--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pypints-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pypints-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pypints-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pypints-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pypints-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pypints-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pints_boundary_extender

```bash
$ singularity exec <container> /usr/local/bin/pints_boundary_extender
$ podman run --it --rm --entrypoint /usr/local/bin/pints_boundary_extender   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pints_boundary_extender   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pints_caller

```bash
$ singularity exec <container> /usr/local/bin/pints_caller
$ podman run --it --rm --entrypoint /usr/local/bin/pints_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pints_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pints_normalizer

```bash
$ singularity exec <container> /usr/local/bin/pints_normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/pints_normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pints_normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pints_visualizer

```bash
$ singularity exec <container> /usr/local/bin/pints_visualizer
$ podman run --it --rm --entrypoint /usr/local/bin/pints_visualizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pints_visualizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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