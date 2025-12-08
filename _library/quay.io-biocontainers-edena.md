---
layout: container
name:  "quay.io/biocontainers/edena"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/edena/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/edena/container.yaml"
updated_at: "2025-12-08 05:19:55.811540"
latest: "3.131028--h9948957_8"
container_url: "https://biocontainers.pro/tools/edena"
aliases:
 - "edena"
versions:
 - "3.131028--h9f5acd7_4"
 - "3.131028--h4ac6f70_6"
 - "3.131028--h9948957_7"
 - "3.131028--h9948957_8"
description: "shpc-registry automated BioContainers addition for edena"
config: {"url": "https://biocontainers.pro/tools/edena", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for edena", "latest": {"3.131028--h9948957_8": "sha256:7aaa8c4c8e7828aafe09e2642fb183bee9d74f86feb4cb526a08ed6b8e6df4e3"}, "tags": {"3.131028--h9f5acd7_4": "sha256:f93e665eab1c6db72ad08dd2dd35990b33c70010e890df878e548c0e48dd8064", "3.131028--h4ac6f70_6": "sha256:6f6f95fa9f7a169371b46b2def25b683e5714082d43bf9c3139fc5e4ddc81d9e", "3.131028--h9948957_7": "sha256:722f8b77845d9c44528f45b5062bbbdcdd9bbe766b1c0580faa98bd2e717c4b0", "3.131028--h9948957_8": "sha256:7aaa8c4c8e7828aafe09e2642fb183bee9d74f86feb4cb526a08ed6b8e6df4e3"}, "docker": "quay.io/biocontainers/edena", "aliases": {"edena": "/usr/local/bin/edena"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/edena.
shpc-registry automated BioContainers addition for edena
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/edena
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/edena:3.131028--h9948957_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/edena/3.131028--h9948957_8
$ module help quay.io/biocontainers/edena/3.131028--h9948957_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### edena-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### edena-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### edena-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### edena-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### edena-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### edena-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### edena

```bash
$ singularity exec <container> /usr/local/bin/edena
$ podman run --it --rm --entrypoint /usr/local/bin/edena   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edena   -v ${PWD} -w ${PWD} <container> -c " $@"
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