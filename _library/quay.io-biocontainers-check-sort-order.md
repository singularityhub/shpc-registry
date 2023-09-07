---
layout: container
name:  "quay.io/biocontainers/check-sort-order"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/check-sort-order/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/check-sort-order/container.yaml"
updated_at: "2023-09-07 03:10:48.575560"
latest: "0.0.7--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/check-sort-order"
aliases:
 - "check-sort-order"
versions:
 - "0.0.7--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for check-sort-order"
config: {"url": "https://biocontainers.pro/tools/check-sort-order", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for check-sort-order", "latest": {"0.0.7--h9ee0642_1": "sha256:c39347e2d1de01877d13eb4d6bd7d589869fe8b54ec664927fc7cb08ef0b340d"}, "tags": {"0.0.7--h9ee0642_1": "sha256:c39347e2d1de01877d13eb4d6bd7d589869fe8b54ec664927fc7cb08ef0b340d"}, "docker": "quay.io/biocontainers/check-sort-order", "aliases": {"check-sort-order": "/usr/local/bin/check-sort-order"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/check-sort-order.
shpc-registry automated BioContainers addition for check-sort-order
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/check-sort-order
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/check-sort-order:0.0.7--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/check-sort-order/0.0.7--h9ee0642_1
$ module help quay.io/biocontainers/check-sort-order/0.0.7--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### check-sort-order-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### check-sort-order-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### check-sort-order-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### check-sort-order-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### check-sort-order-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### check-sort-order-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check-sort-order

```bash
$ singularity exec <container> /usr/local/bin/check-sort-order
$ podman run --it --rm --entrypoint /usr/local/bin/check-sort-order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-sort-order   -v ${PWD} -w ${PWD} <container> -c " $@"
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