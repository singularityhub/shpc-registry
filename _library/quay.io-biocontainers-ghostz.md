---
layout: container
name:  "quay.io/biocontainers/ghostz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghostz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ghostz/container.yaml"
updated_at: "2024-04-18 03:07:38.069478"
latest: "1.0.2--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/ghostz"
aliases:
 - "ghostz"
versions:
 - "1.0.2--h87f3376_3"
 - "1.0.2--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for ghostz"
config: {"url": "https://biocontainers.pro/tools/ghostz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghostz", "latest": {"1.0.2--hdbdd923_5": "sha256:867cf04129aa8984b62438f2d3d69a60b27ece38793255e1a5eb87565a411568"}, "tags": {"1.0.2--h87f3376_3": "sha256:57262b2b9c1baa903369459658733aa12c0f1a843c56199299587cfbbaf02460", "1.0.2--hdbdd923_5": "sha256:867cf04129aa8984b62438f2d3d69a60b27ece38793255e1a5eb87565a411568"}, "docker": "quay.io/biocontainers/ghostz", "aliases": {"ghostz": "/usr/local/bin/ghostz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghostz.
shpc-registry automated BioContainers addition for ghostz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghostz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghostz:1.0.2--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghostz/1.0.2--hdbdd923_5
$ module help quay.io/biocontainers/ghostz/1.0.2--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghostz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghostz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghostz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghostz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghostz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghostz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ghostz

```bash
$ singularity exec <container> /usr/local/bin/ghostz
$ podman run --it --rm --entrypoint /usr/local/bin/ghostz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghostz   -v ${PWD} -w ${PWD} <container> -c " $@"
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