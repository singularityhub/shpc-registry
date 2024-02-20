---
layout: container
name:  "quay.io/biocontainers/polypolish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/polypolish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/polypolish/container.yaml"
updated_at: "2024-02-20 02:23:27.566539"
latest: "0.6.0--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/polypolish"
aliases:
 - "polypolish"
 - "polypolish_insert_filter.pxd"
 - "polypolish_insert_filter.py"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.5.0--h87f3376_2"
 - "0.5.0--h87f3376_3"
 - "0.5.0--hdbdd923_4"
 - "0.6.0--hdbdd923_0"
description: "singularity registry hpc automated addition for polypolish"
config: {"url": "https://biocontainers.pro/tools/polypolish", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for polypolish", "latest": {"0.6.0--hdbdd923_0": "sha256:cb37a584e7de9905f52ce8d0cb578f32dc1a6b86a48dd98314cb38d21c3bc76d"}, "tags": {"0.5.0--h87f3376_2": "sha256:b404c83acb84c8a7bbcdc8a7e83af00e81de0d87a9d45528d4131ad57c0dd1cb", "0.5.0--h87f3376_3": "sha256:d81aa78d125ff2971620a000785e594d8da73ab3afda9ef4c7a6d40ca680ae6d", "0.5.0--hdbdd923_4": "sha256:4039e2317464283afcc6bf182767c908b2ea3b561b8b70f3a8748c8ab9716d81", "0.6.0--hdbdd923_0": "sha256:cb37a584e7de9905f52ce8d0cb578f32dc1a6b86a48dd98314cb38d21c3bc76d"}, "docker": "quay.io/biocontainers/polypolish", "aliases": {"polypolish": "/usr/local/bin/polypolish", "polypolish_insert_filter.pxd": "/usr/local/bin/polypolish_insert_filter.pxd", "polypolish_insert_filter.py": "/usr/local/bin/polypolish_insert_filter.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/polypolish.
singularity registry hpc automated addition for polypolish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/polypolish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/polypolish:0.6.0--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/polypolish/0.6.0--hdbdd923_0
$ module help quay.io/biocontainers/polypolish/0.6.0--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### polypolish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### polypolish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### polypolish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### polypolish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### polypolish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### polypolish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### polypolish

```bash
$ singularity exec <container> /usr/local/bin/polypolish
$ podman run --it --rm --entrypoint /usr/local/bin/polypolish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polypolish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polypolish_insert_filter.pxd

```bash
$ singularity exec <container> /usr/local/bin/polypolish_insert_filter.pxd
$ podman run --it --rm --entrypoint /usr/local/bin/polypolish_insert_filter.pxd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polypolish_insert_filter.pxd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polypolish_insert_filter.py

```bash
$ singularity exec <container> /usr/local/bin/polypolish_insert_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/polypolish_insert_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polypolish_insert_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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