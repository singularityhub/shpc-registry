---
layout: container
name:  "quay.io/biocontainers/gzrt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gzrt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gzrt/container.yaml"
updated_at: "2024-12-03 04:42:38.441375"
latest: "0.8--he4a0461_0"
container_url: "https://biocontainers.pro/tools/gzrt"
aliases:
 - "gzrecover"
versions:
 - "0.8--he4a0461_0"
description: "singularity registry hpc automated addition for gzrt"
config: {"url": "https://biocontainers.pro/tools/gzrt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gzrt", "latest": {"0.8--he4a0461_0": "sha256:1486d96c1fe956ef9689d356657ee33e573061ecad2468897d84b1fad4fdf7aa"}, "tags": {"0.8--he4a0461_0": "sha256:1486d96c1fe956ef9689d356657ee33e573061ecad2468897d84b1fad4fdf7aa"}, "docker": "quay.io/biocontainers/gzrt", "aliases": {"gzrecover": "/usr/local/bin/gzrecover"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gzrt.
singularity registry hpc automated addition for gzrt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gzrt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gzrt:0.8--he4a0461_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gzrt/0.8--he4a0461_0
$ module help quay.io/biocontainers/gzrt/0.8--he4a0461_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gzrt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gzrt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gzrt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gzrt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gzrt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gzrt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gzrecover

```bash
$ singularity exec <container> /usr/local/bin/gzrecover
$ podman run --it --rm --entrypoint /usr/local/bin/gzrecover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzrecover   -v ${PWD} -w ${PWD} <container> -c " $@"
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