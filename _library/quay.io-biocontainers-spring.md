---
layout: container
name:  "quay.io/biocontainers/spring"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spring/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spring/container.yaml"
updated_at: "2024-06-27 03:09:59.602821"
latest: "1.1.1--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/spring"
aliases:
 - "spring"
versions:
 - "1.1.0--h9f5acd7_0"
 - "1.1.0--h4ac6f70_2"
 - "1.1.1--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for spring"
config: {"url": "https://biocontainers.pro/tools/spring", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spring", "latest": {"1.1.1--h4ac6f70_2": "sha256:c3b1a888d5439bdcf99e8af19f3b445259648c3df8290602c5e7ced8efff2b1e"}, "tags": {"1.1.0--h9f5acd7_0": "sha256:cef9815bea26dd1f47e3cb3a2ac71f03ac0c372972bab8e80b43e56bc3ce1a0f", "1.1.0--h4ac6f70_2": "sha256:07f915837048af7a3c36cc13e0f2ee26877c222113f5eed0fad831a9d3814ef4", "1.1.1--h4ac6f70_2": "sha256:c3b1a888d5439bdcf99e8af19f3b445259648c3df8290602c5e7ced8efff2b1e"}, "docker": "quay.io/biocontainers/spring", "aliases": {"spring": "/usr/local/bin/spring"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spring.
shpc-registry automated BioContainers addition for spring
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spring
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spring:1.1.1--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spring/1.1.1--h4ac6f70_2
$ module help quay.io/biocontainers/spring/1.1.1--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spring-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spring-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spring-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spring-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spring-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spring-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spring

```bash
$ singularity exec <container> /usr/local/bin/spring
$ podman run --it --rm --entrypoint /usr/local/bin/spring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring   -v ${PWD} -w ${PWD} <container> -c " $@"
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