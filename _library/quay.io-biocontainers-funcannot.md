---
layout: container
name:  "quay.io/biocontainers/funcannot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/funcannot/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/funcannot/container.yaml"
updated_at: "2022-10-27 01:11:53.122153"
latest: "v2.8--h470a237_1"
container_url: "https://biocontainers.pro/tools/funcannot"
aliases:
 - "funcannot"
versions:
 - "v2.8--h470a237_1"
description: "shpc-registry automated BioContainers addition for funcannot"
config: {"url": "https://biocontainers.pro/tools/funcannot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for funcannot", "latest": {"v2.8--h470a237_1": "sha256:b8c2d24f89a4293ee221ee4af860d3a5d02355f369fccb779525cf4a89470b37"}, "tags": {"v2.8--h470a237_1": "sha256:b8c2d24f89a4293ee221ee4af860d3a5d02355f369fccb779525cf4a89470b37"}, "docker": "quay.io/biocontainers/funcannot", "aliases": {"funcannot": "/usr/local/bin/funcannot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/funcannot.
shpc-registry automated BioContainers addition for funcannot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/funcannot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/funcannot:v2.8--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/funcannot/v2.8--h470a237_1
$ module help quay.io/biocontainers/funcannot/v2.8--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### funcannot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### funcannot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### funcannot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### funcannot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### funcannot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### funcannot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### funcannot

```bash
$ singularity exec <container> /usr/local/bin/funcannot
$ podman run --it --rm --entrypoint /usr/local/bin/funcannot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funcannot   -v ${PWD} -w ${PWD} <container> -c " $@"
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