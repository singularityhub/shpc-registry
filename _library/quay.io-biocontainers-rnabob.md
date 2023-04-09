---
layout: container
name:  "quay.io/biocontainers/rnabob"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnabob/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnabob/container.yaml"
updated_at: "2023-04-09 03:00:36.324486"
latest: "2.2.1--h470a237_1"
container_url: "https://biocontainers.pro/tools/rnabob"
aliases:
 - "rnabob"
versions:
 - "2.2.1--h470a237_1"
description: "shpc-registry automated BioContainers addition for rnabob"
config: {"url": "https://biocontainers.pro/tools/rnabob", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnabob", "latest": {"2.2.1--h470a237_1": "sha256:08f5562582fbad7bf3cdc5d6407870116b7d1bc9bc8a59e9de74511c7b3e4d6a"}, "tags": {"2.2.1--h470a237_1": "sha256:08f5562582fbad7bf3cdc5d6407870116b7d1bc9bc8a59e9de74511c7b3e4d6a"}, "docker": "quay.io/biocontainers/rnabob", "aliases": {"rnabob": "/usr/local/bin/rnabob"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnabob.
shpc-registry automated BioContainers addition for rnabob
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnabob
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnabob:2.2.1--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnabob/2.2.1--h470a237_1
$ module help quay.io/biocontainers/rnabob/2.2.1--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnabob-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnabob-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnabob-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnabob-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnabob-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnabob-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rnabob

```bash
$ singularity exec <container> /usr/local/bin/rnabob
$ podman run --it --rm --entrypoint /usr/local/bin/rnabob   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnabob   -v ${PWD} -w ${PWD} <container> -c " $@"
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