---
layout: container
name:  "quay.io/biocontainers/rust-overlaps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-overlaps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-overlaps/container.yaml"
updated_at: "2023-11-13 03:30:41.385327"
latest: "0.1.1--he4a0461_9"
container_url: "https://biocontainers.pro/tools/rust-overlaps"
aliases:
 - "rust-overlaps"
versions:
 - "0.1.1--h7132678_7"
 - "0.1.1--he4a0461_9"
description: "shpc-registry automated BioContainers addition for rust-overlaps"
config: {"url": "https://biocontainers.pro/tools/rust-overlaps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rust-overlaps", "latest": {"0.1.1--he4a0461_9": "sha256:a933a2ea33492bd51feaee3416b3fc064afd047ee458ab5663afdb9c0509c7b6"}, "tags": {"0.1.1--h7132678_7": "sha256:02d445e0122a974a8febacd13901aee09f5f4c171116698fe7fa052907d8441a", "0.1.1--he4a0461_9": "sha256:a933a2ea33492bd51feaee3416b3fc064afd047ee458ab5663afdb9c0509c7b6"}, "docker": "quay.io/biocontainers/rust-overlaps", "aliases": {"rust-overlaps": "/usr/local/bin/rust-overlaps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-overlaps.
shpc-registry automated BioContainers addition for rust-overlaps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-overlaps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-overlaps:0.1.1--he4a0461_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-overlaps/0.1.1--he4a0461_9
$ module help quay.io/biocontainers/rust-overlaps/0.1.1--he4a0461_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-overlaps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-overlaps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-overlaps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-overlaps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-overlaps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-overlaps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rust-overlaps

```bash
$ singularity exec <container> /usr/local/bin/rust-overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
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