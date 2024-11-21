---
layout: container
name:  "quay.io/biocontainers/enano"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enano/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enano/container.yaml"
updated_at: "2024-11-21 03:24:00.880688"
latest: "1.0--hdcf5f25_6"
container_url: "https://biocontainers.pro/tools/enano"
aliases:
 - "enano"
versions:
 - "1.0--hd03093a_4"
 - "1.0--hdcf5f25_6"
description: "shpc-registry automated BioContainers addition for enano"
config: {"url": "https://biocontainers.pro/tools/enano", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for enano", "latest": {"1.0--hdcf5f25_6": "sha256:a3f5a4dab505b0704d9f4c3a627e5f9e1554c075c292731dcb2dea6183cf9ab9"}, "tags": {"1.0--hd03093a_4": "sha256:835b9b948b72fe01ed278456a988114190286596b31c0c6fbfc45ae67eea3141", "1.0--hdcf5f25_6": "sha256:a3f5a4dab505b0704d9f4c3a627e5f9e1554c075c292731dcb2dea6183cf9ab9"}, "docker": "quay.io/biocontainers/enano", "aliases": {"enano": "/usr/local/bin/enano"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enano.
shpc-registry automated BioContainers addition for enano
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enano
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enano:1.0--hdcf5f25_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enano/1.0--hdcf5f25_6
$ module help quay.io/biocontainers/enano/1.0--hdcf5f25_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enano-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enano-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enano-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enano-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enano-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enano-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### enano

```bash
$ singularity exec <container> /usr/local/bin/enano
$ podman run --it --rm --entrypoint /usr/local/bin/enano   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enano   -v ${PWD} -w ${PWD} <container> -c " $@"
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