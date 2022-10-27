---
layout: container
name:  "quay.io/biocontainers/sensv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sensv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sensv/container.yaml"
updated_at: "2022-10-27 00:57:04.279426"
latest: "v1.0.1--h8b12597_0"
container_url: "https://biocontainers.pro/tools/sensv"
aliases:
 - "SURVIVOR"
 - "config.ini"
 - "grabix"
 - "libpypy3-c.so.debug"
 - "pypy3"
 - "sensv"
versions:
 - "v1.0.1--h8b12597_0"
description: "shpc-registry automated BioContainers addition for sensv"
config: {"url": "https://biocontainers.pro/tools/sensv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sensv", "latest": {"v1.0.1--h8b12597_0": "sha256:001423fe13c250b9d74dcdca4043a55e6e654f5326b93ed5ced03514d3b85d5b"}, "tags": {"v1.0.1--h8b12597_0": "sha256:001423fe13c250b9d74dcdca4043a55e6e654f5326b93ed5ced03514d3b85d5b"}, "docker": "quay.io/biocontainers/sensv", "aliases": {"SURVIVOR": "/usr/local/bin/SURVIVOR", "config.ini": "/usr/local/bin/config.ini", "grabix": "/usr/local/bin/grabix", "libpypy3-c.so.debug": "/usr/local/bin/libpypy3-c.so.debug", "pypy3": "/usr/local/bin/pypy3", "sensv": "/usr/local/bin/sensv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sensv.
shpc-registry automated BioContainers addition for sensv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sensv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sensv:v1.0.1--h8b12597_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sensv/v1.0.1--h8b12597_0
$ module help quay.io/biocontainers/sensv/v1.0.1--h8b12597_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sensv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sensv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sensv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sensv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sensv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sensv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SURVIVOR

```bash
$ singularity exec <container> /usr/local/bin/SURVIVOR
$ podman run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config.ini

```bash
$ singularity exec <container> /usr/local/bin/config.ini
$ podman run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grabix

```bash
$ singularity exec <container> /usr/local/bin/grabix
$ podman run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libpypy3-c.so.debug

```bash
$ singularity exec <container> /usr/local/bin/libpypy3-c.so.debug
$ podman run --it --rm --entrypoint /usr/local/bin/libpypy3-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libpypy3-c.so.debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypy3

```bash
$ singularity exec <container> /usr/local/bin/pypy3
$ podman run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypy3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sensv

```bash
$ singularity exec <container> /usr/local/bin/sensv
$ podman run --it --rm --entrypoint /usr/local/bin/sensv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sensv   -v ${PWD} -w ${PWD} <container> -c " $@"
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