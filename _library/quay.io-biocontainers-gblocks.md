---
layout: container
name:  "quay.io/biocontainers/gblocks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gblocks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gblocks/container.yaml"
updated_at: "2025-04-23 03:16:24.698490"
latest: "0.91b--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/gblocks"
aliases:
 - "Gblocks"
versions:
 - "0.91b--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for gblocks"
config: {"url": "https://biocontainers.pro/tools/gblocks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gblocks", "latest": {"0.91b--h9ee0642_2": "sha256:11d9f0b38fcc98cd73cf1e6da0d9f8f9b55130f97cdffaf5161683ecebfbce50"}, "tags": {"0.91b--h9ee0642_2": "sha256:11d9f0b38fcc98cd73cf1e6da0d9f8f9b55130f97cdffaf5161683ecebfbce50"}, "docker": "quay.io/biocontainers/gblocks", "aliases": {"Gblocks": "/usr/local/bin/Gblocks"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gblocks.
shpc-registry automated BioContainers addition for gblocks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gblocks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gblocks:0.91b--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gblocks/0.91b--h9ee0642_2
$ module help quay.io/biocontainers/gblocks/0.91b--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gblocks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gblocks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gblocks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gblocks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gblocks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gblocks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gblocks

```bash
$ singularity exec <container> /usr/local/bin/Gblocks
$ podman run --it --rm --entrypoint /usr/local/bin/Gblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gblocks   -v ${PWD} -w ${PWD} <container> -c " $@"
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