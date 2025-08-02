---
layout: container
name:  "quay.io/biocontainers/moreutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moreutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moreutils/container.yaml"
updated_at: "2025-08-02 04:14:20.992216"
latest: "0.5.7--1"
container_url: "https://biocontainers.pro/tools/moreutils"
aliases:
 - "chronic"
 - "combine"
 - "errno"
 - "ifdata"
 - "ifne"
 - "isutf8"
 - "lckdo"
 - "mispipe"
 - "pee"
 - "sponge"
 - "ts"
 - "vidir"
 - "vipe"
 - "zrun"
versions:
 - "0.5.7--1"
description: "shpc-registry automated BioContainers addition for moreutils"
config: {"url": "https://biocontainers.pro/tools/moreutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moreutils", "latest": {"0.5.7--1": "sha256:ac489c0f88e565d5af6896f556b912155df385d9c949307abb14270201ae0dbf"}, "tags": {"0.5.7--1": "sha256:ac489c0f88e565d5af6896f556b912155df385d9c949307abb14270201ae0dbf"}, "docker": "quay.io/biocontainers/moreutils", "aliases": {"chronic": "/usr/local/bin/chronic", "combine": "/usr/local/bin/combine", "errno": "/usr/local/bin/errno", "ifdata": "/usr/local/bin/ifdata", "ifne": "/usr/local/bin/ifne", "isutf8": "/usr/local/bin/isutf8", "lckdo": "/usr/local/bin/lckdo", "mispipe": "/usr/local/bin/mispipe", "pee": "/usr/local/bin/pee", "sponge": "/usr/local/bin/sponge", "ts": "/usr/local/bin/ts", "vidir": "/usr/local/bin/vidir", "vipe": "/usr/local/bin/vipe", "zrun": "/usr/local/bin/zrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moreutils.
shpc-registry automated BioContainers addition for moreutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moreutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moreutils:0.5.7--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moreutils/0.5.7--1
$ module help quay.io/biocontainers/moreutils/0.5.7--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moreutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moreutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moreutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moreutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moreutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moreutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chronic

```bash
$ singularity exec <container> /usr/local/bin/chronic
$ podman run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine

```bash
$ singularity exec <container> /usr/local/bin/combine
$ podman run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### errno

```bash
$ singularity exec <container> /usr/local/bin/errno
$ podman run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifdata

```bash
$ singularity exec <container> /usr/local/bin/ifdata
$ podman run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifne

```bash
$ singularity exec <container> /usr/local/bin/ifne
$ podman run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isutf8

```bash
$ singularity exec <container> /usr/local/bin/isutf8
$ podman run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lckdo

```bash
$ singularity exec <container> /usr/local/bin/lckdo
$ podman run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mispipe

```bash
$ singularity exec <container> /usr/local/bin/mispipe
$ podman run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pee

```bash
$ singularity exec <container> /usr/local/bin/pee
$ podman run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sponge

```bash
$ singularity exec <container> /usr/local/bin/sponge
$ podman run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ts

```bash
$ singularity exec <container> /usr/local/bin/ts
$ podman run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vidir

```bash
$ singularity exec <container> /usr/local/bin/vidir
$ podman run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vipe

```bash
$ singularity exec <container> /usr/local/bin/vipe
$ podman run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zrun

```bash
$ singularity exec <container> /usr/local/bin/zrun
$ podman run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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