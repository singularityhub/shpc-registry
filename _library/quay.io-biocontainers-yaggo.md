---
layout: container
name:  "quay.io/biocontainers/yaggo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yaggo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/yaggo/container.yaml"
updated_at: "2022-10-27 01:07:20.058203"
latest: "1.5.9--0"
container_url: "https://biocontainers.pro/tools/yaggo"
aliases:
 - "yaggo"
versions:
 - "1.5.9--0"
description: "shpc-registry automated BioContainers addition for yaggo"
config: {"url": "https://biocontainers.pro/tools/yaggo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yaggo", "latest": {"1.5.9--0": "sha256:a51367f9d77246dfc82e3a042b9d4ad9345f1c3332dcaa3962b832219babc640"}, "tags": {"1.5.9--0": "sha256:a51367f9d77246dfc82e3a042b9d4ad9345f1c3332dcaa3962b832219babc640"}, "docker": "quay.io/biocontainers/yaggo", "aliases": {"yaggo": "/usr/local/bin/yaggo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yaggo.
shpc-registry automated BioContainers addition for yaggo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yaggo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yaggo:1.5.9--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yaggo/1.5.9--0
$ module help quay.io/biocontainers/yaggo/1.5.9--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yaggo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yaggo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yaggo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yaggo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yaggo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yaggo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yaggo

```bash
$ singularity exec <container> /usr/local/bin/yaggo
$ podman run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yaggo   -v ${PWD} -w ${PWD} <container> -c " $@"
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