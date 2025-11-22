---
layout: container
name:  "quay.io/biocontainers/newmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/newmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/newmap/container.yaml"
updated_at: "2025-11-22 03:36:19.922343"
latest: "0.2--py310h8ea774a_1"
container_url: "https://biocontainers.pro/tools/newmap"
aliases:
 - "newmap"
 - "numpy-config"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2--py310h8ea774a_1"
 - "0.2--py312h9c9b0c2_1"
description: "singularity registry hpc automated addition for newmap"
config: {"url": "https://biocontainers.pro/tools/newmap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for newmap", "latest": {"0.2--py310h8ea774a_1": "sha256:623369e1282526e349897d2ee7ddfe2022c50c470bee5c31ba3c7bd8e11c2f75"}, "tags": {"0.2--py310h8ea774a_1": "sha256:623369e1282526e349897d2ee7ddfe2022c50c470bee5c31ba3c7bd8e11c2f75", "0.2--py312h9c9b0c2_1": "sha256:51c072591ec72ee36f58aad7c3f9a1693d43868c7f66b028d7f5ea9e09b6170d"}, "docker": "quay.io/biocontainers/newmap", "aliases": {"newmap": "/usr/local/bin/newmap", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/newmap.
singularity registry hpc automated addition for newmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/newmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/newmap:0.2--py310h8ea774a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/newmap/0.2--py310h8ea774a_1
$ module help quay.io/biocontainers/newmap/0.2--py310h8ea774a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### newmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### newmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### newmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### newmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### newmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### newmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### newmap

```bash
$ singularity exec <container> /usr/local/bin/newmap
$ podman run --it --rm --entrypoint /usr/local/bin/newmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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