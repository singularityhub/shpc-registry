---
layout: container
name:  "quay.io/biocontainers/r-sigminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sigminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sigminer/container.yaml"
updated_at: "2025-04-17 03:11:25.084260"
latest: "2.3.1--r43h21a89ab_1"
container_url: "https://biocontainers.pro/tools/r-sigminer"
aliases:
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.1.7--r41hecf12ef_1"
 - "2.1.9--r42hecf12ef_1"
 - "2.2.0--r42h21a89ab_1"
 - "2.1.9--r42h21a89ab_2"
 - "2.2.2--r43h21a89ab_0"
 - "2.3.0--r43h21a89ab_0"
 - "2.3.1--r43h21a89ab_0"
 - "2.3.1--r43h21a89ab_1"
description: "shpc-registry automated BioContainers addition for r-sigminer"
config: {"url": "https://biocontainers.pro/tools/r-sigminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sigminer", "latest": {"2.3.1--r43h21a89ab_1": "sha256:f32a2d8d475ac95f672bfa46fb4ee1f6495a1ea8bce3e85181c9b52347d8a65a"}, "tags": {"2.1.7--r41hecf12ef_1": "sha256:d1b85332c383412d0c463b0ce4459fa6078b504299bcdfadf4536f7ca318c366", "2.1.9--r42hecf12ef_1": "sha256:b9f51c2a7726724e4d7f15d7e1002b31a402e89cba537c5b10c3d269d4dc862b", "2.2.0--r42h21a89ab_1": "sha256:c067526ea1c51809dd45e2f14f613d266f2d4f2417094b6a026c359c66784147", "2.1.9--r42h21a89ab_2": "sha256:32fda439bfa9ed2858588f5d5912e3015c898c78e3296628d117ec83323debe9", "2.2.2--r43h21a89ab_0": "sha256:184cdc81a9c81248aa7f6dc323148dc9825078c6a0c68d3135ddbcae78a63125", "2.3.0--r43h21a89ab_0": "sha256:6fa4ac6d95429a371acc886b7a7c2ef4a42e8ab8c67a43610c27723990186835", "2.3.1--r43h21a89ab_0": "sha256:4986a0266b8ccb3f03a54da628ccd84ae9f1974e9c16ca3a5b2392f1e5780c77", "2.3.1--r43h21a89ab_1": "sha256:f32a2d8d475ac95f672bfa46fb4ee1f6495a1ea8bce3e85181c9b52347d8a65a"}, "docker": "quay.io/biocontainers/r-sigminer", "aliases": {"f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sigminer.
shpc-registry automated BioContainers addition for r-sigminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sigminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sigminer:2.3.1--r43h21a89ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sigminer/2.3.1--r43h21a89ab_1
$ module help quay.io/biocontainers/r-sigminer/2.3.1--r43h21a89ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sigminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sigminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sigminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sigminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sigminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sigminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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