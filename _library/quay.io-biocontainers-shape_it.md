---
layout: container
name:  "quay.io/biocontainers/shape_it"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shape_it/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/shape_it/container.yaml"
updated_at: "2022-10-27 00:42:05.771200"
latest: "1.0.1--h7d875b9_7"
container_url: "https://biocontainers.pro/tools/shape_it"
aliases:
 - "babel"
 - "obchiral"
 - "shape-it"
versions:
 - "1.0.1--h7d875b9_7"
description: "shpc-registry automated BioContainers addition for shape_it"
config: {"url": "https://biocontainers.pro/tools/shape_it", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shape_it", "latest": {"1.0.1--h7d875b9_7": "sha256:1cdb5da1c631d63dfab87013f1d5d9329472d997a274a6c958083d0fe5158848"}, "tags": {"1.0.1--h7d875b9_7": "sha256:1cdb5da1c631d63dfab87013f1d5d9329472d997a274a6c958083d0fe5158848"}, "docker": "quay.io/biocontainers/shape_it", "aliases": {"babel": "/usr/local/bin/babel", "obchiral": "/usr/local/bin/obchiral", "shape-it": "/usr/local/bin/shape-it"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shape_it.
shpc-registry automated BioContainers addition for shape_it
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shape_it
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shape_it:1.0.1--h7d875b9_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shape_it/1.0.1--h7d875b9_7
$ module help quay.io/biocontainers/shape_it/1.0.1--h7d875b9_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shape_it-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shape_it-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shape_it-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shape_it-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shape_it-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shape_it-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### babel

```bash
$ singularity exec <container> /usr/local/bin/babel
$ podman run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/babel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obchiral

```bash
$ singularity exec <container> /usr/local/bin/obchiral
$ podman run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/obchiral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shape-it

```bash
$ singularity exec <container> /usr/local/bin/shape-it
$ podman run --it --rm --entrypoint /usr/local/bin/shape-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shape-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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