---
layout: container
name:  "quay.io/biocontainers/pyslow5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyslow5/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pyslow5/container.yaml"
updated_at: "2022-10-27 01:04:56.425349"
latest: "0.7.0--py39h6471ffd_0"
container_url: "https://biocontainers.pro/tools/pyslow5"

versions:
 - "0.7.0--py39h6471ffd_0"
description: "shpc-registry automated BioContainers addition for pyslow5"
config: {"url": "https://biocontainers.pro/tools/pyslow5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyslow5", "latest": {"0.7.0--py39h6471ffd_0": "sha256:e898c7978c38db51683ec354a8723040cef681c64f6e1f852978963e09eb86e7"}, "tags": {"0.7.0--py39h6471ffd_0": "sha256:e898c7978c38db51683ec354a8723040cef681c64f6e1f852978963e09eb86e7"}, "docker": "quay.io/biocontainers/pyslow5"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyslow5.
shpc-registry automated BioContainers addition for pyslow5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyslow5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyslow5:0.7.0--py39h6471ffd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyslow5/0.7.0--py39h6471ffd_0
$ module help quay.io/biocontainers/pyslow5/0.7.0--py39h6471ffd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyslow5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyslow5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyslow5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyslow5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyslow5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyslow5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pyslow5

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