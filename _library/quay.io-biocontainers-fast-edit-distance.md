---
layout: container
name:  "quay.io/biocontainers/fast-edit-distance"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fast-edit-distance/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fast-edit-distance/container.yaml"
updated_at: "2025-02-16 03:11:33.156765"
latest: "1.2.2--py39hff71179_0"
container_url: "https://biocontainers.pro/tools/fast-edit-distance"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.2.1--py310h7c593f9_1"
 - "1.2.1--py311hdad781d_1"
 - "1.2.1--py310h7c593f9_2"
 - "1.2.2--py39hff71179_0"
description: "singularity registry hpc automated addition for fast-edit-distance"
config: {"url": "https://biocontainers.pro/tools/fast-edit-distance", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fast-edit-distance", "latest": {"1.2.2--py39hff71179_0": "sha256:4fb21b8e80fac6ed5be5b8c866e8b5afeb6e75ab15d21fc42601ed8cc2b74df8"}, "tags": {"1.2.1--py310h7c593f9_1": "sha256:3d02efb64342a646935859a8b9deb6b5c629e890252ad35d15dd697a4c2f19a5", "1.2.1--py311hdad781d_1": "sha256:098301cdb18da9f5c5ee05342fe17690f44d142aa31d2bb07e2aeffcbc30da0b", "1.2.1--py310h7c593f9_2": "sha256:dbac3f8a1c4cd8f5d7b733e2fe01d91f4720ef4fd470cf9423c6fe9343d56f29", "1.2.2--py39hff71179_0": "sha256:4fb21b8e80fac6ed5be5b8c866e8b5afeb6e75ab15d21fc42601ed8cc2b74df8"}, "docker": "quay.io/biocontainers/fast-edit-distance", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fast-edit-distance.
singularity registry hpc automated addition for fast-edit-distance
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fast-edit-distance
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fast-edit-distance:1.2.2--py39hff71179_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fast-edit-distance/1.2.2--py39hff71179_0
$ module help quay.io/biocontainers/fast-edit-distance/1.2.2--py39hff71179_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fast-edit-distance-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fast-edit-distance-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fast-edit-distance-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fast-edit-distance-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fast-edit-distance-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fast-edit-distance-inspect-deffile:

```bash
$ singularity inspect -d <container>
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