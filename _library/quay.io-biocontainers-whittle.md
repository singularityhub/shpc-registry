---
layout: container
name:  "quay.io/biocontainers/whittle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/whittle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/whittle/container.yaml"
updated_at: "2026-08-14 04:56:51.424548"
latest: "0.1.1--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/whittle"
aliases:
 - "whittle"
versions:
 - "0.1.1--hfa8f182_0"
description: "singularity registry hpc automated addition for whittle"
config: {"url": "https://biocontainers.pro/tools/whittle", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for whittle", "latest": {"0.1.1--hfa8f182_0": "sha256:0bd01c4fef407abede42b0e4d650bcf7772bb54617615e30b0757a46265ad0c0"}, "tags": {"0.1.1--hfa8f182_0": "sha256:0bd01c4fef407abede42b0e4d650bcf7772bb54617615e30b0757a46265ad0c0"}, "docker": "quay.io/biocontainers/whittle", "aliases": {"whittle": "/usr/local/bin/whittle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/whittle.
singularity registry hpc automated addition for whittle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/whittle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/whittle:0.1.1--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/whittle/0.1.1--hfa8f182_0
$ module help quay.io/biocontainers/whittle/0.1.1--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### whittle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### whittle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### whittle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### whittle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### whittle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### whittle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### whittle

```bash
$ singularity exec <container> /usr/local/bin/whittle
$ podman run --it --rm --entrypoint /usr/local/bin/whittle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whittle   -v ${PWD} -w ${PWD} <container> -c " $@"
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