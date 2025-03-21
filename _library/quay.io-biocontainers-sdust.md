---
layout: container
name:  "quay.io/biocontainers/sdust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sdust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sdust/container.yaml"
updated_at: "2025-03-21 03:37:08.212447"
latest: "0.1--h077b44d_2"
container_url: "https://biocontainers.pro/tools/sdust"
aliases:
 - "sdust"
versions:
 - "0.1--hdcf5f25_1"
 - "0.1--h077b44d_2"
description: "singularity registry hpc automated addition for sdust"
config: {"url": "https://biocontainers.pro/tools/sdust", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sdust", "latest": {"0.1--h077b44d_2": "sha256:4dc0baa8d4d4104e57379a1abcb359dcb08b793619fbe998a7ba83d2fd4d5b95"}, "tags": {"0.1--hdcf5f25_1": "sha256:09e66e581edc837b3d25d34f4dac2c5492c1ad7bf979ca414fc8e533d750c3c4", "0.1--h077b44d_2": "sha256:4dc0baa8d4d4104e57379a1abcb359dcb08b793619fbe998a7ba83d2fd4d5b95"}, "docker": "quay.io/biocontainers/sdust", "aliases": {"sdust": "/usr/local/bin/sdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sdust.
singularity registry hpc automated addition for sdust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sdust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sdust:0.1--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sdust/0.1--h077b44d_2
$ module help quay.io/biocontainers/sdust/0.1--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sdust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sdust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sdust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sdust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sdust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sdust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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