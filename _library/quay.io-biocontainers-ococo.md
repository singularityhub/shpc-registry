---
layout: container
name:  "quay.io/biocontainers/ococo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ococo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ococo/container.yaml"
updated_at: "2023-07-26 03:28:15.602581"
latest: "0.1.2.7--h146fbdb_8"
container_url: "https://biocontainers.pro/tools/ococo"
aliases:
 - "ococo"
versions:
 - "0.1.2.7--h867801b_5"
 - "0.1.2.7--hd36ca80_6"
 - "0.1.2.7--h146fbdb_8"
description: "shpc-registry automated BioContainers addition for ococo"
config: {"url": "https://biocontainers.pro/tools/ococo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ococo", "latest": {"0.1.2.7--h146fbdb_8": "sha256:5488036549fa99caf35f3662f12ee3de8548c1c9888735e859fcac676ebbd542"}, "tags": {"0.1.2.7--h867801b_5": "sha256:0fb9c4047d3a8c055a8a3a1aacdbaaeca934da7467429a460d8031e7f12f1e31", "0.1.2.7--hd36ca80_6": "sha256:4c0b5ed18e5ae9568e642656f0ece0517489d928419740b17a4227fef976e5bc", "0.1.2.7--h146fbdb_8": "sha256:5488036549fa99caf35f3662f12ee3de8548c1c9888735e859fcac676ebbd542"}, "docker": "quay.io/biocontainers/ococo", "aliases": {"ococo": "/usr/local/bin/ococo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ococo.
shpc-registry automated BioContainers addition for ococo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ococo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ococo:0.1.2.7--h146fbdb_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ococo/0.1.2.7--h146fbdb_8
$ module help quay.io/biocontainers/ococo/0.1.2.7--h146fbdb_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ococo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ococo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ococo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ococo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ococo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ococo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ococo

```bash
$ singularity exec <container> /usr/local/bin/ococo
$ podman run --it --rm --entrypoint /usr/local/bin/ococo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ococo   -v ${PWD} -w ${PWD} <container> -c " $@"
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