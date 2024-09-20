---
layout: container
name:  "quay.io/biocontainers/bats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bats/container.yaml"
updated_at: "2024-09-20 03:21:31.459265"
latest: "0.4.0--1"
container_url: "https://biocontainers.pro/tools/bats"
aliases:
 - "bats"
versions:
 - "0.4.0--1"
description: "shpc-registry automated BioContainers addition for bats"
config: {"url": "https://biocontainers.pro/tools/bats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bats", "latest": {"0.4.0--1": "sha256:8a79f2694f4b14702e39dfb9927a3266afc23408c10ab4c254148ae8f71ae0fb"}, "tags": {"0.4.0--1": "sha256:8a79f2694f4b14702e39dfb9927a3266afc23408c10ab4c254148ae8f71ae0fb"}, "docker": "quay.io/biocontainers/bats", "aliases": {"bats": "/usr/local/bin/bats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bats.
shpc-registry automated BioContainers addition for bats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bats:0.4.0--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bats/0.4.0--1
$ module help quay.io/biocontainers/bats/0.4.0--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bats

```bash
$ singularity exec <container> /usr/local/bin/bats
$ podman run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bats   -v ${PWD} -w ${PWD} <container> -c " $@"
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