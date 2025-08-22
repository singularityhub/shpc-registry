---
layout: container
name:  "quay.io/jupyter/tensorflow-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/jupyter/tensorflow-notebook/container.yaml"
updated_at: "2025-08-22 03:10:15.183120"
latest: "cuda-b74418220768"
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
 - "cuda-b74418220768"
 - "cuda-ac8453913caf"
 - "cuda-aabaa5807262"
description: "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "quay.io/jupyter/tensorflow-notebook", "url": "https://quay.io/repository/jupyter/tensorflow-notebook", "maintainer": "@HasseJohansen", "description": "Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks", "latest": {"cuda-b74418220768": "sha256:6104812c40306416b261d0bdded3a5c3130ab8fbeb6a249f1637476926d68599"}, "tags": {"latest": "sha256:a525055401d349d3754f6940e821eb1256997cd4f402eeff17007fefd9304302", "2025-06-02": "sha256:fcd545494caf7ea38d531512784d380c3efa4c13e635071fc914d7d80ac4f5b6", "cuda-2025-06-02": "sha256:99496ed0740f617341cc6578da68c69b746828f5145a9d76bc1d2188ece34d3f", "cuda-latest": "sha256:606009c6b693cce8da7bbeed7ca4e6162746144bf61bbbf6682464afad099655", "cuda-388066466d85": "sha256:d8b4f1d67dd6170ef8eff302c22d91e04ea1074ddd3788e9712634e7fa6e1412", "cuda-e57047801c3d": "sha256:d6b79dc162df12bc1d5ee078985fdc5fc3bba9a79e82c52b1763a17c51267d23", "cuda-afdc8061196e": "sha256:de4ef91b24f70718c1eb2500d7a31f623f7f276647e34ca80b860ca93382c133", "cuda-dcecb3155619": "sha256:88368171db064ba1c525b74163f7fdab5c09152a22c32635fc4e8b3e7e25d0b5", "cuda-b74418220768": "sha256:6104812c40306416b261d0bdded3a5c3130ab8fbeb6a249f1637476926d68599", "cuda-ac8453913caf": "sha256:93cca0b900f954e4ad6ce3fc9e26defa31bdd7860450a21851864099fd1d1839", "cuda-aabaa5807262": "sha256:13402ab4a90cc23bfd163175bbfb467620530ebcb61489e96c16106bb7b2146b"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for quay.io/jupyter/tensorflow-notebook.
Jupyter TensorFlow Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/jupyter/tensorflow-notebook
```

Or a specific version:

```bash
$ shpc install quay.io/jupyter/tensorflow-notebook:cuda-b74418220768
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/jupyter/tensorflow-notebook/cuda-b74418220768
$ module help quay.io/jupyter/tensorflow-notebook/cuda-b74418220768
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