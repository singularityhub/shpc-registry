---
layout: container
name:  "quay.io/biocontainers/bioconductor-dchiprep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dchiprep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dchiprep/container.yaml"
updated_at: "2024-02-26 03:56:14.285597"
latest: "1.18.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dchiprep"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.14.0--r36_1"
 - "1.12.0--r351_0"
 - "1.10.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dchiprep"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dchiprep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dchiprep", "latest": {"1.18.0--r40_0": "sha256:fb638c8280c1123d0d232cc6a8a40998a74553789bbde3fdf8ecfaf0c9f30194"}, "tags": {"1.8.0--r3.4.1_0": "sha256:e6e21322dceca279d29dbd292fcaefbca1257821ef4e46c972a2c8e21ca83c0b", "1.18.0--r40_0": "sha256:fb638c8280c1123d0d232cc6a8a40998a74553789bbde3fdf8ecfaf0c9f30194", "1.16.0--r36_0": "sha256:a5a0a8394ccb40b3b3ce1edc6e8f561de4646a55ba06d00c7ca9b28809deb65b", "1.14.0--r36_1": "sha256:d2a7c25df437e3b644ea6a116627e7c82994877b8e75246b958951e6b9477559", "1.12.0--r351_0": "sha256:114c37fd7718ba499c427d6115e2b5ca86962ab7dbf5a9706f219388fcc2fb8e", "1.10.0--r351_0": "sha256:002700cb731b7b8e5432b2c4faa071f0a5dd04b566df2cd6f66c9627b9cd2ab6"}, "docker": "quay.io/biocontainers/bioconductor-dchiprep", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dchiprep.
shpc-registry automated BioContainers addition for bioconductor-dchiprep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dchiprep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dchiprep:1.18.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dchiprep/1.18.0--r40_0
$ module help quay.io/biocontainers/bioconductor-dchiprep/1.18.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dchiprep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dchiprep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dchiprep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dchiprep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dchiprep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dchiprep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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