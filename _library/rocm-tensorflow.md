---
layout: container
name:  "rocm/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocm/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocm/tensorflow/container.yaml"
updated_at: "2024-01-09 03:16:19.615568"
latest: "rocm5.7-tf2.13-dev"
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
description: "Tensorflow with ROCm backend support"
config: {"docker": "rocm/tensorflow", "url": "https://hub.docker.com/r/rocm/tensorflow", "maintainer": "@dipietrantonio", "description": "Tensorflow with ROCm backend support", "latest": {"rocm5.7-tf2.13-dev": "sha256:6f995539eebc062aac2b53db40e2b545192d8b032d0deada8c24c6651a7ac332"}, "tags": {"rocm5.5-tf2.11-dev": "sha256:646dc917033b1c8b69058e7dd8e127bb90b96f178841d3e95b9010bee10c1765", "gpg": "sha256:77be414a2b0f13a23696f846320a3ab03df1da974f7d642456e06f02aaa93544", "latest": "sha256:6f995539eebc062aac2b53db40e2b545192d8b032d0deada8c24c6651a7ac332", "rocm5.6-tf2.12-dev": "sha256:7bbea3f8edf8fd4fb0f1b7f6720910f29aaa31edf51a9fff8624a8d2da6cfefe", "rocm5.7-tf2.13-dev": "sha256:6f995539eebc062aac2b53db40e2b545192d8b032d0deada8c24c6651a7ac332"}, "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python", "python3": "/usr/bin/python3"}}
---

This module is a singularity container wrapper for rocm/tensorflow.
Tensorflow with ROCm backend support
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocm/tensorflow
```

Or a specific version:

```bash
$ shpc install rocm/tensorflow:rocm5.7-tf2.13-dev
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocm/tensorflow/rocm5.7-tf2.13-dev
$ module help rocm/tensorflow/rocm5.7-tf2.13-dev
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