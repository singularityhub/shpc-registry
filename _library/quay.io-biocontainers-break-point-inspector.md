---
layout: container
name:  "quay.io/biocontainers/break-point-inspector"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/break-point-inspector/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/break-point-inspector/container.yaml"
updated_at: "2022-10-27 00:48:12.304761"
latest: "1.5--1"
container_url: "https://biocontainers.pro/tools/break-point-inspector"
aliases:
 - "break-point-inspector"
versions:
 - "1.5--1"
description: "shpc-registry automated BioContainers addition for break-point-inspector"
config: {"url": "https://biocontainers.pro/tools/break-point-inspector", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for break-point-inspector", "latest": {"1.5--1": "sha256:8b9e82642f820e23986c65c77c3f2d3137d4796570508679375713175a74ee6b"}, "tags": {"1.5--1": "sha256:8b9e82642f820e23986c65c77c3f2d3137d4796570508679375713175a74ee6b"}, "docker": "quay.io/biocontainers/break-point-inspector", "aliases": {"break-point-inspector": "/usr/local/bin/break-point-inspector"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/break-point-inspector.
shpc-registry automated BioContainers addition for break-point-inspector
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/break-point-inspector
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/break-point-inspector:1.5--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/break-point-inspector/1.5--1
$ module help quay.io/biocontainers/break-point-inspector/1.5--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### break-point-inspector-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### break-point-inspector-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### break-point-inspector-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### break-point-inspector-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### break-point-inspector-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### break-point-inspector-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### break-point-inspector

```bash
$ singularity exec <container> /usr/local/bin/break-point-inspector
$ podman run --it --rm --entrypoint /usr/local/bin/break-point-inspector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/break-point-inspector   -v ${PWD} -w ${PWD} <container> -c " $@"
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