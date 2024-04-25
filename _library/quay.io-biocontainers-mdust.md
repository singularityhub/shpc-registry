---
layout: container
name:  "quay.io/biocontainers/mdust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mdust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mdust/container.yaml"
updated_at: "2024-04-25 03:05:18.625425"
latest: "2006.10.17--h031d066_6"
container_url: "https://biocontainers.pro/tools/mdust"
aliases:
 - "mdust"
versions:
 - "2006.10.17--hec16e2b_4"
 - "2006.10.17--h031d066_6"
description: "shpc-registry automated BioContainers addition for mdust"
config: {"url": "https://biocontainers.pro/tools/mdust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mdust", "latest": {"2006.10.17--h031d066_6": "sha256:e3dbeb026f83c40d550c41db16c0c6c55617f67edac54cc488ebd173e1b2d1e5"}, "tags": {"2006.10.17--hec16e2b_4": "sha256:6a238cb90621acd3a08c738229cd7d47361bf6350f368b7a494e0421d55d795d", "2006.10.17--h031d066_6": "sha256:e3dbeb026f83c40d550c41db16c0c6c55617f67edac54cc488ebd173e1b2d1e5"}, "docker": "quay.io/biocontainers/mdust", "aliases": {"mdust": "/usr/local/bin/mdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mdust.
shpc-registry automated BioContainers addition for mdust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mdust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mdust:2006.10.17--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mdust/2006.10.17--h031d066_6
$ module help quay.io/biocontainers/mdust/2006.10.17--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mdust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mdust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mdust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mdust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mdust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mdust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mdust

```bash
$ singularity exec <container> /usr/local/bin/mdust
$ podman run --it --rm --entrypoint /usr/local/bin/mdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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