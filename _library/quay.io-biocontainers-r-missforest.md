---
layout: container
name:  "quay.io/biocontainers/r-missforest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-missforest/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-missforest/container.yaml"
updated_at: "2022-10-27 00:47:38.944685"
latest: "1.4--r3.3.1_0"
container_url: "https://biocontainers.pro/tools/r-missforest"

versions:
 - "1.4--r3.3.1_0"
description: "shpc-registry automated BioContainers addition for r-missforest"
config: {"url": "https://biocontainers.pro/tools/r-missforest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-missforest", "latest": {"1.4--r3.3.1_0": "sha256:0a078f410ed41b80fdf60b435f35d6e10da25e2f0aac6cc55c82f33fba4e6e07"}, "tags": {"1.4--r3.3.1_0": "sha256:0a078f410ed41b80fdf60b435f35d6e10da25e2f0aac6cc55c82f33fba4e6e07"}, "docker": "quay.io/biocontainers/r-missforest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-missforest.
shpc-registry automated BioContainers addition for r-missforest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-missforest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-missforest:1.4--r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-missforest/1.4--r3.3.1_0
$ module help quay.io/biocontainers/r-missforest/1.4--r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-missforest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-missforest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-missforest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-missforest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-missforest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-missforest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-missforest

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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