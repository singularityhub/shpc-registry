---
layout: container
name:  "quay.io/biocontainers/spring2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spring2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spring2/container.yaml"
updated_at: "2026-08-31 08:25:11.027960"
latest: "1.3.4--h8471819_0"
container_url: "https://biocontainers.pro/tools/spring2"
aliases:
 - "spring2"
versions:
 - "1.3.4--h8471819_0"
description: "singularity registry hpc automated addition for spring2"
config: {"url": "https://biocontainers.pro/tools/spring2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spring2", "latest": {"1.3.4--h8471819_0": "sha256:42b89037af5b353b5ab5f599f3c9d555662761bc3cb718f3389c29234976ce3d"}, "tags": {"1.3.4--h8471819_0": "sha256:42b89037af5b353b5ab5f599f3c9d555662761bc3cb718f3389c29234976ce3d"}, "docker": "quay.io/biocontainers/spring2", "aliases": {"spring2": "/usr/local/bin/spring2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spring2.
singularity registry hpc automated addition for spring2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spring2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spring2:1.3.4--h8471819_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spring2/1.3.4--h8471819_0
$ module help quay.io/biocontainers/spring2/1.3.4--h8471819_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spring2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spring2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spring2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spring2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spring2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spring2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spring2

```bash
$ singularity exec <container> /usr/local/bin/spring2
$ podman run --it --rm --entrypoint /usr/local/bin/spring2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring2   -v ${PWD} -w ${PWD} <container> -c " $@"
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