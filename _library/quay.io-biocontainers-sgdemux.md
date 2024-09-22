---
layout: container
name:  "quay.io/biocontainers/sgdemux"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sgdemux/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sgdemux/container.yaml"
updated_at: "2024-09-22 03:33:56.982788"
latest: "1.2.0--h4c94732_2"
container_url: "https://biocontainers.pro/tools/sgdemux"
aliases:
 - "sgdemux"
versions:
 - "1.1.1--ha982bd6_0"
 - "1.1.2--ha982bd6_0"
 - "1.2.0--h4c94732_2"
description: "singularity registry hpc automated addition for sgdemux"
config: {"url": "https://biocontainers.pro/tools/sgdemux", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sgdemux", "latest": {"1.2.0--h4c94732_2": "sha256:52b6d3ff954ae8482e06f8bcd181ec305565ae60573522568c01e89305fc5008"}, "tags": {"1.1.1--ha982bd6_0": "sha256:00a6856695b320ea9a85d726ab4dbaa191ebbdb198edfbb0c7d7352999a1776d", "1.1.2--ha982bd6_0": "sha256:2f521a99f563009375eaacc473d11add529328365da615162d97462cab75a71a", "1.2.0--h4c94732_2": "sha256:52b6d3ff954ae8482e06f8bcd181ec305565ae60573522568c01e89305fc5008"}, "docker": "quay.io/biocontainers/sgdemux", "aliases": {"sgdemux": "/usr/local/bin/sgdemux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sgdemux.
singularity registry hpc automated addition for sgdemux
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sgdemux
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sgdemux:1.2.0--h4c94732_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sgdemux/1.2.0--h4c94732_2
$ module help quay.io/biocontainers/sgdemux/1.2.0--h4c94732_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sgdemux-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sgdemux-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sgdemux-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sgdemux-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sgdemux-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sgdemux-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sgdemux

```bash
$ singularity exec <container> /usr/local/bin/sgdemux
$ podman run --it --rm --entrypoint /usr/local/bin/sgdemux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgdemux   -v ${PWD} -w ${PWD} <container> -c " $@"
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