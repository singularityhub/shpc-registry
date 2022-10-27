---
layout: container
name:  "quay.io/biocontainers/logbook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/logbook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/logbook/container.yaml"
updated_at: "2022-10-27 00:46:11.032930"
latest: "1.4.3--py37h14c3975_0"
container_url: "https://biocontainers.pro/tools/logbook"

versions:
 - "1.4.3--py37h14c3975_0"
description: "shpc-registry automated BioContainers addition for logbook"
config: {"url": "https://biocontainers.pro/tools/logbook", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for logbook", "latest": {"1.4.3--py37h14c3975_0": "sha256:7bd8c68dde8888cb4da83be21a2e4e0d9b4ab20963afaab29c93eca1dc5aecda"}, "tags": {"1.4.3--py37h14c3975_0": "sha256:7bd8c68dde8888cb4da83be21a2e4e0d9b4ab20963afaab29c93eca1dc5aecda"}, "docker": "quay.io/biocontainers/logbook"}
---

This module is a singularity container wrapper for quay.io/biocontainers/logbook.
shpc-registry automated BioContainers addition for logbook
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/logbook
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/logbook:1.4.3--py37h14c3975_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/logbook/1.4.3--py37h14c3975_0
$ module help quay.io/biocontainers/logbook/1.4.3--py37h14c3975_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### logbook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### logbook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### logbook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### logbook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### logbook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### logbook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### logbook

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