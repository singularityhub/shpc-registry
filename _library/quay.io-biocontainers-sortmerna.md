---
layout: container
name:  "quay.io/biocontainers/sortmerna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sortmerna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sortmerna/container.yaml"
updated_at: "2022-11-27 12:59:57.659600"
latest: "4.3.6--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/sortmerna"
aliases:
 - "sortmerna"
versions:
 - "4.3.6--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for sortmerna"
config: {"url": "https://biocontainers.pro/tools/sortmerna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sortmerna", "latest": {"4.3.6--h9ee0642_0": "sha256:e35dc8312efb4255dafc0b06197838785a50c364d2baa64b9adcad65f8feb57c"}, "tags": {"4.3.6--h9ee0642_0": "sha256:e35dc8312efb4255dafc0b06197838785a50c364d2baa64b9adcad65f8feb57c"}, "docker": "quay.io/biocontainers/sortmerna", "aliases": {"sortmerna": "/usr/local/bin/sortmerna"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sortmerna.
shpc-registry automated BioContainers addition for sortmerna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sortmerna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sortmerna:4.3.6--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sortmerna/4.3.6--h9ee0642_0
$ module help quay.io/biocontainers/sortmerna/4.3.6--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sortmerna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sortmerna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sortmerna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sortmerna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sortmerna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sortmerna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sortmerna

```bash
$ singularity exec <container> /usr/local/bin/sortmerna
$ podman run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortmerna   -v ${PWD} -w ${PWD} <container> -c " $@"
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