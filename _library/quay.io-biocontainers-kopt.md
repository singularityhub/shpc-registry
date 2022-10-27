---
layout: container
name:  "quay.io/biocontainers/kopt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kopt/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kopt/container.yaml"
updated_at: "2022-10-27 01:04:03.995220"
latest: "0.1.0--pyh145b6a8_2"
container_url: "https://biocontainers.pro/tools/kopt"
aliases:
 - "hyperopt-mongo-worker"
versions:
 - "0.1.0--pyh145b6a8_2"
description: "shpc-registry automated BioContainers addition for kopt"
config: {"url": "https://biocontainers.pro/tools/kopt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kopt", "latest": {"0.1.0--pyh145b6a8_2": "sha256:718867578adabf2f9bf94a160c494fcc0ae40d6b03fbad5497bbe503c9bcb259"}, "tags": {"0.1.0--pyh145b6a8_2": "sha256:718867578adabf2f9bf94a160c494fcc0ae40d6b03fbad5497bbe503c9bcb259"}, "docker": "quay.io/biocontainers/kopt", "aliases": {"hyperopt-mongo-worker": "/usr/local/bin/hyperopt-mongo-worker"}}
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