---
layout: container
name:  "quay.io/biocontainers/minialign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minialign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minialign/container.yaml"
updated_at: "2024-01-21 02:59:06.342293"
latest: "0.5.3--1"
container_url: "https://biocontainers.pro/tools/minialign"
aliases:
 - "minialign"
versions:
 - "0.5.3--1"
description: "shpc-registry automated BioContainers addition for minialign"
config: {"url": "https://biocontainers.pro/tools/minialign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minialign", "latest": {"0.5.3--1": "sha256:80fcc5ff9f4b49cda4e3dfa946a4a6c951382e12155d3e6c09f80ccf255e9f25"}, "tags": {"0.5.3--1": "sha256:80fcc5ff9f4b49cda4e3dfa946a4a6c951382e12155d3e6c09f80ccf255e9f25"}, "docker": "quay.io/biocontainers/minialign", "aliases": {"minialign": "/usr/local/bin/minialign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minialign.
shpc-registry automated BioContainers addition for minialign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minialign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minialign:0.5.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minialign/0.5.3--1
$ module help quay.io/biocontainers/minialign/0.5.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minialign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minialign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minialign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minialign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minialign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minialign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minialign

```bash
$ singularity exec <container> /usr/local/bin/minialign
$ podman run --it --rm --entrypoint /usr/local/bin/minialign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minialign   -v ${PWD} -w ${PWD} <container> -c " $@"
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