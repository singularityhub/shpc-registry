---
layout: container
name:  "quay.io/biocontainers/qfilt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/qfilt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/qfilt/container.yaml"
updated_at: "2023-05-25 03:13:26.694062"
latest: "0.0.1--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/qfilt"
aliases:
 - "qfilt"
versions:
 - "0.0.1--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for qfilt"
config: {"url": "https://biocontainers.pro/tools/qfilt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for qfilt", "latest": {"0.0.1--h9f5acd7_4": "sha256:ac1e2fba0d07cf02a05b695e45b038ccd655d2d2a300448f9047ac32849a7cf4"}, "tags": {"0.0.1--h9f5acd7_4": "sha256:ac1e2fba0d07cf02a05b695e45b038ccd655d2d2a300448f9047ac32849a7cf4"}, "docker": "quay.io/biocontainers/qfilt", "aliases": {"qfilt": "/usr/local/bin/qfilt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/qfilt.
shpc-registry automated BioContainers addition for qfilt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/qfilt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/qfilt:0.0.1--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/qfilt/0.0.1--h9f5acd7_4
$ module help quay.io/biocontainers/qfilt/0.0.1--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qfilt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qfilt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qfilt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qfilt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qfilt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qfilt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qfilt

```bash
$ singularity exec <container> /usr/local/bin/qfilt
$ podman run --it --rm --entrypoint /usr/local/bin/qfilt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qfilt   -v ${PWD} -w ${PWD} <container> -c " $@"
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