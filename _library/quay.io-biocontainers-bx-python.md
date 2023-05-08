---
layout: container
name:  "quay.io/biocontainers/bx-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bx-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bx-python/container.yaml"
updated_at: "2023-05-08 04:22:40.986452"
latest: "0.8.11--py36h5e0341f_0"
container_url: "https://biocontainers.pro/tools/bx-python"

versions:
 - "0.8.9--py27h54ae540_2"
 - "0.8.11--py36h5e0341f_0"
description: "shpc-registry automated BioContainers addition for bx-python"
config: {"url": "https://biocontainers.pro/tools/bx-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bx-python", "latest": {"0.8.11--py36h5e0341f_0": "sha256:c46b0e7f726f61b22d6cfbd8abe65bcebdd33b9ee018c42808d012e078332ad0"}, "tags": {"0.8.9--py27h54ae540_2": "sha256:cc1f109a9aabe9943ab6df613d5aed5bdd0e6e88a72853fb7171b8de51dcda66", "0.8.11--py36h5e0341f_0": "sha256:c46b0e7f726f61b22d6cfbd8abe65bcebdd33b9ee018c42808d012e078332ad0"}, "docker": "quay.io/biocontainers/bx-python"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bx-python.
shpc-registry automated BioContainers addition for bx-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bx-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bx-python:0.8.11--py36h5e0341f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bx-python/0.8.11--py36h5e0341f_0
$ module help quay.io/biocontainers/bx-python/0.8.11--py36h5e0341f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bx-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bx-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bx-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bx-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bx-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bx-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bx-python

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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