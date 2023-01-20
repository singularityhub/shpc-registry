---
layout: container
name:  "quay.io/biocontainers/treerecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treerecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treerecs/container.yaml"
updated_at: "2023-01-20 03:32:19.397522"
latest: "1.2--h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/treerecs"
aliases:
 - "treerecs"
versions:
 - "1.2--h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for treerecs"
config: {"url": "https://biocontainers.pro/tools/treerecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treerecs", "latest": {"1.2--h9f5acd7_2": "sha256:b87f210730d7e2c501fbb84d72030402de4e0a26477f138035a3bc54d44be1b3"}, "tags": {"1.2--h9f5acd7_2": "sha256:b87f210730d7e2c501fbb84d72030402de4e0a26477f138035a3bc54d44be1b3"}, "docker": "quay.io/biocontainers/treerecs", "aliases": {"treerecs": "/usr/local/bin/treerecs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treerecs.
shpc-registry automated BioContainers addition for treerecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treerecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treerecs:1.2--h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treerecs/1.2--h9f5acd7_2
$ module help quay.io/biocontainers/treerecs/1.2--h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treerecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treerecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treerecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treerecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treerecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treerecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### treerecs

```bash
$ singularity exec <container> /usr/local/bin/treerecs
$ podman run --it --rm --entrypoint /usr/local/bin/treerecs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treerecs   -v ${PWD} -w ${PWD} <container> -c " $@"
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