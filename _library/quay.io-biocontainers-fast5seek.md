---
layout: container
name:  "quay.io/biocontainers/fast5seek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fast5seek/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fast5seek/container.yaml"
updated_at: "2022-10-27 00:59:11.648408"
latest: "0.1.1--py_1"
container_url: "https://biocontainers.pro/tools/fast5seek"
aliases:
 - "fast5seek"
versions:
 - "0.1.1--py_1"
description: "shpc-registry automated BioContainers addition for fast5seek"
config: {"url": "https://biocontainers.pro/tools/fast5seek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fast5seek", "latest": {"0.1.1--py_1": "sha256:54d1f835aadd275e297a2e6a6403721dfcf88e26d1d087f60bed0060fc32725c"}, "tags": {"0.1.1--py_1": "sha256:54d1f835aadd275e297a2e6a6403721dfcf88e26d1d087f60bed0060fc32725c"}, "docker": "quay.io/biocontainers/fast5seek", "aliases": {"fast5seek": "/usr/local/bin/fast5seek"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fast5seek.
shpc-registry automated BioContainers addition for fast5seek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fast5seek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fast5seek:0.1.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fast5seek/0.1.1--py_1
$ module help quay.io/biocontainers/fast5seek/0.1.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fast5seek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fast5seek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fast5seek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fast5seek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fast5seek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fast5seek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fast5seek

```bash
$ singularity exec <container> /usr/local/bin/fast5seek
$ podman run --it --rm --entrypoint /usr/local/bin/fast5seek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5seek   -v ${PWD} -w ${PWD} <container> -c " $@"
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