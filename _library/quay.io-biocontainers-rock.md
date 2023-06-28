---
layout: container
name:  "quay.io/biocontainers/rock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rock/container.yaml"
updated_at: "2023-06-28 03:41:34.808801"
latest: "2.0--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/rock"
aliases:
 - "rock"
versions:
 - "2.0--h9f5acd7_0"
 - "2.0--h4ac6f70_2"
description: "singularity registry hpc automated addition for rock"
config: {"url": "https://biocontainers.pro/tools/rock", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rock", "latest": {"2.0--h4ac6f70_2": "sha256:0fce6a4d905e1ff56ba87b40dc58ac7463bded4ee9a571c1e1423c232882165b"}, "tags": {"2.0--h9f5acd7_0": "sha256:7c1eccd07a6499a89d315006ab918590bcbe0ba8ee5914a59ffb038a0a03c2c1", "2.0--h4ac6f70_2": "sha256:0fce6a4d905e1ff56ba87b40dc58ac7463bded4ee9a571c1e1423c232882165b"}, "docker": "quay.io/biocontainers/rock", "aliases": {"rock": "/usr/local/bin/rock"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rock.
singularity registry hpc automated addition for rock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rock:2.0--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rock/2.0--h4ac6f70_2
$ module help quay.io/biocontainers/rock/2.0--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rock

```bash
$ singularity exec <container> /usr/local/bin/rock
$ podman run --it --rm --entrypoint /usr/local/bin/rock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rock   -v ${PWD} -w ${PWD} <container> -c " $@"
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