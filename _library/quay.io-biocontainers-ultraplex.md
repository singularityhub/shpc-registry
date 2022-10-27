---
layout: container
name:  "quay.io/biocontainers/ultraplex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultraplex/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ultraplex/container.yaml"
updated_at: "2022-10-27 00:52:59.162221"
latest: "1.2.5--py38hbff2b2d_1"
container_url: "https://biocontainers.pro/tools/ultraplex"
aliases:
 - "ultraplex"
versions:
 - "1.2.5--py38hbff2b2d_1"
description: "shpc-registry automated BioContainers addition for ultraplex"
config: {"url": "https://biocontainers.pro/tools/ultraplex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultraplex", "latest": {"1.2.5--py38hbff2b2d_1": "sha256:ddbad5d727fc973a41af1ea912875d0d5dae098ced96529579f0f9d467b14ec6"}, "tags": {"1.2.5--py38hbff2b2d_1": "sha256:ddbad5d727fc973a41af1ea912875d0d5dae098ced96529579f0f9d467b14ec6"}, "docker": "quay.io/biocontainers/ultraplex", "aliases": {"ultraplex": "/usr/local/bin/ultraplex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultraplex.
shpc-registry automated BioContainers addition for ultraplex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultraplex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultraplex:1.2.5--py38hbff2b2d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultraplex/1.2.5--py38hbff2b2d_1
$ module help quay.io/biocontainers/ultraplex/1.2.5--py38hbff2b2d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultraplex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultraplex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultraplex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultraplex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultraplex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultraplex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ultraplex

```bash
$ singularity exec <container> /usr/local/bin/ultraplex
$ podman run --it --rm --entrypoint /usr/local/bin/ultraplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ultraplex   -v ${PWD} -w ${PWD} <container> -c " $@"
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