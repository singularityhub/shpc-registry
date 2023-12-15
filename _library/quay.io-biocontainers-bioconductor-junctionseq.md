---
layout: container
name:  "quay.io/biocontainers/bioconductor-junctionseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-junctionseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-junctionseq/container.yaml"
updated_at: "2023-12-15 02:34:20.635201"
latest: "1.17.0--r40h5f743cb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-junctionseq"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.17.0--r40h5f743cb_0"
 - "1.16.0--r36he1b5a44_0"
 - "1.14.0--r36he1b5a44_1"
 - "1.12.0--r351hf484d3e_0"
 - "1.10.0--r351hfc679d8_0"
description: "shpc-registry automated BioContainers addition for bioconductor-junctionseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-junctionseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-junctionseq", "latest": {"1.17.0--r40h5f743cb_0": "sha256:e5e9d0fdc1771a0846f7bf2cbe477a692115945d0c91011348bfe0136131eaf6"}, "tags": {"1.8.0--r3.4.1_0": "sha256:04106cbd134485b3c4e6d454b392f0b0a8a1942cb816e60acecadd634d5dffb3", "1.17.0--r40h5f743cb_0": "sha256:e5e9d0fdc1771a0846f7bf2cbe477a692115945d0c91011348bfe0136131eaf6", "1.16.0--r36he1b5a44_0": "sha256:4a584a330eac49f41394e1df127a8a2a38e78d248c0e26f2e3bec612f263837b", "1.14.0--r36he1b5a44_1": "sha256:e185436c0f25a0961e77db8a0ad052de3e97ae47d8971356e7760d8136655f3e", "1.12.0--r351hf484d3e_0": "sha256:f8d3f41c4e42a1721099d903efbf835378f3ad94c897d04ea6eae2434dd55ec3", "1.10.0--r351hfc679d8_0": "sha256:357e5d9d9623f51accbe0428b1052ede92f098ecd885a9757ddd7e8d5f52aa35"}, "docker": "quay.io/biocontainers/bioconductor-junctionseq", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-junctionseq.
shpc-registry automated BioContainers addition for bioconductor-junctionseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-junctionseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-junctionseq:1.17.0--r40h5f743cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-junctionseq/1.17.0--r40h5f743cb_0
$ module help quay.io/biocontainers/bioconductor-junctionseq/1.17.0--r40h5f743cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-junctionseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-junctionseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-junctionseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-junctionseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-junctionseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-junctionseq-inspect-deffile:

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