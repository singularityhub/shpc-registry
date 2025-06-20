---
layout: container
name:  "quay.io/jupyter/tensorflow-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
updated_at: "2025-06-20 03:19:53.052951"
latest: "cuda-388066466d85"
container_url: "https://quay.io/repository/jupyter/tensorflow-notebook"
aliases:
 - "run-notebook"
versions:
 - "latest"
 - "2025-06-02"
 - "cuda-2025-06-02"
 - "cuda-latest"
 - "cuda-388066466d85"
 - "cuda-e57047801c3d"
 - "cuda-afdc8061196e"
 - "cuda-dcecb3155619"
description: "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/tensorflow-notebook", "url": "https://quay.io/repository/jupyter/tensorflow-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks", "latest": {"cuda-388066466d85": "sha256:d8b4f1d67dd6170ef8eff302c22d91e04ea1074ddd3788e9712634e7fa6e1412"}, "tags": {"latest": "sha256:c640236b57d563b5468ea888ff38d8641645071fc0794c64b334da57576399aa", "2025-06-02": "sha256:fcd545494caf7ea38d531512784d380c3efa4c13e635071fc914d7d80ac4f5b6", "cuda-2025-06-02": "sha256:99496ed0740f617341cc6578da68c69b746828f5145a9d76bc1d2188ece34d3f", "cuda-latest": "sha256:abab0c908a565fd7748c5fb4a1ca2feffa6198028a4b160e9b4668b26c113d50", "cuda-388066466d85": "sha256:d8b4f1d67dd6170ef8eff302c22d91e04ea1074ddd3788e9712634e7fa6e1412", "cuda-e57047801c3d": "sha256:d6b79dc162df12bc1d5ee078985fdc5fc3bba9a79e82c52b1763a17c51267d23", "cuda-afdc8061196e": "sha256:de4ef91b24f70718c1eb2500d7a31f623f7f276647e34ca80b860ca93382c133", "cuda-dcecb3155619": "sha256:88368171db064ba1c525b74163f7fdab5c09152a22c32635fc4e8b3e7e25d0b5"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/tensorflow-notebook.
Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/tensorflow-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/tensorflow-notebook:cuda-388066466d85
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/tensorflow-notebook/cuda-388066466d85
$ module help quay.io/jupyter/tensorflow-notebook/cuda-388066466d85
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