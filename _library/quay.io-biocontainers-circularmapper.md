---
layout: container
name:  "quay.io/biocontainers/circularmapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circularmapper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/circularmapper/container.yaml"
updated_at: "2022-10-27 00:19:27.511257"
latest: "1.93.5--h4a94de4_1"
container_url: "https://biocontainers.pro/tools/circularmapper"
aliases:
 - "circulargenerator"
 - "realignsamfile"
versions:
 - "1.93.5--h4a94de4_1"
description: "shpc-registry automated BioContainers addition for circularmapper"
config: {"url": "https://biocontainers.pro/tools/circularmapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for circularmapper", "latest": {"1.93.5--h4a94de4_1": "sha256:4d535a4464632ca9d2484185fb7c995700bb29b226e7cf6260a0dfbc53eed895"}, "tags": {"1.93.5--h4a94de4_1": "sha256:4d535a4464632ca9d2484185fb7c995700bb29b226e7cf6260a0dfbc53eed895"}, "docker": "quay.io/biocontainers/circularmapper", "aliases": {"circulargenerator": "/usr/local/bin/circulargenerator", "realignsamfile": "/usr/local/bin/realignsamfile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/circularmapper.
shpc-registry automated BioContainers addition for circularmapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circularmapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circularmapper:1.93.5--h4a94de4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circularmapper/1.93.5--h4a94de4_1
$ module help quay.io/biocontainers/circularmapper/1.93.5--h4a94de4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circularmapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circularmapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circularmapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circularmapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circularmapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circularmapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### circulargenerator

```bash
$ singularity exec <container> /usr/local/bin/circulargenerator
$ podman run --it --rm --entrypoint /usr/local/bin/circulargenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circulargenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### realignsamfile

```bash
$ singularity exec <container> /usr/local/bin/realignsamfile
$ podman run --it --rm --entrypoint /usr/local/bin/realignsamfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/realignsamfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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