---
layout: container
name:  "quay.io/biocontainers/yacrd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yacrd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yacrd/container.yaml"
updated_at: "2024-02-17 02:23:13.361444"
latest: "1.0.0--h8bd2d3b_2"
container_url: "https://biocontainers.pro/tools/yacrd"
aliases:
 - "yacrd"
versions:
 - "1.0.0--hc308579_0"
 - "1.0.0--hc308579_1"
 - "1.0.0--h8bd2d3b_2"
description: "shpc-registry automated BioContainers addition for yacrd"
config: {"url": "https://biocontainers.pro/tools/yacrd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yacrd", "latest": {"1.0.0--h8bd2d3b_2": "sha256:ebbdb4f7e8b5b7c421fdcb0fddde7bbac1d3036821dfd235df472a7e295d58ec"}, "tags": {"1.0.0--hc308579_0": "sha256:aa06ab658ee12917d5be9406cd2f7d2f644079d5fcc27b17d28c73bb47780f9e", "1.0.0--hc308579_1": "sha256:8e6e4d501a72126dada2679a48b7d8f73640cf4565a60af981e2dc0116d4a790", "1.0.0--h8bd2d3b_2": "sha256:ebbdb4f7e8b5b7c421fdcb0fddde7bbac1d3036821dfd235df472a7e295d58ec"}, "docker": "quay.io/biocontainers/yacrd", "aliases": {"yacrd": "/usr/local/bin/yacrd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yacrd.
shpc-registry automated BioContainers addition for yacrd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yacrd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yacrd:1.0.0--h8bd2d3b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yacrd/1.0.0--h8bd2d3b_2
$ module help quay.io/biocontainers/yacrd/1.0.0--h8bd2d3b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yacrd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yacrd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yacrd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yacrd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yacrd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yacrd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yacrd

```bash
$ singularity exec <container> /usr/local/bin/yacrd
$ podman run --it --rm --entrypoint /usr/local/bin/yacrd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yacrd   -v ${PWD} -w ${PWD} <container> -c " $@"
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