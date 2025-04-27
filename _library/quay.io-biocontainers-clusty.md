---
layout: container
name:  "quay.io/biocontainers/clusty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clusty/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clusty/container.yaml"
updated_at: "2025-04-27 03:23:42.142925"
latest: "1.2.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/clusty"
aliases:
 - "clusty"
versions:
 - "1.0.0--hdbdd923_1"
 - "1.1.1--hdbdd923_0"
 - "1.1.5--h9ee0642_0"
 - "1.2.0--h9ee0642_0"
description: "singularity registry hpc automated addition for clusty"
config: {"url": "https://biocontainers.pro/tools/clusty", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clusty", "latest": {"1.2.0--h9ee0642_0": "sha256:75bcf205bf7be3d57b6cb35812bb6dac80aedc650eab30bfb5defe73f4617440"}, "tags": {"1.0.0--hdbdd923_1": "sha256:d68ae51f541cd5d7dfa185c25770cbf4cd6f8e96ca1601c07a6ed3bfdbfbccdc", "1.1.1--hdbdd923_0": "sha256:cc6213fb0b6b90e8845377727d19c0258ffc22124c4165d726b24ef983228175", "1.1.5--h9ee0642_0": "sha256:b843fbb6f763bc2e254fba9cd14fac367124c596400c3a2046ae1a23ce623384", "1.2.0--h9ee0642_0": "sha256:75bcf205bf7be3d57b6cb35812bb6dac80aedc650eab30bfb5defe73f4617440"}, "docker": "quay.io/biocontainers/clusty", "aliases": {"clusty": "/usr/local/bin/clusty"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clusty.
singularity registry hpc automated addition for clusty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clusty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clusty:1.2.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clusty/1.2.0--h9ee0642_0
$ module help quay.io/biocontainers/clusty/1.2.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clusty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clusty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clusty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clusty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clusty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clusty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clusty

```bash
$ singularity exec <container> /usr/local/bin/clusty
$ podman run --it --rm --entrypoint /usr/local/bin/clusty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusty   -v ${PWD} -w ${PWD} <container> -c " $@"
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