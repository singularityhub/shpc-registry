---
layout: container
name:  "quay.io/biocontainers/cansnper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cansnper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cansnper/container.yaml"
updated_at: "2023-11-26 03:09:58.047671"
latest: "1.0.10--py_1"
container_url: "https://biocontainers.pro/tools/cansnper"

versions:
 - "1.0.10--py_1"
description: "shpc-registry automated BioContainers addition for cansnper"
config: {"url": "https://biocontainers.pro/tools/cansnper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cansnper", "latest": {"1.0.10--py_1": "sha256:62aae79a2b239197a189b4d9c5b090602722f16ba9af440247b37c402f4ddc63"}, "tags": {"1.0.10--py_1": "sha256:62aae79a2b239197a189b4d9c5b090602722f16ba9af440247b37c402f4ddc63"}, "docker": "quay.io/biocontainers/cansnper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/cansnper.
shpc-registry automated BioContainers addition for cansnper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cansnper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cansnper:1.0.10--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cansnper/1.0.10--py_1
$ module help quay.io/biocontainers/cansnper/1.0.10--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cansnper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cansnper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cansnper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cansnper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cansnper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cansnper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cansnper

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