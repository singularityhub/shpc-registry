---
layout: container
name:  "quay.io/biocontainers/iced"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iced/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/iced/container.yaml"
updated_at: "2022-10-27 00:55:58.585991"
latest: "0.5.9--py37h9c5868f_0"
container_url: "https://biocontainers.pro/tools/iced"
aliases:
 - "ice"
versions:
 - "0.5.9--py37h9c5868f_0"
description: "shpc-registry automated BioContainers addition for iced"
config: {"url": "https://biocontainers.pro/tools/iced", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iced", "latest": {"0.5.9--py37h9c5868f_0": "sha256:57e789ead8ebd6aef0f697052a9c6a8d18151913245f01bb5ac085e7570da9c2"}, "tags": {"0.5.9--py37h9c5868f_0": "sha256:57e789ead8ebd6aef0f697052a9c6a8d18151913245f01bb5ac085e7570da9c2"}, "docker": "quay.io/biocontainers/iced", "aliases": {"ice": "/usr/local/bin/ice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iced.
shpc-registry automated BioContainers addition for iced
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iced
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iced:0.5.9--py37h9c5868f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iced/0.5.9--py37h9c5868f_0
$ module help quay.io/biocontainers/iced/0.5.9--py37h9c5868f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iced-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iced-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iced-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iced-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iced-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iced-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ice

```bash
$ singularity exec <container> /usr/local/bin/ice
$ podman run --it --rm --entrypoint /usr/local/bin/ice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ice   -v ${PWD} -w ${PWD} <container> -c " $@"
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