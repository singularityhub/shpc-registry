---
layout: container
name:  "quay.io/biocontainers/bioconductor-prize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prize/container.yaml"
updated_at: "2023-01-18 03:14:51.916378"
latest: "1.17.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prize"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.17.0--r40_0"
 - "1.16.0--r36_0"
 - "1.14.0--r36_1"
 - "1.12.1--r351_0"
 - "1.10.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prize", "latest": {"1.17.0--r40_0": "sha256:32f357c04d9fe964624c36b7497f0a259e0816d9eb5aae7f39957b6c704c1204"}, "tags": {"1.8.0--r3.4.1_0": "sha256:8e83bfe5341d06c3fd4702536a3527b4544729f2efc2e0d2cf96c291803f92a9", "1.17.0--r40_0": "sha256:32f357c04d9fe964624c36b7497f0a259e0816d9eb5aae7f39957b6c704c1204", "1.16.0--r36_0": "sha256:12871e18e68932beff2dca1d38a2cef5990d9a893e3580c96e1cd5fc5b19f5c9", "1.14.0--r36_1": "sha256:6b195a8687e7948d9bc9129bba3b61c9ed59315b77215f6662abc8b791317330", "1.12.1--r351_0": "sha256:e1f3df7e0c4227b7fcbee7bfe65d104ba4c9bc20c3917e14c5b1993a9eef542a", "1.10.0--r351_0": "sha256:cd160816d52572c6eb9bf6a2ae344e91df2f476653076072b38aa3d0628e350e"}, "docker": "quay.io/biocontainers/bioconductor-prize", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prize.
shpc-registry automated BioContainers addition for bioconductor-prize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prize:1.17.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prize/1.17.0--r40_0
$ module help quay.io/biocontainers/bioconductor-prize/1.17.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prize-inspect-deffile:

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