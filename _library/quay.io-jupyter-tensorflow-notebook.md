---
layout: container
name:  "quay.io/jupyter/tensorflow-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
updated_at: "2025-06-13 03:20:56.068028"
latest: "2025-06-02"
container_url: "https://quay.io/repository/jupyter/tensorflow-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "cuda-2025-06-02"
description: "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/tensorflow-notebook", "url": "https://quay.io/repository/jupyter/tensorflow-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2025-06-02": "sha256:fcd545494caf7ea38d531512784d380c3efa4c13e635071fc914d7d80ac4f5b6"}, "tags": {"latest": "sha256:fcd545494caf7ea38d531512784d380c3efa4c13e635071fc914d7d80ac4f5b6", "2025-06-02": "sha256:fcd545494caf7ea38d531512784d380c3efa4c13e635071fc914d7d80ac4f5b6", "cuda-2025-06-02": "sha256:99496ed0740f617341cc6578da68c69b746828f5145a9d76bc1d2188ece34d3f"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/tensorflow-notebook.
Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/tensorflow-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/tensorflow-notebook:2025-06-02
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/tensorflow-notebook/2025-06-02
$ module help quay.io/jupyter/tensorflow-notebook/2025-06-02
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-notebook-inspect-deffile:

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