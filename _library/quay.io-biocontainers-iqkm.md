---
layout: container
name:  "quay.io/biocontainers/iqkm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iqkm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/iqkm/container.yaml"
updated_at: "2022-10-27 00:58:42.351566"
latest: "1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/iqkm"
aliases:
 - "iqkm"
 - "isort-identify-imports"
versions:
 - "1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for iqkm"
config: {"url": "https://biocontainers.pro/tools/iqkm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iqkm", "latest": {"1.0--pyhdfd78af_0": "sha256:f968644320efd8fbec876e3fed40a60ec93ae7dae7609e3f341adf0b7ae26ddb"}, "tags": {"1.0--pyhdfd78af_0": "sha256:f968644320efd8fbec876e3fed40a60ec93ae7dae7609e3f341adf0b7ae26ddb"}, "docker": "quay.io/biocontainers/iqkm", "aliases": {"iqkm": "/usr/local/bin/iqkm", "isort-identify-imports": "/usr/local/bin/isort-identify-imports"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iqkm.
shpc-registry automated BioContainers addition for iqkm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iqkm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iqkm:1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iqkm/1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/iqkm/1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iqkm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iqkm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iqkm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iqkm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iqkm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iqkm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iqkm

```bash
$ singularity exec <container> /usr/local/bin/iqkm
$ podman run --it --rm --entrypoint /usr/local/bin/iqkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
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