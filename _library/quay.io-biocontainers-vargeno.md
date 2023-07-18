---
layout: container
name:  "quay.io/biocontainers/vargeno"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vargeno/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vargeno/container.yaml"
updated_at: "2023-07-18 03:33:30.530179"
latest: "1.0.3--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/vargeno"
aliases:
 - "vargeno"
versions:
 - "1.0.3--h9f5acd7_3"
 - "1.0.3--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for vargeno"
config: {"url": "https://biocontainers.pro/tools/vargeno", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vargeno", "latest": {"1.0.3--h4ac6f70_5": "sha256:56a970ce73ddae4da260b0fda764a0e6b0816e4eb4990c95af3632504c6c7a4d"}, "tags": {"1.0.3--h9f5acd7_3": "sha256:4da3bde328e0c75ffe430ad7a8f90fcd15a0914b9a06f9649a5a99e25d07e9fc", "1.0.3--h4ac6f70_5": "sha256:56a970ce73ddae4da260b0fda764a0e6b0816e4eb4990c95af3632504c6c7a4d"}, "docker": "quay.io/biocontainers/vargeno", "aliases": {"vargeno": "/usr/local/bin/vargeno"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vargeno.
shpc-registry automated BioContainers addition for vargeno
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vargeno
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vargeno:1.0.3--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vargeno/1.0.3--h4ac6f70_5
$ module help quay.io/biocontainers/vargeno/1.0.3--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vargeno-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vargeno-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vargeno-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vargeno-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vargeno-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vargeno-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vargeno

```bash
$ singularity exec <container> /usr/local/bin/vargeno
$ podman run --it --rm --entrypoint /usr/local/bin/vargeno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vargeno   -v ${PWD} -w ${PWD} <container> -c " $@"
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