---
layout: container
name:  "quay.io/biocontainers/super_distance"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/super_distance/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/super_distance/container.yaml"
updated_at: "2023-11-06 02:56:24.299771"
latest: "1.1.0--he4a0461_5"
container_url: "https://biocontainers.pro/tools/super_distance"
aliases:
 - "super_distance"
versions:
 - "1.1.0--h7132678_3"
 - "1.1.0--he4a0461_5"
description: "shpc-registry automated BioContainers addition for super_distance"
config: {"url": "https://biocontainers.pro/tools/super_distance", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for super_distance", "latest": {"1.1.0--he4a0461_5": "sha256:e9542359f8387e8ef66f10f555355d76d783b4048d7d993463dd73c9ba3335b2"}, "tags": {"1.1.0--h7132678_3": "sha256:a61f7dba5e92d4f0fb0cfaf9ad819817f6a07ef6f8237a832ff96b522d7c3ff6", "1.1.0--he4a0461_5": "sha256:e9542359f8387e8ef66f10f555355d76d783b4048d7d993463dd73c9ba3335b2"}, "docker": "quay.io/biocontainers/super_distance", "aliases": {"super_distance": "/usr/local/bin/super_distance"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/super_distance.
shpc-registry automated BioContainers addition for super_distance
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/super_distance
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/super_distance:1.1.0--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/super_distance/1.1.0--he4a0461_5
$ module help quay.io/biocontainers/super_distance/1.1.0--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### super_distance-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### super_distance-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### super_distance-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### super_distance-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### super_distance-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### super_distance-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### super_distance

```bash
$ singularity exec <container> /usr/local/bin/super_distance
$ podman run --it --rm --entrypoint /usr/local/bin/super_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/super_distance   -v ${PWD} -w ${PWD} <container> -c " $@"
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