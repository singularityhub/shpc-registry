---
layout: container
name:  "quay.io/biocontainers/amplify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplify/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amplify/container.yaml"
updated_at: "2024-08-25 02:48:12.573271"
latest: "2.0.0--py36hdfd78af_1"
container_url: "https://biocontainers.pro/tools/amplify"
aliases:
 - "AMPlify"
 - "train_amplify"
 - "theano-cache"
 - "theano-nose"
 - "freeze_graph"
 - "mako-render"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "toco_from_protos"
 - "tensorboard"
 - "markdown_py"
versions:
 - "1.1.0--hdfd78af_0"
 - "2.0.0--py36hdfd78af_0"
 - "2.0.0--py36hdfd78af_1"
description: "shpc-registry automated BioContainers addition for amplify"
config: {"url": "https://biocontainers.pro/tools/amplify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for amplify", "latest": {"2.0.0--py36hdfd78af_1": "sha256:57d0feb347d4c221777dade97279f94989b75c77f5a5101e8da0a2a1fb2742fa"}, "tags": {"1.1.0--hdfd78af_0": "sha256:787ca694b922f8ee6313d2df2b429ad62940444f8ebc60edc1f9b5e283a24928", "2.0.0--py36hdfd78af_0": "sha256:4202d742a883a4b5e76044e32d34320b95221add3fd18e8274cb3bc3b511cd11", "2.0.0--py36hdfd78af_1": "sha256:57d0feb347d4c221777dade97279f94989b75c77f5a5101e8da0a2a1fb2742fa"}, "docker": "quay.io/biocontainers/amplify", "aliases": {"AMPlify": "/usr/local/bin/AMPlify", "train_amplify": "/usr/local/bin/train_amplify", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "freeze_graph": "/usr/local/bin/freeze_graph", "mako-render": "/usr/local/bin/mako-render", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "toco_from_protos": "/usr/local/bin/toco_from_protos", "tensorboard": "/usr/local/bin/tensorboard", "markdown_py": "/usr/local/bin/markdown_py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplify.
shpc-registry automated BioContainers addition for amplify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplify:2.0.0--py36hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplify/2.0.0--py36hdfd78af_1
$ module help quay.io/biocontainers/amplify/2.0.0--py36hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMPlify

```bash
$ singularity exec <container> /usr/local/bin/AMPlify
$ podman run --it --rm --entrypoint /usr/local/bin/AMPlify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMPlify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_amplify

```bash
$ singularity exec <container> /usr/local/bin/train_amplify
$ podman run --it --rm --entrypoint /usr/local/bin/train_amplify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_amplify   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
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