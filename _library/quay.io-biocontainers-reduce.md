---
layout: container
name:  "quay.io/biocontainers/reduce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reduce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reduce/container.yaml"
updated_at: "2025-12-31 04:13:59.206666"
latest: "4.15--py311he264feb_3"
container_url: "https://biocontainers.pro/tools/reduce"
aliases:
 - "reduce"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "4.14--py310hb119401_1"
 - "4.14--py311h9f068be_2"
 - "4.14--py312h9c9b0c2_3"
 - "4.15--h503566f_1"
 - "4.15--py311he264feb_2"
 - "4.15--py311he264feb_3"
description: "singularity registry hpc automated addition for reduce"
config: {"url": "https://biocontainers.pro/tools/reduce", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reduce", "latest": {"4.15--py311he264feb_3": "sha256:9f650daee99e852d9207bcff9ea5999f02e7ea4cbd83d63ff4ad4c034f35849e"}, "tags": {"4.14--py310hb119401_1": "sha256:54116c6a44bc4a606d9505f2eeaa79cd2b7cff861bad0e656005b50633443bb0", "4.14--py311h9f068be_2": "sha256:9f5ec69926e679e63a9189e77333ec509c10a0f3c828176bfb73c0c8dab0bf56", "4.14--py312h9c9b0c2_3": "sha256:4cbdab056f076356a600bda2efa686ff3e2bdb3fe73cd543552058d2c23db3d9", "4.15--h503566f_1": "sha256:f030c61d8b8967c2dfc296dd9afe4037b30cf81ef2531127be7298e8a78425cd", "4.15--py311he264feb_2": "sha256:b20f0d3aaba1bf55191db4af7dbffeae7a15fde91785f1e7c5850d3f68dd8b82", "4.15--py311he264feb_3": "sha256:9f650daee99e852d9207bcff9ea5999f02e7ea4cbd83d63ff4ad4c034f35849e"}, "docker": "quay.io/biocontainers/reduce", "aliases": {"reduce": "/usr/local/bin/reduce", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reduce.
singularity registry hpc automated addition for reduce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reduce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reduce:4.15--py311he264feb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reduce/4.15--py311he264feb_3
$ module help quay.io/biocontainers/reduce/4.15--py311he264feb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reduce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reduce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reduce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reduce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reduce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reduce-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### reduce

```bash
$ singularity exec <container> /usr/local/bin/reduce
$ podman run --it --rm --entrypoint /usr/local/bin/reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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