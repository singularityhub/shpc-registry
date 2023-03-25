---
layout: container
name:  "quay.io/biocontainers/gfaffix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfaffix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfaffix/container.yaml"
updated_at: "2023-03-25 02:41:22.863545"
latest: "0.1.4--hec16e2b_0"
container_url: "https://biocontainers.pro/tools/gfaffix"
aliases:
 - "gfaffix"
versions:
 - "0.1.4--hec16e2b_0"
description: "shpc-registry automated BioContainers addition for gfaffix"
config: {"url": "https://biocontainers.pro/tools/gfaffix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gfaffix", "latest": {"0.1.4--hec16e2b_0": "sha256:b501573c8e52d99a2a5c2bd31386e2a7b34160e51561829c7876378cba7d4607"}, "tags": {"0.1.4--hec16e2b_0": "sha256:b501573c8e52d99a2a5c2bd31386e2a7b34160e51561829c7876378cba7d4607"}, "docker": "quay.io/biocontainers/gfaffix", "aliases": {"gfaffix": "/usr/local/bin/gfaffix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfaffix.
shpc-registry automated BioContainers addition for gfaffix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfaffix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfaffix:0.1.4--hec16e2b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfaffix/0.1.4--hec16e2b_0
$ module help quay.io/biocontainers/gfaffix/0.1.4--hec16e2b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfaffix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfaffix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfaffix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfaffix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfaffix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfaffix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfaffix

```bash
$ singularity exec <container> /usr/local/bin/gfaffix
$ podman run --it --rm --entrypoint /usr/local/bin/gfaffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfaffix   -v ${PWD} -w ${PWD} <container> -c " $@"
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