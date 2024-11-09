---
layout: container
name:  "quay.io/biocontainers/impute2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/impute2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/impute2/container.yaml"
updated_at: "2024-11-09 03:07:00.671468"
latest: "2.3.2--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/impute2"
aliases:
 - "impute2"
versions:
 - "2.3.2--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for impute2"
config: {"url": "https://biocontainers.pro/tools/impute2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for impute2", "latest": {"2.3.2--h9ee0642_2": "sha256:6739e16213e72627401fa8763d5dd62db14143471d0a6bb98761c0efb38915e6"}, "tags": {"2.3.2--h9ee0642_2": "sha256:6739e16213e72627401fa8763d5dd62db14143471d0a6bb98761c0efb38915e6"}, "docker": "quay.io/biocontainers/impute2", "aliases": {"impute2": "/usr/local/bin/impute2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/impute2.
shpc-registry automated BioContainers addition for impute2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/impute2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/impute2:2.3.2--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/impute2/2.3.2--h9ee0642_2
$ module help quay.io/biocontainers/impute2/2.3.2--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### impute2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### impute2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### impute2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### impute2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### impute2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### impute2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### impute2

```bash
$ singularity exec <container> /usr/local/bin/impute2
$ podman run --it --rm --entrypoint /usr/local/bin/impute2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impute2   -v ${PWD} -w ${PWD} <container> -c " $@"
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