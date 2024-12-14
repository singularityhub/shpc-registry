---
layout: container
name:  "quay.io/biocontainers/bolt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bolt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bolt/container.yaml"
updated_at: "2024-12-14 03:21:32.545050"
latest: "0.3.0--h65a12c2_6"
container_url: "https://biocontainers.pro/tools/bolt"

versions:
 - "0.3.0--h4a302ff_5"
 - "0.3.0--h65a12c2_6"
description: "shpc-registry automated BioContainers addition for bolt"
config: {"url": "https://biocontainers.pro/tools/bolt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bolt", "latest": {"0.3.0--h65a12c2_6": "sha256:82d87dd0bc2cc9e8c42e4d6d102217a443fd43a904cd863012e56e75ae4b5da8"}, "tags": {"0.3.0--h4a302ff_5": "sha256:8cc764364680531c4a6519d35b2cef75d6931fa70392d9dcc692d3e56b23d831", "0.3.0--h65a12c2_6": "sha256:82d87dd0bc2cc9e8c42e4d6d102217a443fd43a904cd863012e56e75ae4b5da8"}, "docker": "quay.io/biocontainers/bolt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bolt.
shpc-registry automated BioContainers addition for bolt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bolt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bolt:0.3.0--h65a12c2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bolt/0.3.0--h65a12c2_6
$ module help quay.io/biocontainers/bolt/0.3.0--h65a12c2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bolt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bolt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bolt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bolt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bolt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bolt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bolt

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