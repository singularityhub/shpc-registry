---
layout: container
name:  "quay.io/biocontainers/bioconductor-pannbuilder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pannbuilder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pannbuilder/container.yaml"
updated_at: "2025-09-18 03:43:57.277006"
latest: "1.43.0--r341_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pannbuilder"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.43.0--r341_0"
 - "1.43.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pannbuilder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pannbuilder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pannbuilder", "latest": {"1.43.0--r341_0": "sha256:5fdf90ee377d909d0766b2425947b29b654be57a3d3c72b4a83790534fc0b912"}, "tags": {"1.43.0--r341_0": "sha256:5fdf90ee377d909d0766b2425947b29b654be57a3d3c72b4a83790534fc0b912", "1.43.0--r351_0": "sha256:7d71bf0af37586d25551e5bf1d376779e90676b19a320b4ed06e5347f9ea2041"}, "docker": "quay.io/biocontainers/bioconductor-pannbuilder", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pannbuilder.
shpc-registry automated BioContainers addition for bioconductor-pannbuilder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pannbuilder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pannbuilder:1.43.0--r341_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pannbuilder/1.43.0--r341_0
$ module help quay.io/biocontainers/bioconductor-pannbuilder/1.43.0--r341_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pannbuilder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pannbuilder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pannbuilder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pannbuilder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pannbuilder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pannbuilder-inspect-deffile:

```bash
$ singularity inspect -d <container>
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