---
layout: container
name:  "amdih/pytorch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amdih/pytorch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amdih/pytorch/container.yaml"
updated_at: "2024-07-29 03:26:21.276172"
latest: "rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0"
container_url: "https://www.amd.com/en/technologies/infinity-hub/pytorch"
aliases:
 - "python3"
 - "python"
versions:
 - "rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0"
description: "PyTorch is a GPU accelerated tensor computational framework with a Python front end."
config: {"docker": "amdih/pytorch", "url": "https://www.amd.com/en/technologies/infinity-hub/pytorch", "description": "PyTorch is a GPU accelerated tensor computational framework with a Python front end.", "maintainer": "@cristiandipietrantonio", "latest": {"rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0": "sha256:b075da4b74e9349e3fd9e38695c5800f391f1aec414f80d3846f67e21c70c0ce"}, "tags": {"rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0": "sha256:b075da4b74e9349e3fd9e38695c5800f391f1aec414f80d3846f67e21c70c0ce"}, "aliases": [{"name": "python3", "command": "/opt/conda/bin/python3"}, {"name": "python", "command": "/opt/conda/bin/python"}]}
---

This module is a singularity container wrapper for amdih/pytorch.
PyTorch is a GPU accelerated tensor computational framework with a Python front end.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amdih/pytorch
```

Or a specific version:

```bash
$ shpc install amdih/pytorch:rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amdih/pytorch/rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0
$ module help amdih/pytorch/rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0
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


#### python3

```bash
$ singularity exec <container> /opt/conda/bin/python3
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python

```bash
$ singularity exec <container> /opt/conda/bin/python
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