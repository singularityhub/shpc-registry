---
layout: container
name:  "quay.io/biocontainers/proot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proot/container.yaml"
updated_at: "2025-11-16 03:43:05.005222"
latest: "5.1.0--0"
container_url: "https://biocontainers.pro/tools/proot"
aliases:
 - "proot"
versions:
 - "5.1.0--0"
description: "shpc-registry automated BioContainers addition for proot"
config: {"url": "https://biocontainers.pro/tools/proot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proot", "latest": {"5.1.0--0": "sha256:be6b72ab8b91fb6c9ddd37b38ac81f0f531726a5282af54a9e9f28df93016bc6"}, "tags": {"5.1.0--0": "sha256:be6b72ab8b91fb6c9ddd37b38ac81f0f531726a5282af54a9e9f28df93016bc6"}, "docker": "quay.io/biocontainers/proot", "aliases": {"proot": "/usr/local/bin/proot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proot.
shpc-registry automated BioContainers addition for proot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proot:5.1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proot/5.1.0--0
$ module help quay.io/biocontainers/proot/5.1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proot

```bash
$ singularity exec <container> /usr/local/bin/proot
$ podman run --it --rm --entrypoint /usr/local/bin/proot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proot   -v ${PWD} -w ${PWD} <container> -c " $@"
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