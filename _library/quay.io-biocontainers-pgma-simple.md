---
layout: container
name:  "quay.io/biocontainers/pgma-simple"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgma-simple/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgma-simple/container.yaml"
updated_at: "2023-05-30 03:13:13.169526"
latest: "0.1--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/pgma-simple"
aliases:
 - "pgma"
versions:
 - "0.1--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for pgma-simple"
config: {"url": "https://biocontainers.pro/tools/pgma-simple", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pgma-simple", "latest": {"0.1--h9f5acd7_4": "sha256:74a7dc6d1dd8df00486d19884583e58485a4302527a23086d8d8692a25b947e6"}, "tags": {"0.1--h9f5acd7_4": "sha256:74a7dc6d1dd8df00486d19884583e58485a4302527a23086d8d8692a25b947e6"}, "docker": "quay.io/biocontainers/pgma-simple", "aliases": {"pgma": "/usr/local/bin/pgma"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgma-simple.
shpc-registry automated BioContainers addition for pgma-simple
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgma-simple
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgma-simple:0.1--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgma-simple/0.1--h9f5acd7_4
$ module help quay.io/biocontainers/pgma-simple/0.1--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgma-simple-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgma-simple-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgma-simple-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgma-simple-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgma-simple-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgma-simple-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pgma

```bash
$ singularity exec <container> /usr/local/bin/pgma
$ podman run --it --rm --entrypoint /usr/local/bin/pgma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgma   -v ${PWD} -w ${PWD} <container> -c " $@"
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