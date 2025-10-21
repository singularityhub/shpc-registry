---
layout: container
name:  "quay.io/biocontainers/tedna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tedna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tedna/container.yaml"
updated_at: "2025-10-21 03:40:40.883355"
latest: "1.2.2--hfc679d8_2"
container_url: "https://biocontainers.pro/tools/tedna"
aliases:
 - "tedna"
versions:
 - "1.2.2--hfc679d8_2"
description: "shpc-registry automated BioContainers addition for tedna"
config: {"url": "https://biocontainers.pro/tools/tedna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tedna", "latest": {"1.2.2--hfc679d8_2": "sha256:8acadbc22abb9937a9ba83bce0d4a0e5743b3f243e28a7d4eb7c3222ab3cce7d"}, "tags": {"1.2.2--hfc679d8_2": "sha256:8acadbc22abb9937a9ba83bce0d4a0e5743b3f243e28a7d4eb7c3222ab3cce7d"}, "docker": "quay.io/biocontainers/tedna", "aliases": {"tedna": "/usr/local/bin/tedna"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tedna.
shpc-registry automated BioContainers addition for tedna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tedna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tedna:1.2.2--hfc679d8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tedna/1.2.2--hfc679d8_2
$ module help quay.io/biocontainers/tedna/1.2.2--hfc679d8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tedna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tedna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tedna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tedna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tedna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tedna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tedna

```bash
$ singularity exec <container> /usr/local/bin/tedna
$ podman run --it --rm --entrypoint /usr/local/bin/tedna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tedna   -v ${PWD} -w ${PWD} <container> -c " $@"
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