---
layout: container
name:  "quay.io/biocontainers/dos2unix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dos2unix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dos2unix/container.yaml"
updated_at: "2026-01-06 03:53:52.709342"
latest: "7.5.3"
container_url: "https://biocontainers.pro/tools/dos2unix"
aliases:
 - "dos2unix"
 - "mac2unix"
 - "unix2dos"
 - "unix2mac"
versions:
 - "7.5.2"
 - "7.5.3"
description: "singularity registry hpc automated addition for dos2unix"
config: {"url": "https://biocontainers.pro/tools/dos2unix", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dos2unix", "latest": {"7.5.3": "sha256:6297c1b0c9b8f641bb0176675d1c7e5453eae73e7e0da0f1717b3aa2d97d712c"}, "tags": {"7.5.2": "sha256:f9ae717e6827571c03147d9d321ebc999f2513fc13854e714a0e51f92fdf65ac", "7.5.3": "sha256:6297c1b0c9b8f641bb0176675d1c7e5453eae73e7e0da0f1717b3aa2d97d712c"}, "docker": "quay.io/biocontainers/dos2unix", "aliases": {"dos2unix": "/usr/local/bin/dos2unix", "mac2unix": "/usr/local/bin/mac2unix", "unix2dos": "/usr/local/bin/unix2dos", "unix2mac": "/usr/local/bin/unix2mac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dos2unix.
singularity registry hpc automated addition for dos2unix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dos2unix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dos2unix:7.5.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dos2unix/7.5.3
$ module help quay.io/biocontainers/dos2unix/7.5.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dos2unix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dos2unix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dos2unix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dos2unix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dos2unix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dos2unix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dos2unix

```bash
$ singularity exec <container> /usr/local/bin/dos2unix
$ podman run --it --rm --entrypoint /usr/local/bin/dos2unix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dos2unix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mac2unix

```bash
$ singularity exec <container> /usr/local/bin/mac2unix
$ podman run --it --rm --entrypoint /usr/local/bin/mac2unix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mac2unix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unix2dos

```bash
$ singularity exec <container> /usr/local/bin/unix2dos
$ podman run --it --rm --entrypoint /usr/local/bin/unix2dos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unix2dos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unix2mac

```bash
$ singularity exec <container> /usr/local/bin/unix2mac
$ podman run --it --rm --entrypoint /usr/local/bin/unix2mac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unix2mac   -v ${PWD} -w ${PWD} <container> -c " $@"
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