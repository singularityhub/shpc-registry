---
layout: container
name:  "quay.io/biocontainers/r-abdiv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-abdiv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-abdiv/container.yaml"
updated_at: "2024-03-24 02:54:08.136196"
latest: "0.2.0--r43h3121a25_2"
container_url: "https://biocontainers.pro/tools/r-abdiv"

versions:
 - "0.2.0--r42h3121a25_1"
 - "0.2.0--r43h3121a25_2"
description: "singularity registry hpc automated addition for r-abdiv"
config: {"url": "https://biocontainers.pro/tools/r-abdiv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-abdiv", "latest": {"0.2.0--r43h3121a25_2": "sha256:5e55c5d58b2a22450c78691e52c75ca92bc726b05dc85d67d6446fe491e367a3"}, "tags": {"0.2.0--r42h3121a25_1": "sha256:9cf6d39e29d69f1dc660e90af50485053198ae542f7223a74f0e43017254d8e1", "0.2.0--r43h3121a25_2": "sha256:5e55c5d58b2a22450c78691e52c75ca92bc726b05dc85d67d6446fe491e367a3"}, "docker": "quay.io/biocontainers/r-abdiv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-abdiv.
singularity registry hpc automated addition for r-abdiv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-abdiv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-abdiv:0.2.0--r43h3121a25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-abdiv/0.2.0--r43h3121a25_2
$ module help quay.io/biocontainers/r-abdiv/0.2.0--r43h3121a25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-abdiv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-abdiv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-abdiv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-abdiv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-abdiv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-abdiv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-abdiv

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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