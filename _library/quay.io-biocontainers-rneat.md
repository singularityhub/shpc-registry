---
layout: container
name:  "quay.io/biocontainers/rneat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rneat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rneat/container.yaml"
updated_at: "2026-07-02 06:55:43.711006"
latest: "1.17.4--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/rneat"
aliases:
 - "rneat"
versions:
 - "1.17.4--hfa8f182_0"
description: "singularity registry hpc automated addition for rneat"
config: {"url": "https://biocontainers.pro/tools/rneat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rneat", "latest": {"1.17.4--hfa8f182_0": "sha256:1585d17ea6495c07fc78c22cb75bf207773de0f8a61476706c52c55145c63965"}, "tags": {"1.17.4--hfa8f182_0": "sha256:1585d17ea6495c07fc78c22cb75bf207773de0f8a61476706c52c55145c63965"}, "docker": "quay.io/biocontainers/rneat", "aliases": {"rneat": "/usr/local/bin/rneat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rneat.
singularity registry hpc automated addition for rneat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rneat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rneat:1.17.4--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rneat/1.17.4--hfa8f182_0
$ module help quay.io/biocontainers/rneat/1.17.4--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rneat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rneat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rneat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rneat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rneat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rneat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rneat

```bash
$ singularity exec <container> /usr/local/bin/rneat
$ podman run --it --rm --entrypoint /usr/local/bin/rneat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rneat   -v ${PWD} -w ${PWD} <container> -c " $@"
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