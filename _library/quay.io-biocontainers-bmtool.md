---
layout: container
name:  "quay.io/biocontainers/bmtool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bmtool/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bmtool/container.yaml"
updated_at: "2024-12-15 03:36:08.773012"
latest: "3.101--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/bmtool"
aliases:
 - "bmtool"
versions:
 - "3.101--he1b5a44_3"
 - "3.101--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for bmtool"
config: {"url": "https://biocontainers.pro/tools/bmtool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bmtool", "latest": {"3.101--hdbdd923_5": "sha256:7ab31b3ca0b9f652eeead87959a30169cc19cfc97f83364d506bbde9b4247963"}, "tags": {"3.101--he1b5a44_3": "sha256:3a6d1f79775ee79ee4c225176aa37c02b84ede98a6eb4da712d4c8323f8c8689", "3.101--hdbdd923_5": "sha256:7ab31b3ca0b9f652eeead87959a30169cc19cfc97f83364d506bbde9b4247963"}, "docker": "quay.io/biocontainers/bmtool", "aliases": {"bmtool": "/usr/local/bin/bmtool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bmtool.
shpc-registry automated BioContainers addition for bmtool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bmtool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bmtool:3.101--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bmtool/3.101--hdbdd923_5
$ module help quay.io/biocontainers/bmtool/3.101--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bmtool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bmtool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bmtool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bmtool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bmtool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bmtool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bmtool

```bash
$ singularity exec <container> /usr/local/bin/bmtool
$ podman run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
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