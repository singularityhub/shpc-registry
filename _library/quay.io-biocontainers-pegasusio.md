---
layout: container
name:  "quay.io/biocontainers/pegasusio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pegasusio/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pegasusio/container.yaml"
updated_at: "2022-10-27 01:05:41.228698"
latest: "0.5.0--py39h38f01e4_0"
container_url: "https://biocontainers.pro/tools/pegasusio"
aliases:
 - "pegasusio"
versions:
 - "0.5.0--py39h38f01e4_0"
description: "shpc-registry automated BioContainers addition for pegasusio"
config: {"url": "https://biocontainers.pro/tools/pegasusio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pegasusio", "latest": {"0.5.0--py39h38f01e4_0": "sha256:661d999a3ff8fc343d8d85e8313be7ead9827680d4a2918202b013bc4f55a5b8"}, "tags": {"0.5.0--py39h38f01e4_0": "sha256:661d999a3ff8fc343d8d85e8313be7ead9827680d4a2918202b013bc4f55a5b8"}, "docker": "quay.io/biocontainers/pegasusio", "aliases": {"pegasusio": "/usr/local/bin/pegasusio"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pegasusio.
shpc-registry automated BioContainers addition for pegasusio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pegasusio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pegasusio:0.5.0--py39h38f01e4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pegasusio/0.5.0--py39h38f01e4_0
$ module help quay.io/biocontainers/pegasusio/0.5.0--py39h38f01e4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pegasusio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pegasusio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pegasusio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pegasusio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pegasusio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pegasusio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pegasusio

```bash
$ singularity exec <container> /usr/local/bin/pegasusio
$ podman run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
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