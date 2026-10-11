---
layout: container
name:  "quay.io/biocontainers/skope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skope/container.yaml"
updated_at: "2026-10-11 09:00:10.824062"
latest: "0.5.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/skope"
aliases:
 - "skope"
versions:
 - "0.5.0--hfa8f182_0"
description: "singularity registry hpc automated addition for skope"
config: {"url": "https://biocontainers.pro/tools/skope", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skope", "latest": {"0.5.0--hfa8f182_0": "sha256:a10ed21e0d58386b819c2e4f60a861327c2f52721910e25224e647208e275ce8"}, "tags": {"0.5.0--hfa8f182_0": "sha256:a10ed21e0d58386b819c2e4f60a861327c2f52721910e25224e647208e275ce8"}, "docker": "quay.io/biocontainers/skope", "aliases": {"skope": "/usr/local/bin/skope"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skope.
singularity registry hpc automated addition for skope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skope:0.5.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skope/0.5.0--hfa8f182_0
$ module help quay.io/biocontainers/skope/0.5.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skope

```bash
$ singularity exec <container> /usr/local/bin/skope
$ podman run --it --rm --entrypoint /usr/local/bin/skope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skope   -v ${PWD} -w ${PWD} <container> -c " $@"
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