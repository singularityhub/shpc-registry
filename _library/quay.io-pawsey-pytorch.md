---
layout: container
name:  "quay.io/pawsey/pytorch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/pytorch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/pytorch/container.yaml"
updated_at: "2025-09-16 03:46:48.165915"
latest: "2.7.1-rocm6.3.3"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "python"
 - "python3"
 - "venv"
 - "bash"
versions:
 - "2.7.1-rocm6.3.3"
 - "2.6.0-rocm6.2.2"
 - "2.2.0-rocm5.6.0"
 - "2.1.2-rocm5.6.0"
 - "2.1.0-rocm5.6.0"
 - "2.2.0-rocm5.7.3"
description: "Pawsey build of PyTorch for AMD GPUs."
config: {"docker": "quay.io/pawsey/pytorch", "url": "https://singularity-hpc.readthedocs.io", "maintainer": "dipietrantonio", "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python3", "python3": "/usr/bin/python3", "venv": "/usr/bin/python3 -m venv --system-site-packages", "bash": "/bin/bash"}, "description": "Pawsey build of PyTorch for AMD GPUs.", "latest": {"2.7.1-rocm6.3.3": "sha256:c595ccd9bd0dcb2809b543b9db6520a148881763213ea51b38780e93ab2ae08a"}, "tags": {"2.7.1-rocm6.3.3": "sha256:c595ccd9bd0dcb2809b543b9db6520a148881763213ea51b38780e93ab2ae08a", "2.6.0-rocm6.2.2": "sha256:ac1a258c78075b0e76eb52c6c79b46ce3def9fe5a66d50726ebd39e81577ab0f", "2.2.0-rocm5.6.0": "sha256:148b1d0842cd70acd6cc4b5d3cd2da7a426f56442317d2b722915baf82d7f5ff", "2.1.2-rocm5.6.0": "sha256:d8f91fb847ff2f3a38c091e5d69a628cd7637739ab90db5ab42e596d67a48073", "2.1.0-rocm5.6.0": "sha256:3dbe6711f170d409cba0e25577859799e97eccb80c3d1b8b6df5bd6cf8c0aea6", "2.2.0-rocm5.7.3": "sha256:378f81d0c2cd1a85723bcad7ada4991d2a87bb5328199966e766031733b7dd8e"}}
---

This module is a singularity container wrapper for quay.io/pawsey/pytorch.
Pawsey build of PyTorch for AMD GPUs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/pytorch
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/pytorch:2.7.1-rocm6.3.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/pytorch/2.7.1-rocm6.3.3
$ module help quay.io/pawsey/pytorch/2.7.1-rocm6.3.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytorch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytorch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytorch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytorch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytorch-inspect-deffile:

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