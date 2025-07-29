---
layout: container
name:  "quay.io/pawsey/hpc-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/hpc-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/hpc-python/container.yaml"
updated_at: "2025-07-29 04:44:07.942791"
latest: "3.11-ubuntu23.04"
container_url: "https://quay.io/repository/pawsey/hpc-python"
aliases:
 - "python"
 - "python3"
versions:
 - "3.11-ubuntu23.04"
 - "3.11-ubuntu23.04-hdf5mpi"
description: "Base Python images with popular packages for HPC workflows."
config: {"docker": "quay.io/pawsey/hpc-python", "url": "https://quay.io/repository/pawsey/hpc-python", "maintainer": "@marcodelapierre", "description": "Base Python images with popular packages for HPC workflows.", "latest": {"3.11-ubuntu23.04": "sha256:0b374bd5dce385a32ebd57266d1124f74206919dcc82a9b345868fd2cccb5672"}, "tags": {"3.11-ubuntu23.04": "sha256:0b374bd5dce385a32ebd57266d1124f74206919dcc82a9b345868fd2cccb5672", "3.11-ubuntu23.04-hdf5mpi": "sha256:b42b65b2d49bf24c595e23ac0e1b11ac2bccf36d716356493f7b32ef12e35b48"}, "aliases": {"python": "/usr/local/bin/python", "python3": "/usr/local/bin/python3"}, "env": {"PYTHONSTARTUP": "", "PYTHONUSERBASE": ""}, "features": {"home": true}}
---

This module is a singularity container wrapper for quay.io/pawsey/hpc-python.
Base Python images with popular packages for HPC workflows.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/hpc-python
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/hpc-python:3.11-ubuntu23.04
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/hpc-python/3.11-ubuntu23.04
$ module help quay.io/pawsey/hpc-python/3.11-ubuntu23.04
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hpc-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hpc-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hpc-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hpc-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hpc-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hpc-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /usr/local/bin/python3
$ podman run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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