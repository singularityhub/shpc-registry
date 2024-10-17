---
layout: container
name:  "quay.io/biocontainers/involucro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/involucro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/involucro/container.yaml"
updated_at: "2024-10-17 18:38:13.738850"
latest: "1.1.2--he881be0_4"
container_url: "https://biocontainers.pro/tools/involucro"
aliases:
 - "involucro"
versions:
 - "1.1.2--he881be0_3"
 - "1.1.2--he881be0_4"
description: "shpc-registry automated BioContainers addition for involucro"
config: {"url": "https://biocontainers.pro/tools/involucro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for involucro", "latest": {"1.1.2--he881be0_4": "sha256:f2406f47b603239a259ee1c27c438062357883638a515ce6f51388588eeb967b"}, "tags": {"1.1.2--he881be0_3": "sha256:f05e70162e3811b9173e4c7536003a4bdb13135e9691675cb071b97d2a579abf", "1.1.2--he881be0_4": "sha256:f2406f47b603239a259ee1c27c438062357883638a515ce6f51388588eeb967b"}, "docker": "quay.io/biocontainers/involucro", "aliases": {"involucro": "/usr/local/bin/involucro"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/involucro.
shpc-registry automated BioContainers addition for involucro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/involucro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/involucro:1.1.2--he881be0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/involucro/1.1.2--he881be0_4
$ module help quay.io/biocontainers/involucro/1.1.2--he881be0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### involucro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### involucro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### involucro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### involucro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### involucro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### involucro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### involucro

```bash
$ singularity exec <container> /usr/local/bin/involucro
$ podman run --it --rm --entrypoint /usr/local/bin/involucro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/involucro   -v ${PWD} -w ${PWD} <container> -c " $@"
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