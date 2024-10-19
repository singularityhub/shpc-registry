---
layout: container
name:  "quay.io/biocontainers/bioconductor-ramigo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ramigo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ramigo/container.yaml"
updated_at: "2024-10-19 03:12:36.490004"
latest: "1.28.0--r341_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ramigo"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.28.0--r341_0"
 - "1.28.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ramigo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ramigo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ramigo", "latest": {"1.28.0--r341_0": "sha256:1e1a18506ebc4db4bc65fecd30c2a9d77f4eafd35de647052609ae11b8df3d0b"}, "tags": {"1.28.0--r341_0": "sha256:1e1a18506ebc4db4bc65fecd30c2a9d77f4eafd35de647052609ae11b8df3d0b", "1.28.0--r351_0": "sha256:b84c6d33184dcdb33ec6b1d7c17ad910b52f876f76bc86002f62d22f36b9b423"}, "docker": "quay.io/biocontainers/bioconductor-ramigo", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ramigo.
shpc-registry automated BioContainers addition for bioconductor-ramigo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ramigo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ramigo:1.28.0--r341_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ramigo/1.28.0--r341_0
$ module help quay.io/biocontainers/bioconductor-ramigo/1.28.0--r341_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ramigo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ramigo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ramigo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ramigo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ramigo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ramigo-inspect-deffile:

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