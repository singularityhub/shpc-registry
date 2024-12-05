---
layout: container
name:  "rocm/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocm/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocm/tensorflow/container.yaml"
updated_at: "2024-12-05 04:09:49.977912"
latest: "rocm6.2-py3.9-tf2.16-dev"
container_url: "https://hub.docker.com/r/rocm/tensorflow"
aliases:
 - "python"
 - "python3"
versions:
 - "rocm5.5-tf2.11-dev"
 - "gpg"
 - "latest"
 - "rocm5.6-tf2.12-dev"
 - "rocm5.7-tf2.13-dev"
 - "rocm6.0-tf2.14-dev"
 - "rocm6.1-py3.10-tf2.15-dev"
 - "rocm6.2-py3.9-tf2.16-dev"
description: "Tensorflow with ROCm backend support"
config: {"docker": "rocm/tensorflow", "url": "https://hub.docker.com/r/rocm/tensorflow", "maintainer": "@dipietrantonio", "description": "Tensorflow with ROCm backend support", "latest": {"rocm6.2-py3.9-tf2.16-dev": "sha256:dcdeafe0dcb5b5160c7ab7ef860dc29a95f2d2dd691946497ab6fb549cde8497"}, "tags": {"rocm5.5-tf2.11-dev": "sha256:646dc917033b1c8b69058e7dd8e127bb90b96f178841d3e95b9010bee10c1765", "gpg": "sha256:77be414a2b0f13a23696f846320a3ab03df1da974f7d642456e06f02aaa93544", "latest": "sha256:3d5ba86a2cc3b6a4c2e160f6bffc7c5503e14e2fbb8d9712bc70ec8708f72d8c", "rocm5.6-tf2.12-dev": "sha256:7bbea3f8edf8fd4fb0f1b7f6720910f29aaa31edf51a9fff8624a8d2da6cfefe", "rocm5.7-tf2.13-dev": "sha256:6f995539eebc062aac2b53db40e2b545192d8b032d0deada8c24c6651a7ac332", "rocm6.0-tf2.14-dev": "sha256:aee2c7cde19ed4b3fc4bbd27264b2019656f71020ea9f29eb687fb471a0a60e3", "rocm6.1-py3.10-tf2.15-dev": "sha256:5bb6212c86376d3333be0fc170fef785d8a13a2dc2a3e33649c9a4d86ec38d70", "rocm6.2-py3.9-tf2.16-dev": "sha256:dcdeafe0dcb5b5160c7ab7ef860dc29a95f2d2dd691946497ab6fb549cde8497"}, "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python", "python3": "/usr/bin/python3"}}
---

This module is a singularity container wrapper for rocm/tensorflow.
Tensorflow with ROCm backend support
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocm/tensorflow
```

Or a specific version:

```bash
$ shpc install rocm/tensorflow:rocm6.2-py3.9-tf2.16-dev
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocm/tensorflow/rocm6.2-py3.9-tf2.16-dev
$ module help rocm/tensorflow/rocm6.2-py3.9-tf2.16-dev
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/bin/python
$ podman run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /usr/bin/python3
$ podman run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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