---
layout: container
name:  "quay.io/biocontainers/python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python/container.yaml"
updated_at: "2024-04-01 02:48:03.178680"
latest: "3.12"
container_url: "https://biocontainers.pro/tools/python"

versions:
 - "3.9--1"
 - "3"
 - "3.10"
 - "3.9"
 - "3.12"
description: "shpc-registry automated BioContainers addition for python"
config: {"url": "https://biocontainers.pro/tools/python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python", "latest": {"3.12": "sha256:29fccb317d61a9d09ecf432f63bfea512b98f0f3bc3764dc65fbdbc0f02473b5"}, "tags": {"3.9--1": "sha256:d97d2b329b4e44d2e07a9737ba348b185d6a47f34fba0ef301d44d11669cac60", "3": "sha256:c2b3b7137c6d44ec29dd500e87c0ea5e13e3d537eebb0abfb733ecdd5d2455ee", "3.10": "sha256:f6b44640f06e8265ebf5ce85ca12cea53af110c188d6b4acf5f59887c24abb8f", "3.9": "sha256:c6b961c4c7bbfedddc8bbce9431ce550621c4fe526bb0f11a73c314507ec730d", "3.12": "sha256:29fccb317d61a9d09ecf432f63bfea512b98f0f3bc3764dc65fbdbc0f02473b5"}, "docker": "quay.io/biocontainers/python"}
---

This module is a singularity container wrapper for quay.io/biocontainers/python.
shpc-registry automated BioContainers addition for python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python:3.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python/3.12
$ module help quay.io/biocontainers/python/3.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### python

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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