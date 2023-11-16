---
layout: container
name:  "quay.io/biocontainers/prodigal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prodigal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prodigal/container.yaml"
updated_at: "2023-11-16 02:52:50.603568"
latest: "2.60--1"
container_url: "https://biocontainers.pro/tools/prodigal"
aliases:
 - "prodigal"
versions:
 - "2.60--1"
description: "shpc-registry automated BioContainers addition for prodigal"
config: {"url": "https://biocontainers.pro/tools/prodigal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prodigal", "latest": {"2.60--1": "sha256:7a5993ac64925613deda1b927219d5569fcdee9535f868067800a923485b489b"}, "tags": {"2.60--1": "sha256:7a5993ac64925613deda1b927219d5569fcdee9535f868067800a923485b489b"}, "docker": "quay.io/biocontainers/prodigal", "aliases": {"prodigal": "/usr/local/bin/prodigal"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prodigal.
shpc-registry automated BioContainers addition for prodigal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prodigal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prodigal:2.60--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prodigal/2.60--1
$ module help quay.io/biocontainers/prodigal/2.60--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prodigal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prodigal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prodigal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prodigal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
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