---
layout: container
name:  "quay.io/biocontainers/ngless"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngless/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngless/container.yaml"
updated_at: "2023-05-28 03:21:11.226626"
latest: "1.5.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/ngless"
aliases:
 - "ngless"
 - "ngless-wrapped"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "megahit"
 - "megahit_toolkit"
 - "prodigal"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
versions:
 - "1.5.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for ngless"
config: {"url": "https://biocontainers.pro/tools/ngless", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngless", "latest": {"1.5.0--h9ee0642_0": "sha256:89c76fde148b34728c572790f3a73d2960ccd519d5ad43517cd65f924f7a7eda"}, "tags": {"1.5.0--h9ee0642_0": "sha256:89c76fde148b34728c572790f3a73d2960ccd519d5ad43517cd65f924f7a7eda"}, "docker": "quay.io/biocontainers/ngless", "aliases": {"ngless": "/usr/local/bin/ngless", "ngless-wrapped": "/usr/local/bin/ngless-wrapped", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "prodigal": "/usr/local/bin/prodigal", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngless.
shpc-registry automated BioContainers addition for ngless
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngless
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngless:1.5.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngless/1.5.0--h9ee0642_0
$ module help quay.io/biocontainers/ngless/1.5.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngless-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngless-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngless-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngless-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngless-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngless-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngless

```bash
$ singularity exec <container> /usr/local/bin/ngless
$ podman run --it --rm --entrypoint /usr/local/bin/ngless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngless-wrapped

```bash
$ singularity exec <container> /usr/local/bin/ngless-wrapped
$ podman run --it --rm --entrypoint /usr/local/bin/ngless-wrapped   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngless-wrapped   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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