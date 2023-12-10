---
layout: container
name:  "quay.io/biocontainers/genomeconstellation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomeconstellation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomeconstellation/container.yaml"
updated_at: "2023-12-10 02:50:13.751945"
latest: "0.21.1--h21ec9f0_4"
container_url: "https://biocontainers.pro/tools/genomeconstellation"
aliases:
 - "jgi_gc"
versions:
 - "0.21.1--h7ff8a90_2"
 - "0.21.1--h21ec9f0_4"
description: "shpc-registry automated BioContainers addition for genomeconstellation"
config: {"url": "https://biocontainers.pro/tools/genomeconstellation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomeconstellation", "latest": {"0.21.1--h21ec9f0_4": "sha256:55d1b3de31cf4fd683942e57fd2f5aa94656e7db81ea9dbd66318fda67612a0d"}, "tags": {"0.21.1--h7ff8a90_2": "sha256:9f3d37984a6cce543b5096bb9240e67ed68c467d0d3f5ae3a3377d4728c99578", "0.21.1--h21ec9f0_4": "sha256:55d1b3de31cf4fd683942e57fd2f5aa94656e7db81ea9dbd66318fda67612a0d"}, "docker": "quay.io/biocontainers/genomeconstellation", "aliases": {"jgi_gc": "/usr/local/bin/jgi_gc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomeconstellation.
shpc-registry automated BioContainers addition for genomeconstellation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomeconstellation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomeconstellation:0.21.1--h21ec9f0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomeconstellation/0.21.1--h21ec9f0_4
$ module help quay.io/biocontainers/genomeconstellation/0.21.1--h21ec9f0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomeconstellation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomeconstellation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomeconstellation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomeconstellation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomeconstellation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomeconstellation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jgi_gc

```bash
$ singularity exec <container> /usr/local/bin/jgi_gc
$ podman run --it --rm --entrypoint /usr/local/bin/jgi_gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jgi_gc   -v ${PWD} -w ${PWD} <container> -c " $@"
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