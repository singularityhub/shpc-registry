---
layout: container
name:  "quay.io/biocontainers/structure"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/structure/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/structure/container.yaml"
updated_at: "2025-10-06 03:10:15.192938"
latest: "2.3.4--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/structure"
aliases:
 - "structure"
versions:
 - "2.3.4--hec16e2b_4"
 - "2.3.4--h031d066_6"
 - "2.3.4--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for structure"
config: {"url": "https://biocontainers.pro/tools/structure", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for structure", "latest": {"2.3.4--h7b50bb2_7": "sha256:1295d738ae4ef24497d60930a7af5902f622ab16ec2757bcb69f50afb2f0ab36"}, "tags": {"2.3.4--hec16e2b_4": "sha256:1262296ea0fd9387033f22766b4ada46d8fb1ed475959bc57defe913293eceea", "2.3.4--h031d066_6": "sha256:f5dead4da22d9f2f1aac5e9b1b60f742d49202a2e7baf97c587e15bf6996cbba", "2.3.4--h7b50bb2_7": "sha256:1295d738ae4ef24497d60930a7af5902f622ab16ec2757bcb69f50afb2f0ab36"}, "docker": "quay.io/biocontainers/structure", "aliases": {"structure": "/usr/local/bin/structure"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/structure.
shpc-registry automated BioContainers addition for structure
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/structure
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/structure:2.3.4--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/structure/2.3.4--h7b50bb2_7
$ module help quay.io/biocontainers/structure/2.3.4--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### structure-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### structure-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### structure-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### structure-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### structure-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### structure-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### structure

```bash
$ singularity exec <container> /usr/local/bin/structure
$ podman run --it --rm --entrypoint /usr/local/bin/structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structure   -v ${PWD} -w ${PWD} <container> -c " $@"
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