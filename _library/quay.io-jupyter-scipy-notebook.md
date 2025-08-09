---
layout: container
name:  "quay.io/jupyter/scipy-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/scipy-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/scipy-notebook/container.yaml"
updated_at: "2025-08-09 03:22:12.269863"
latest: "2025-07-14"
container_url: "https://quay.io/repository/jupyter/scipy-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "2025-07-14"
 - "2025-06-23"
description: "Jupyter SciPy Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/scipy-notebook", "url": "https://quay.io/repository/jupyter/scipy-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter SciPy Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-07-14": "sha256:db4f57dc02e79f2694c07da779d2eae3d5155bc72fac02327d80a2ef16e9543b"}, "tags": {"latest": "sha256:db4f57dc02e79f2694c07da779d2eae3d5155bc72fac02327d80a2ef16e9543b", "2025-06-02": "sha256:08e4c32e10df101bcee46fba936b728721cf574c5d0153157c806dc96e56d8cf", "2025-07-14": "sha256:db4f57dc02e79f2694c07da779d2eae3d5155bc72fac02327d80a2ef16e9543b", "2025-06-23": "sha256:edfd03e53938fc956cc8054cbf7cccae42059e6d72e47777a5a6031f26c8cb63"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/scipy-notebook.
Jupyter SciPy Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/scipy-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/scipy-notebook:2025-07-14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/scipy-notebook/2025-07-14
$ module help quay.io/jupyter/scipy-notebook/2025-07-14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scipy-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scipy-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scipy-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scipy-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scipy-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scipy-notebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-notebook

```bash
$ singularity exec <container> jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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