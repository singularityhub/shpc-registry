---
layout: container
name:  "quay.io/pawsey/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/tensorflow/container.yaml"
updated_at: "2025-03-06 03:30:35.600187"
latest: "2.13-rocm5.7.3"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "python"
 - "python3"
 - "venv"
 - "bash"
versions:
 - "2.12.1.570-rocm5.6.0"
 - "2.13-rocm5.7.3"
description: "Pawsey build of TensorFlow for AMD GPUs."
config: {"docker": "quay.io/pawsey/tensorflow", "url": "https://singularity-hpc.readthedocs.io", "maintainer": "dipietrantonio", "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python3", "python3": "/usr/bin/python3", "venv": "/usr/bin/python3 -m venv --system-site-packages", "bash": "/bin/bash"}, "description": "Pawsey build of TensorFlow for AMD GPUs.", "latest": {"2.13-rocm5.7.3": "sha256:89b76025ac71a29ec11119e0a141c457fb0c528c8f6d04e401de89e79bc65ccd"}, "tags": {"2.12.1.570-rocm5.6.0": "sha256:7ed1455b773cfa21229c69502e7a4c48766ee8791076526fb9782ed4161cd099", "2.13-rocm5.7.3": "sha256:89b76025ac71a29ec11119e0a141c457fb0c528c8f6d04e401de89e79bc65ccd"}}
---

This module is a singularity container wrapper for quay.io/pawsey/tensorflow.
Pawsey build of TensorFlow for AMD GPUs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/tensorflow
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/tensorflow:2.13-rocm5.7.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/tensorflow/2.13-rocm5.7.3
$ module help quay.io/pawsey/tensorflow/2.13-rocm5.7.3
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
$ singularity exec <container> /usr/bin/python3
$ podman run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /usr/bin/python3
$ podman run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### venv

```bash
$ singularity exec <container> /usr/bin/python3 -m venv --system-site-packages
$ podman run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c "-m venv --system-site-packages $@"
$ docker run --it --rm --entrypoint /usr/bin/python3   -v ${PWD} -w ${PWD} <container> -c "-m venv --system-site-packages $@"
```


#### bash

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
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