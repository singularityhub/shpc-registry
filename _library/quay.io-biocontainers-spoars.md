---
layout: container
name:  "quay.io/biocontainers/spoars"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spoars/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spoars/container.yaml"
updated_at: "2026-08-12 04:38:47.805893"
latest: "0.1.3--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/spoars"
aliases:
 - "spoars"
versions:
 - "0.1.3--hfa8f182_0"
description: "singularity registry hpc automated addition for spoars"
config: {"url": "https://biocontainers.pro/tools/spoars", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for spoars", "latest": {"0.1.3--hfa8f182_0": "sha256:a28347cccd80f24f4be8161ba8fef75842026f8f2ad7c22662b046212c24c90f"}, "tags": {"0.1.3--hfa8f182_0": "sha256:a28347cccd80f24f4be8161ba8fef75842026f8f2ad7c22662b046212c24c90f"}, "docker": "quay.io/biocontainers/spoars", "aliases": {"spoars": "/usr/local/bin/spoars"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spoars.
singularity registry hpc automated addition for spoars
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spoars
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spoars:0.1.3--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spoars/0.1.3--hfa8f182_0
$ module help quay.io/biocontainers/spoars/0.1.3--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spoars-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spoars-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spoars-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spoars-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spoars-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spoars-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spoars

```bash
$ singularity exec <container> /usr/local/bin/spoars
$ podman run --it --rm --entrypoint /usr/local/bin/spoars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spoars   -v ${PWD} -w ${PWD} <container> -c " $@"
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