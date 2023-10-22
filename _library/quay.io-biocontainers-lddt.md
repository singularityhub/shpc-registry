---
layout: container
name:  "quay.io/biocontainers/lddt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lddt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lddt/container.yaml"
updated_at: "2023-10-22 02:29:03.555267"
latest: "2.2--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/lddt"
aliases:
 - "lddt"
versions:
 - "2.2--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for lddt"
config: {"url": "https://biocontainers.pro/tools/lddt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lddt", "latest": {"2.2--h9ee0642_0": "sha256:8f15a5d8edac35149aeddf173805abc0dcb81748bda9e675cafb6884471b28ca"}, "tags": {"2.2--h9ee0642_0": "sha256:8f15a5d8edac35149aeddf173805abc0dcb81748bda9e675cafb6884471b28ca"}, "docker": "quay.io/biocontainers/lddt", "aliases": {"lddt": "/usr/local/bin/lddt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lddt.
shpc-registry automated BioContainers addition for lddt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lddt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lddt:2.2--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lddt/2.2--h9ee0642_0
$ module help quay.io/biocontainers/lddt/2.2--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lddt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lddt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lddt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lddt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lddt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lddt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lddt

```bash
$ singularity exec <container> /usr/local/bin/lddt
$ podman run --it --rm --entrypoint /usr/local/bin/lddt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lddt   -v ${PWD} -w ${PWD} <container> -c " $@"
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