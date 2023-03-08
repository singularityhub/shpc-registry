---
layout: container
name:  "quay.io/biocontainers/solvebio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/solvebio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/solvebio/container.yaml"
updated_at: "2023-03-08 21:24:07.353108"
latest: "2.21.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/solvebio"
aliases:
 - "solvebio"
 - "chardetect"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.9.0--py_0"
 - "2.19.0--pyh5e36f6f_0"
 - "2.18.1--pyh5e36f6f_0"
 - "2.17.1--pyh5e36f6f_0"
 - "2.16.0--pyh3252c3a_0"
 - "2.15.0--pyh3252c3a_0"
 - "2.21.0--pyh7cba7a3_0"
 - "2.20.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for solvebio"
config: {"url": "https://biocontainers.pro/tools/solvebio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for solvebio", "latest": {"2.21.0--pyh7cba7a3_0": "sha256:4880a1c5246aa621ac6274b599783ba0f40cc1c64d8eea6d17a92effd3a44c8d"}, "tags": {"2.9.0--py_0": "sha256:259ebad4ec983aeb94bb0f009e12bbfb61aa30370238862a362db1e1214edad4", "2.19.0--pyh5e36f6f_0": "sha256:284eae07e559bd2b55702fea73240658fc433a3adaf8526877c301bc589e2614", "2.18.1--pyh5e36f6f_0": "sha256:7f6755cbdbe23a6da9614fb9bcd0a90d2d35637f4a4125f0bc1a692b2e2e5cce", "2.17.1--pyh5e36f6f_0": "sha256:f5573df4f5deeb476496d73e1873c506c8ed8b16ed7348c3d7f03ce33c039c1b", "2.16.0--pyh3252c3a_0": "sha256:2be079d5ccb8824073283800d719f77c73b9fe78229e03961d7b567b3cc41bb1", "2.15.0--pyh3252c3a_0": "sha256:cf2e8fa075f2f1cd88376bfdf8cb2971cd38b53fee34f2f3664f0d363c32269b", "2.21.0--pyh7cba7a3_0": "sha256:4880a1c5246aa621ac6274b599783ba0f40cc1c64d8eea6d17a92effd3a44c8d", "2.20.0--pyh7cba7a3_0": "sha256:aeb2e306845b7bb7fc2b233d50405952ac686cb042a514cc831a624c70a71ca0"}, "docker": "quay.io/biocontainers/solvebio", "aliases": {"solvebio": "/usr/local/bin/solvebio", "chardetect": "/usr/local/bin/chardetect", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/solvebio.
shpc-registry automated BioContainers addition for solvebio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/solvebio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/solvebio:2.21.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/solvebio/2.21.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/solvebio/2.21.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### solvebio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### solvebio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### solvebio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### solvebio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### solvebio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### solvebio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### solvebio

```bash
$ singularity exec <container> /usr/local/bin/solvebio
$ podman run --it --rm --entrypoint /usr/local/bin/solvebio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/solvebio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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