---
layout: container
name:  "quay.io/biocontainers/lemon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lemon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lemon/container.yaml"
updated_at: "2024-10-21 03:21:03.136350"
latest: "1.3.1--0"
container_url: "https://biocontainers.pro/tools/lemon"

versions:
 - "1.3.1--0"
description: "shpc-registry automated BioContainers addition for lemon"
config: {"url": "https://biocontainers.pro/tools/lemon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lemon", "latest": {"1.3.1--0": "sha256:b8a56eb4f7b720a78890f87e27f4f8c820bb6f2a2a7cc5c812e8a71abc968931"}, "tags": {"1.3.1--0": "sha256:b8a56eb4f7b720a78890f87e27f4f8c820bb6f2a2a7cc5c812e8a71abc968931"}, "docker": "quay.io/biocontainers/lemon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/lemon.
shpc-registry automated BioContainers addition for lemon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lemon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lemon:1.3.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lemon/1.3.1--0
$ module help quay.io/biocontainers/lemon/1.3.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lemon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lemon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lemon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lemon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lemon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lemon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### lemon

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