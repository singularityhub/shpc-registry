---
layout: container
name:  "quay.io/biocontainers/consensify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/consensify/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/consensify/container.yaml"
updated_at: "2025-01-10 03:37:12.212517"
latest: "2.4.0--h077b44d_2"
container_url: "https://biocontainers.pro/tools/consensify"
aliases:
 - "consensify_c"
versions:
 - "2.4.0--hdcf5f25_1"
 - "2.4.0--h077b44d_2"
description: "singularity registry hpc automated addition for consensify"
config: {"url": "https://biocontainers.pro/tools/consensify", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for consensify", "latest": {"2.4.0--h077b44d_2": "sha256:0acffd9269917997663df8e5047d5b8a05b34c248c520a84ab9ed58ba0bf0872"}, "tags": {"2.4.0--hdcf5f25_1": "sha256:de3328f8446bf945753224b7f59896fa2cfa7e4e2d27f5cdee01cba258835923", "2.4.0--h077b44d_2": "sha256:0acffd9269917997663df8e5047d5b8a05b34c248c520a84ab9ed58ba0bf0872"}, "docker": "quay.io/biocontainers/consensify", "aliases": {"consensify_c": "/usr/local/bin/consensify_c"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/consensify.
singularity registry hpc automated addition for consensify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/consensify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/consensify:2.4.0--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/consensify/2.4.0--h077b44d_2
$ module help quay.io/biocontainers/consensify/2.4.0--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consensify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consensify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consensify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consensify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consensify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consensify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consensify_c

```bash
$ singularity exec <container> /usr/local/bin/consensify_c
$ podman run --it --rm --entrypoint /usr/local/bin/consensify_c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensify_c   -v ${PWD} -w ${PWD} <container> -c " $@"
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