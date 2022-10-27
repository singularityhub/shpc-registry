---
layout: container
name:  "quay.io/biocontainers/genblastg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genblastg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genblastg/container.yaml"
updated_at: "2022-10-27 00:31:22.472121"
latest: "1.39--1"
container_url: "https://biocontainers.pro/tools/genblastg"
aliases:
 - "genblastG"
versions:
 - "1.39--1"
description: "shpc-registry automated BioContainers addition for genblastg"
config: {"url": "https://biocontainers.pro/tools/genblastg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genblastg", "latest": {"1.39--1": "sha256:2f1f5f2632e46840f6e2a05470493e13b52c7a86e3a4b2b218793022162f4d38"}, "tags": {"1.39--1": "sha256:2f1f5f2632e46840f6e2a05470493e13b52c7a86e3a4b2b218793022162f4d38"}, "docker": "quay.io/biocontainers/genblastg", "aliases": {"genblastG": "/usr/local/bin/genblastG"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genblastg.
shpc-registry automated BioContainers addition for genblastg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genblastg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genblastg:1.39--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genblastg/1.39--1
$ module help quay.io/biocontainers/genblastg/1.39--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genblastg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genblastg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genblastg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genblastg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genblastg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genblastg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genblastG

```bash
$ singularity exec <container> /usr/local/bin/genblastG
$ podman run --it --rm --entrypoint /usr/local/bin/genblastG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genblastG   -v ${PWD} -w ${PWD} <container> -c " $@"
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