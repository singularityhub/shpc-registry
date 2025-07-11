---
layout: container
name:  "quay.io/jupyter/minimal-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/minimal-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/minimal-notebook/container.yaml"
updated_at: "2025-07-11 04:32:22.042804"
latest: "2025-06-23"
container_url: "https://quay.io/repository/jupyter/minimal-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-05-30"
 - "2025-06-23"
description: "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/minimal-notebook", "url": "https://quay.io/repository/jupyter/minimal-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-06-23": "sha256:5e4e24ca25cf1a76c322792fc7915d9839f216867da89f1a1e18e71c9279972a"}, "tags": {"latest": "sha256:5e4e24ca25cf1a76c322792fc7915d9839f216867da89f1a1e18e71c9279972a", "2025-05-30": "sha256:b1e5df5d0147db361f004f898700feffc80a58d09bca567bb93395945a30a8a2", "2025-06-23": "sha256:5e4e24ca25cf1a76c322792fc7915d9839f216867da89f1a1e18e71c9279972a"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/minimal-notebook.
Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/minimal-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/minimal-notebook:2025-06-23
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/minimal-notebook/2025-06-23
$ module help quay.io/jupyter/minimal-notebook/2025-06-23
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimal-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimal-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimal-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimal-notebook-inspect-deffile:

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