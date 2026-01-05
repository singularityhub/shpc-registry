---
layout: container
name:  "quay.io/biocontainers/rattle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rattle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rattle/container.yaml"
updated_at: "2026-01-05 04:44:27.442465"
latest: "1.0--h5ca1c30_0"
container_url: "https://biocontainers.pro/tools/rattle"
aliases:
 - "rattle"
versions:
 - "1.0--h5ca1c30_0"
description: "singularity registry hpc automated addition for rattle"
config: {"url": "https://biocontainers.pro/tools/rattle", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rattle", "latest": {"1.0--h5ca1c30_0": "sha256:f43ae7fd0e20eac760edee42d04702c98efccf4d06a4cbc621df1e90a62c38b3"}, "tags": {"1.0--h5ca1c30_0": "sha256:f43ae7fd0e20eac760edee42d04702c98efccf4d06a4cbc621df1e90a62c38b3"}, "docker": "quay.io/biocontainers/rattle", "aliases": {"rattle": "/usr/local/bin/rattle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rattle.
singularity registry hpc automated addition for rattle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rattle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rattle:1.0--h5ca1c30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rattle/1.0--h5ca1c30_0
$ module help quay.io/biocontainers/rattle/1.0--h5ca1c30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rattle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rattle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rattle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rattle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rattle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rattle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rattle

```bash
$ singularity exec <container> /usr/local/bin/rattle
$ podman run --it --rm --entrypoint /usr/local/bin/rattle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rattle   -v ${PWD} -w ${PWD} <container> -c " $@"
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