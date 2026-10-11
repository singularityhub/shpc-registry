---
layout: container
name:  "quay.io/biocontainers/bqtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bqtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bqtools/container.yaml"
updated_at: "2026-10-11 09:13:05.991496"
latest: "0.5.14--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/bqtools"
aliases:
 - "bqtools"
versions:
 - "0.5.14--hfa8f182_0"
description: "singularity registry hpc automated addition for bqtools"
config: {"url": "https://biocontainers.pro/tools/bqtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bqtools", "latest": {"0.5.14--hfa8f182_0": "sha256:dfe6477770207192909bebabe3c8549ac5920a7ea19dd462921471a2005ebeb8"}, "tags": {"0.5.14--hfa8f182_0": "sha256:dfe6477770207192909bebabe3c8549ac5920a7ea19dd462921471a2005ebeb8"}, "docker": "quay.io/biocontainers/bqtools", "aliases": {"bqtools": "/usr/local/bin/bqtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bqtools.
singularity registry hpc automated addition for bqtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bqtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bqtools:0.5.14--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bqtools/0.5.14--hfa8f182_0
$ module help quay.io/biocontainers/bqtools/0.5.14--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bqtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bqtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bqtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bqtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bqtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bqtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bqtools

```bash
$ singularity exec <container> /usr/local/bin/bqtools
$ podman run --it --rm --entrypoint /usr/local/bin/bqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bqtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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