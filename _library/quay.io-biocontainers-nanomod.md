---
layout: container
name:  "quay.io/biocontainers/nanomod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanomod/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanomod/container.yaml"
updated_at: "2022-10-27 00:40:14.095286"
latest: "0.2.2--py_0"
container_url: "https://biocontainers.pro/tools/nanomod"
aliases:
 - "NanoMod.py"
versions:
 - "0.2.2--py_0"
description: "shpc-registry automated BioContainers addition for nanomod"
config: {"url": "https://biocontainers.pro/tools/nanomod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanomod", "latest": {"0.2.2--py_0": "sha256:551e6aab5cf1b0815e02cc60f16bd911ae8c1b025d8c3bc3b91db73e496b2e61"}, "tags": {"0.2.2--py_0": "sha256:551e6aab5cf1b0815e02cc60f16bd911ae8c1b025d8c3bc3b91db73e496b2e61"}, "docker": "quay.io/biocontainers/nanomod", "aliases": {"NanoMod.py": "/usr/local/bin/NanoMod.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanomod.
shpc-registry automated BioContainers addition for nanomod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanomod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanomod:0.2.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanomod/0.2.2--py_0
$ module help quay.io/biocontainers/nanomod/0.2.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanomod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanomod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanomod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanomod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanomod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanomod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoMod.py

```bash
$ singularity exec <container> /usr/local/bin/NanoMod.py
$ podman run --it --rm --entrypoint /usr/local/bin/NanoMod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoMod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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