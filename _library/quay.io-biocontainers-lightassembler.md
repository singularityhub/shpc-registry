---
layout: container
name:  "quay.io/biocontainers/lightassembler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lightassembler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lightassembler/container.yaml"
updated_at: "2024-10-30 02:55:26.469974"
latest: "1.0--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/lightassembler"
aliases:
 - "LightAssembler"
 - "libtoolize"
 - "libtool"
versions:
 - "1.0--hd03093a_3"
 - "1.0--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for lightassembler"
config: {"url": "https://biocontainers.pro/tools/lightassembler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lightassembler", "latest": {"1.0--hdcf5f25_5": "sha256:7c914decd36dc948c1d892745d24428cdee5bd8532d216515f9b7dda052546d0"}, "tags": {"1.0--hd03093a_3": "sha256:58f381db032a2492cf55c21fee6da846a34af825ce151aa0bcab99c9507abdc3", "1.0--hdcf5f25_5": "sha256:7c914decd36dc948c1d892745d24428cdee5bd8532d216515f9b7dda052546d0"}, "docker": "quay.io/biocontainers/lightassembler", "aliases": {"LightAssembler": "/usr/local/bin/LightAssembler", "libtoolize": "/usr/local/bin/libtoolize", "libtool": "/usr/local/bin/libtool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lightassembler.
shpc-registry automated BioContainers addition for lightassembler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lightassembler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lightassembler:1.0--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lightassembler/1.0--hdcf5f25_5
$ module help quay.io/biocontainers/lightassembler/1.0--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lightassembler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lightassembler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lightassembler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lightassembler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lightassembler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lightassembler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LightAssembler

```bash
$ singularity exec <container> /usr/local/bin/LightAssembler
$ podman run --it --rm --entrypoint /usr/local/bin/LightAssembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LightAssembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libtoolize

```bash
$ singularity exec <container> /usr/local/bin/libtoolize
$ podman run --it --rm --entrypoint /usr/local/bin/libtoolize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libtoolize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libtool

```bash
$ singularity exec <container> /usr/local/bin/libtool
$ podman run --it --rm --entrypoint /usr/local/bin/libtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libtool   -v ${PWD} -w ${PWD} <container> -c " $@"
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