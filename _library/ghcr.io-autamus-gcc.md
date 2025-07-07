---
layout: container
name:  "ghcr.io/autamus/gcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gcc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gcc/container.yaml"
updated_at: "2025-07-07 04:18:36.625861"
latest: "12.2.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/gcc"
aliases:
 - "c++"
 - "cpp"
 - "g++"
 - "gcc"
 - "gcc-ar"
 - "gcc-nm"
 - "gcc-ranlib"
 - "gcov"
 - "gcov-dump"
 - "gcov-tool"
 - "gfortran"
 - "zstd"
versions:
 - "10.3.0"
 - "11.1.0"
 - "11.2.0"
 - "latest"
 - "11.3.0"
 - "12.2.0"
 - "12.1.0"
description: "The GNU Compiler Collection"
config: {"docker": "ghcr.io/autamus/gcc", "url": "https://github.com/orgs/autamus/packages/container/package/gcc", "maintainer": "@vsoch", "description": "The GNU Compiler Collection", "latest": {"12.2.0": "sha256:02f2bb400eb4b29eeda564d11f99696e6f0b38a7c9f1f497d2924a83173b3975"}, "tags": {"10.3.0": "sha256:f06a6be26b7e03e405061cceb10e9df9787f1c7d79a475613a0165c2ec133e98", "11.1.0": "sha256:eab5ff08025ade13c2f5ed1b71954f353a7f477ffb94a50456b633527c87bfd3", "11.2.0": "sha256:acc888bb3828e0d0be8e1ee0f22706e5db71e8578a4f388f6cce94236541fba0", "latest": "sha256:02f2bb400eb4b29eeda564d11f99696e6f0b38a7c9f1f497d2924a83173b3975", "11.3.0": "sha256:7c276796cc78837f8e9ed0cd1cf46f06f29c0b6ce81aab04e582cca117608f46", "12.2.0": "sha256:02f2bb400eb4b29eeda564d11f99696e6f0b38a7c9f1f497d2924a83173b3975", "12.1.0": "sha256:b5c42f140ca3dadeb2c998a029e8cc8b7bdb5f9b37527c413d8b4df19b1a7924"}, "aliases": {"c++": "/opt/view/bin/c++", "cpp": "/opt/view/bin/cpp", "g++": "/opt/view/bin/g++", "gcc": "/opt/view/bin/gcc", "gcc-ar": "/opt/view/bin/gcc-ar", "gcc-nm": "/opt/view/bin/gcc-nm", "gcc-ranlib": "/opt/view/bin/gcc-ranlib", "gcov": "/opt/view/bin/gcov", "gcov-dump": "/opt/view/bin/gcov-dump", "gcov-tool": "/opt/view/bin/gcov-tool", "gfortran": "/opt/view/bin/gfortran", "zstd": "/opt/view/bin/zstd"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gcc.
The GNU Compiler Collection
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gcc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gcc:12.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gcc/12.2.0
$ module help ghcr.io/autamus/gcc/12.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c++

```bash
$ singularity exec <container> /opt/view/bin/c++
$ podman run --it --rm --entrypoint /opt/view/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp

```bash
$ singularity exec <container> /opt/view/bin/cpp
$ podman run --it --rm --entrypoint /opt/view/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g++

```bash
$ singularity exec <container> /opt/view/bin/g++
$ podman run --it --rm --entrypoint /opt/view/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc

```bash
$ singularity exec <container> /opt/view/bin/gcc
$ podman run --it --rm --entrypoint /opt/view/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ar

```bash
$ singularity exec <container> /opt/view/bin/gcc-ar
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-nm

```bash
$ singularity exec <container> /opt/view/bin/gcc-nm
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ranlib

```bash
$ singularity exec <container> /opt/view/bin/gcc-ranlib
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov

```bash
$ singularity exec <container> /opt/view/bin/gcov
$ podman run --it --rm --entrypoint /opt/view/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-dump

```bash
$ singularity exec <container> /opt/view/bin/gcov-dump
$ podman run --it --rm --entrypoint /opt/view/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-tool

```bash
$ singularity exec <container> /opt/view/bin/gcov-tool
$ podman run --it --rm --entrypoint /opt/view/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfortran

```bash
$ singularity exec <container> /opt/view/bin/gfortran
$ podman run --it --rm --entrypoint /opt/view/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zstd

```bash
$ singularity exec <container> /opt/view/bin/zstd
$ podman run --it --rm --entrypoint /opt/view/bin/zstd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/zstd   -v ${PWD} -w ${PWD} <container> -c " $@"
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