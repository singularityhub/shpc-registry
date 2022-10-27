---
layout: container
name:  "quay.io/biocontainers/ghostscript"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghostscript/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ghostscript/container.yaml"
updated_at: "2022-10-27 00:41:13.963697"
latest: "9.18--1"
container_url: "https://biocontainers.pro/tools/ghostscript"
aliases:
 - "font2c"
 - "wftopfa"
versions:
 - "9.18--1"
description: "shpc-registry automated BioContainers addition for ghostscript"
config: {"url": "https://biocontainers.pro/tools/ghostscript", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghostscript", "latest": {"9.18--1": "sha256:df842762499bed8c87943cd7f1b957cdb4b9e9381ab0a8feee1103c21309a888"}, "tags": {"9.18--1": "sha256:df842762499bed8c87943cd7f1b957cdb4b9e9381ab0a8feee1103c21309a888"}, "docker": "quay.io/biocontainers/ghostscript", "aliases": {"font2c": "/usr/local/bin/font2c", "wftopfa": "/usr/local/bin/wftopfa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghostscript.
shpc-registry automated BioContainers addition for ghostscript
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghostscript
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghostscript:9.18--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghostscript/9.18--1
$ module help quay.io/biocontainers/ghostscript/9.18--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghostscript-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghostscript-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghostscript-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghostscript-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghostscript-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghostscript-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### font2c

```bash
$ singularity exec <container> /usr/local/bin/font2c
$ podman run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/font2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wftopfa

```bash
$ singularity exec <container> /usr/local/bin/wftopfa
$ podman run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wftopfa   -v ${PWD} -w ${PWD} <container> -c " $@"
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