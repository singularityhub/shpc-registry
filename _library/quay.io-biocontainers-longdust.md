---
layout: container
name:  "quay.io/biocontainers/longdust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longdust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longdust/container.yaml"
updated_at: "2025-12-08 03:27:41.722365"
latest: "1.2--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/longdust"
aliases:
 - "longdust"
versions:
 - "1.2--h577a1d6_0"
description: "singularity registry hpc automated addition for longdust"
config: {"url": "https://biocontainers.pro/tools/longdust", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for longdust", "latest": {"1.2--h577a1d6_0": "sha256:d73bef7c688a7cadcea5ad211723cb0f9a4f43b5c9cc70ba5547bde2309f8001"}, "tags": {"1.2--h577a1d6_0": "sha256:d73bef7c688a7cadcea5ad211723cb0f9a4f43b5c9cc70ba5547bde2309f8001"}, "docker": "quay.io/biocontainers/longdust", "aliases": {"longdust": "/usr/local/bin/longdust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longdust.
singularity registry hpc automated addition for longdust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longdust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longdust:1.2--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longdust/1.2--h577a1d6_0
$ module help quay.io/biocontainers/longdust/1.2--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longdust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longdust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longdust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longdust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longdust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longdust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### longdust

```bash
$ singularity exec <container> /usr/local/bin/longdust
$ podman run --it --rm --entrypoint /usr/local/bin/longdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longdust   -v ${PWD} -w ${PWD} <container> -c " $@"
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