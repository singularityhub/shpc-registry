---
layout: container
name:  "quay.io/biocontainers/ngless"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngless/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngless/container.yaml"
updated_at: "2022-10-27 00:42:10.579677"
latest: "1.5.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/ngless"
aliases:
 - "ngless"
 - "ngless-wrapped"
versions:
 - "1.5.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for ngless"
config: {"url": "https://biocontainers.pro/tools/ngless", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngless", "latest": {"1.5.0--h9ee0642_0": "sha256:89c76fde148b34728c572790f3a73d2960ccd519d5ad43517cd65f924f7a7eda"}, "tags": {"1.5.0--h9ee0642_0": "sha256:89c76fde148b34728c572790f3a73d2960ccd519d5ad43517cd65f924f7a7eda"}, "docker": "quay.io/biocontainers/ngless", "aliases": {"ngless": "/usr/local/bin/ngless", "ngless-wrapped": "/usr/local/bin/ngless-wrapped"}}
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