---
layout: container
name:  "quay.io/biocontainers/libarbdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libarbdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libarbdb/container.yaml"
updated_at: "2025-05-15 03:45:39.048831"
latest: "6.0.6--haa8b8d8_8"
container_url: "https://biocontainers.pro/tools/libarbdb"
aliases:
 - "gio-launch-desktop"
versions:
 - "6.0.6--haa8b8d8_8"
description: "shpc-registry automated BioContainers addition for libarbdb"
config: {"url": "https://biocontainers.pro/tools/libarbdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libarbdb", "latest": {"6.0.6--haa8b8d8_8": "sha256:62af2b094b57cfac80c186b2b18df7f5b74d0202a023a39db6b97c3ee3fd2c14"}, "tags": {"6.0.6--haa8b8d8_8": "sha256:62af2b094b57cfac80c186b2b18df7f5b74d0202a023a39db6b97c3ee3fd2c14"}, "docker": "quay.io/biocontainers/libarbdb", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/libarbdb.
shpc-registry automated BioContainers addition for libarbdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libarbdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libarbdb:6.0.6--haa8b8d8_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libarbdb/6.0.6--haa8b8d8_8
$ module help quay.io/biocontainers/libarbdb/6.0.6--haa8b8d8_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libarbdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libarbdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libarbdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libarbdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libarbdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libarbdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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