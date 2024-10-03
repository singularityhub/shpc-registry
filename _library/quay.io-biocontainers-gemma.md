---
layout: container
name:  "quay.io/biocontainers/gemma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gemma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gemma/container.yaml"
updated_at: "2024-10-03 03:45:32.445761"
latest: "0.98.3--hb4ccc14_0"
container_url: "https://biocontainers.pro/tools/gemma"
aliases:
 - "gemma"
versions:
 - "0.98.3--hb4ccc14_0"
description: "shpc-registry automated BioContainers addition for gemma"
config: {"url": "https://biocontainers.pro/tools/gemma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gemma", "latest": {"0.98.3--hb4ccc14_0": "sha256:a4dc7b706d43d76790238b0d747cfb59161172eef354976847780181d6a09304"}, "tags": {"0.98.3--hb4ccc14_0": "sha256:a4dc7b706d43d76790238b0d747cfb59161172eef354976847780181d6a09304"}, "docker": "quay.io/biocontainers/gemma", "aliases": {"gemma": "/usr/local/bin/gemma"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gemma.
shpc-registry automated BioContainers addition for gemma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gemma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gemma:0.98.3--hb4ccc14_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gemma/0.98.3--hb4ccc14_0
$ module help quay.io/biocontainers/gemma/0.98.3--hb4ccc14_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gemma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gemma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gemma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gemma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gemma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gemma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gemma

```bash
$ singularity exec <container> /usr/local/bin/gemma
$ podman run --it --rm --entrypoint /usr/local/bin/gemma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gemma   -v ${PWD} -w ${PWD} <container> -c " $@"
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