---
layout: container
name:  "quay.io/biocontainers/cansnper2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cansnper2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cansnper2/container.yaml"
updated_at: "2022-10-27 01:14:56.838363"
latest: "2.0.6--py_0"
container_url: "https://biocontainers.pro/tools/cansnper2"
aliases:
 - "CanSNPer2"
 - "CanSNPer2-database"
 - "CanSNPer2-download"
 - "CanSNPer2-test"
 - "flextaxd"
 - "flextaxd-create"
 - "progressiveMauve"
versions:
 - "2.0.6--py_0"
description: "shpc-registry automated BioContainers addition for cansnper2"
config: {"url": "https://biocontainers.pro/tools/cansnper2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cansnper2", "latest": {"2.0.6--py_0": "sha256:970881caf9bf51f6e6340a5d4a052b69a3c56ad20cafd7fdb74842099a074aa8"}, "tags": {"2.0.6--py_0": "sha256:970881caf9bf51f6e6340a5d4a052b69a3c56ad20cafd7fdb74842099a074aa8"}, "docker": "quay.io/biocontainers/cansnper2", "aliases": {"CanSNPer2": "/usr/local/bin/CanSNPer2", "CanSNPer2-database": "/usr/local/bin/CanSNPer2-database", "CanSNPer2-download": "/usr/local/bin/CanSNPer2-download", "CanSNPer2-test": "/usr/local/bin/CanSNPer2-test", "flextaxd": "/usr/local/bin/flextaxd", "flextaxd-create": "/usr/local/bin/flextaxd-create", "progressiveMauve": "/usr/local/bin/progressiveMauve"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cansnper2.
shpc-registry automated BioContainers addition for cansnper2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cansnper2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cansnper2:2.0.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cansnper2/2.0.6--py_0
$ module help quay.io/biocontainers/cansnper2/2.0.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cansnper2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cansnper2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cansnper2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cansnper2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cansnper2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cansnper2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CanSNPer2

```bash
$ singularity exec <container> /usr/local/bin/CanSNPer2
$ podman run --it --rm --entrypoint /usr/local/bin/CanSNPer2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CanSNPer2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CanSNPer2-database

```bash
$ singularity exec <container> /usr/local/bin/CanSNPer2-database
$ podman run --it --rm --entrypoint /usr/local/bin/CanSNPer2-database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CanSNPer2-database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CanSNPer2-download

```bash
$ singularity exec <container> /usr/local/bin/CanSNPer2-download
$ podman run --it --rm --entrypoint /usr/local/bin/CanSNPer2-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CanSNPer2-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CanSNPer2-test

```bash
$ singularity exec <container> /usr/local/bin/CanSNPer2-test
$ podman run --it --rm --entrypoint /usr/local/bin/CanSNPer2-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CanSNPer2-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flextaxd

```bash
$ singularity exec <container> /usr/local/bin/flextaxd
$ podman run --it --rm --entrypoint /usr/local/bin/flextaxd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flextaxd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flextaxd-create

```bash
$ singularity exec <container> /usr/local/bin/flextaxd-create
$ podman run --it --rm --entrypoint /usr/local/bin/flextaxd-create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flextaxd-create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### progressiveMauve

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauve
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
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