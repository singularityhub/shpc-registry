---
layout: container
name:  "quay.io/biocontainers/weebill"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/weebill/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/weebill/container.yaml"
updated_at: "2026-08-27 23:27:38.054070"
latest: "0.3.0--hec9b1f2_0"
container_url: "https://biocontainers.pro/tools/weebill"
aliases:
 - "weebill"
versions:
 - "0.3.0--hec9b1f2_0"
description: "singularity registry hpc automated addition for weebill"
config: {"url": "https://biocontainers.pro/tools/weebill", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for weebill", "latest": {"0.3.0--hec9b1f2_0": "sha256:7dd3b6fcb6a012cab7190f8baa6bbf8d58f79b1b9f812dbc34449b21a0f3d737"}, "tags": {"0.3.0--hec9b1f2_0": "sha256:7dd3b6fcb6a012cab7190f8baa6bbf8d58f79b1b9f812dbc34449b21a0f3d737"}, "docker": "quay.io/biocontainers/weebill", "aliases": {"weebill": "/usr/local/bin/weebill"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/weebill.
singularity registry hpc automated addition for weebill
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/weebill
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/weebill:0.3.0--hec9b1f2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/weebill/0.3.0--hec9b1f2_0
$ module help quay.io/biocontainers/weebill/0.3.0--hec9b1f2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### weebill-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### weebill-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### weebill-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### weebill-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### weebill-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### weebill-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### weebill

```bash
$ singularity exec <container> /usr/local/bin/weebill
$ podman run --it --rm --entrypoint /usr/local/bin/weebill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weebill   -v ${PWD} -w ${PWD} <container> -c " $@"
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