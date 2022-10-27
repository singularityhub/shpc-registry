---
layout: container
name:  "quay.io/biocontainers/scalop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scalop/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scalop/container.yaml"
updated_at: "2022-10-27 00:51:17.845286"
latest: "2021.01.27--py_0"
container_url: "https://biocontainers.pro/tools/scalop"
aliases:
 - "SCALOP"
versions:
 - "2021.01.27--py_0"
description: "shpc-registry automated BioContainers addition for scalop"
config: {"url": "https://biocontainers.pro/tools/scalop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scalop", "latest": {"2021.01.27--py_0": "sha256:018e757277fe816bacdc7b7fc91f0cc8a8277d70246b60a69624ba855a2d9e2a"}, "tags": {"2021.01.27--py_0": "sha256:018e757277fe816bacdc7b7fc91f0cc8a8277d70246b60a69624ba855a2d9e2a"}, "docker": "quay.io/biocontainers/scalop", "aliases": {"SCALOP": "/usr/local/bin/SCALOP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scalop.
shpc-registry automated BioContainers addition for scalop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scalop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scalop:2021.01.27--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scalop/2021.01.27--py_0
$ module help quay.io/biocontainers/scalop/2021.01.27--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scalop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scalop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scalop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scalop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scalop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scalop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SCALOP

```bash
$ singularity exec <container> /usr/local/bin/SCALOP
$ podman run --it --rm --entrypoint /usr/local/bin/SCALOP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SCALOP   -v ${PWD} -w ${PWD} <container> -c " $@"
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