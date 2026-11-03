---
layout: container
name:  "quay.io/biocontainers/lrcorrect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrcorrect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrcorrect/container.yaml"
updated_at: "2026-11-03 09:32:53.242677"
latest: "0.1.0--hf1b6044_0"
container_url: "https://biocontainers.pro/tools/lrcorrect"
aliases:
 - "lrcorrect"
versions:
 - "0.1.0--hf1b6044_0"
description: "singularity registry hpc automated addition for lrcorrect"
config: {"url": "https://biocontainers.pro/tools/lrcorrect", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lrcorrect", "latest": {"0.1.0--hf1b6044_0": "sha256:f81cab77e6e875ad7fdd6f62635bd9d0cd70b140c363f071c2a620eb5d5db47d"}, "tags": {"0.1.0--hf1b6044_0": "sha256:f81cab77e6e875ad7fdd6f62635bd9d0cd70b140c363f071c2a620eb5d5db47d"}, "docker": "quay.io/biocontainers/lrcorrect", "aliases": {"lrcorrect": "/usr/local/bin/lrcorrect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrcorrect.
singularity registry hpc automated addition for lrcorrect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrcorrect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrcorrect:0.1.0--hf1b6044_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrcorrect/0.1.0--hf1b6044_0
$ module help quay.io/biocontainers/lrcorrect/0.1.0--hf1b6044_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrcorrect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrcorrect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrcorrect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrcorrect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrcorrect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrcorrect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lrcorrect

```bash
$ singularity exec <container> /usr/local/bin/lrcorrect
$ podman run --it --rm --entrypoint /usr/local/bin/lrcorrect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrcorrect   -v ${PWD} -w ${PWD} <container> -c " $@"
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