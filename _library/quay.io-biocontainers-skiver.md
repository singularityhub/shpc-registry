---
layout: container
name:  "quay.io/biocontainers/skiver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skiver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skiver/container.yaml"
updated_at: "2026-08-18 02:58:53.031777"
latest: "0.3.1--hec9b1f2_0"
container_url: "https://biocontainers.pro/tools/skiver"
aliases:
 - "skiver"
versions:
 - "0.3.1--hec9b1f2_0"
description: "singularity registry hpc automated addition for skiver"
config: {"url": "https://biocontainers.pro/tools/skiver", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skiver", "latest": {"0.3.1--hec9b1f2_0": "sha256:6c5bc7d3bb904dcfda34aaf51a78afb0b22deb5edb65bbae38f957e7d8e480d2"}, "tags": {"0.3.1--hec9b1f2_0": "sha256:6c5bc7d3bb904dcfda34aaf51a78afb0b22deb5edb65bbae38f957e7d8e480d2"}, "docker": "quay.io/biocontainers/skiver", "aliases": {"skiver": "/usr/local/bin/skiver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skiver.
singularity registry hpc automated addition for skiver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skiver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skiver:0.3.1--hec9b1f2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skiver/0.3.1--hec9b1f2_0
$ module help quay.io/biocontainers/skiver/0.3.1--hec9b1f2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skiver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skiver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skiver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skiver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skiver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skiver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skiver

```bash
$ singularity exec <container> /usr/local/bin/skiver
$ podman run --it --rm --entrypoint /usr/local/bin/skiver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skiver   -v ${PWD} -w ${PWD} <container> -c " $@"
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