---
layout: container
name:  "quay.io/biocontainers/kopt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kopt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kopt/container.yaml"
updated_at: "2023-05-27 03:18:04.409723"
latest: "0.1.0--pyh145b6a8_2"
container_url: "https://biocontainers.pro/tools/kopt"
aliases:
 - "hyperopt-mongo-worker"
 - "theano-cache"
 - "theano-nose"
 - "freeze_graph"
 - "mako-render"
 - "tf_upgrade_v2"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "toco_from_protos"
 - "tensorboard"
versions:
 - "0.1.0--pyh145b6a8_2"
description: "shpc-registry automated BioContainers addition for kopt"
config: {"url": "https://biocontainers.pro/tools/kopt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kopt", "latest": {"0.1.0--pyh145b6a8_2": "sha256:718867578adabf2f9bf94a160c494fcc0ae40d6b03fbad5497bbe503c9bcb259"}, "tags": {"0.1.0--pyh145b6a8_2": "sha256:718867578adabf2f9bf94a160c494fcc0ae40d6b03fbad5497bbe503c9bcb259"}, "docker": "quay.io/biocontainers/kopt", "aliases": {"hyperopt-mongo-worker": "/usr/local/bin/hyperopt-mongo-worker", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "freeze_graph": "/usr/local/bin/freeze_graph", "mako-render": "/usr/local/bin/mako-render", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "toco_from_protos": "/usr/local/bin/toco_from_protos", "tensorboard": "/usr/local/bin/tensorboard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kopt.
shpc-registry automated BioContainers addition for kopt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kopt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kopt:0.1.0--pyh145b6a8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kopt/0.1.0--pyh145b6a8_2
$ module help quay.io/biocontainers/kopt/0.1.0--pyh145b6a8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kopt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kopt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kopt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kopt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kopt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kopt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hyperopt-mongo-worker

```bash
$ singularity exec <container> /usr/local/bin/hyperopt-mongo-worker
$ podman run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-cache

```bash
$ singularity exec <container> /usr/local/bin/theano-cache
$ podman run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-nose

```bash
$ singularity exec <container> /usr/local/bin/theano-nose
$ podman run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco_from_protos

```bash
$ singularity exec <container> /usr/local/bin/toco_from_protos
$ podman run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
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