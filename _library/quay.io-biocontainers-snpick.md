---
layout: container
name:  "quay.io/biocontainers/snpick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snpick/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snpick/container.yaml"
updated_at: "2025-01-06 03:10:01.105075"
latest: "1.0.0--h3f2c17f_0"
container_url: "https://biocontainers.pro/tools/snpick"
aliases:
 - "snpick"
versions:
 - "1.0.0--h3f2c17f_0"
description: "singularity registry hpc automated addition for snpick"
config: {"url": "https://biocontainers.pro/tools/snpick", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snpick", "latest": {"1.0.0--h3f2c17f_0": "sha256:5759dec7c0b1304d37ab37fcf65af7fb9589d5cf4439774c4755a97f51c604e8"}, "tags": {"1.0.0--h3f2c17f_0": "sha256:5759dec7c0b1304d37ab37fcf65af7fb9589d5cf4439774c4755a97f51c604e8"}, "docker": "quay.io/biocontainers/snpick", "aliases": {"snpick": "/usr/local/bin/snpick"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snpick.
singularity registry hpc automated addition for snpick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snpick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snpick:1.0.0--h3f2c17f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snpick/1.0.0--h3f2c17f_0
$ module help quay.io/biocontainers/snpick/1.0.0--h3f2c17f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snpick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snpick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snpick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snpick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snpick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snpick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snpick

```bash
$ singularity exec <container> /usr/local/bin/snpick
$ podman run --it --rm --entrypoint /usr/local/bin/snpick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpick   -v ${PWD} -w ${PWD} <container> -c " $@"
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