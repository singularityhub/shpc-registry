---
layout: container
name:  "quay.io/biocontainers/grz-check-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-check-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-check-python/container.yaml"
updated_at: "2026-06-18 07:14:38.206497"
latest: "0.3.0--py312hf7f01f6_1"
container_url: "https://biocontainers.pro/tools/grz-check-python"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.3.0--py312hf7f01f6_1"
description: "singularity registry hpc automated addition for grz-check-python"
config: {"url": "https://biocontainers.pro/tools/grz-check-python", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-check-python", "latest": {"0.3.0--py312hf7f01f6_1": "sha256:e993deecef1602779c394eac4a29385e6ac1abb6ba0d36274f74e87c6c5cacd2"}, "tags": {"0.3.0--py312hf7f01f6_1": "sha256:e993deecef1602779c394eac4a29385e6ac1abb6ba0d36274f74e87c6c5cacd2"}, "docker": "quay.io/biocontainers/grz-check-python", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-check-python.
singularity registry hpc automated addition for grz-check-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-check-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-check-python:0.3.0--py312hf7f01f6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-check-python/0.3.0--py312hf7f01f6_1
$ module help quay.io/biocontainers/grz-check-python/0.3.0--py312hf7f01f6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-check-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-check-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-check-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-check-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-check-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-check-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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