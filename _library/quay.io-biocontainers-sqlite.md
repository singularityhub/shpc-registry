---
layout: container
name:  "quay.io/biocontainers/sqlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sqlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sqlite/container.yaml"
updated_at: "2023-01-22 03:24:22.990365"
latest: "3.33.0"
container_url: "https://biocontainers.pro/tools/sqlite"
aliases:
 - "sqlite3"
versions:
 - "3.33.0"
description: "shpc-registry automated BioContainers addition for sqlite"
config: {"url": "https://biocontainers.pro/tools/sqlite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sqlite", "latest": {"3.33.0": "sha256:8d3aba438a721ce57ac824e1b726f5f9b6e2526b82c8dca38b3c2a07b5fb78e8"}, "tags": {"3.33.0": "sha256:8d3aba438a721ce57ac824e1b726f5f9b6e2526b82c8dca38b3c2a07b5fb78e8"}, "docker": "quay.io/biocontainers/sqlite", "aliases": {"sqlite3": "/usr/local/bin/sqlite3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sqlite.
shpc-registry automated BioContainers addition for sqlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sqlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sqlite:3.33.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sqlite/3.33.0
$ module help quay.io/biocontainers/sqlite/3.33.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sqlite3

```bash
$ singularity exec <container> /usr/local/bin/sqlite3
$ podman run --it --rm --entrypoint /usr/local/bin/sqlite3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlite3   -v ${PWD} -w ${PWD} <container> -c " $@"
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