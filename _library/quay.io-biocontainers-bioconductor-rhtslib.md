---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhtslib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhtslib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhtslib/container.yaml"
updated_at: "2024-09-06 02:50:36.660923"
latest: "2.4.0--r43ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-rhtslib"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "2.0.0--r42hc0cfd56_0"
 - "1.26.0--r41hc0cfd56_2"
 - "1.24.0--r41hd029910_0"
 - "1.22.0--r40hd029910_1"
 - "1.20.0--r40h037d062_0"
 - "2.0.0--r42ha9d7317_1"
 - "2.2.0--r43ha9d7317_0"
 - "2.4.0--r43ha9d7317_1"
 - "2.4.0--r43ha9d7317_2"
description: "shpc-registry automated BioContainers addition for bioconductor-rhtslib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhtslib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhtslib", "latest": {"2.4.0--r43ha9d7317_2": "sha256:3f84f632b151e34391f93d07d7e3f88f0e37379fe625894d61685762180f7648"}, "tags": {"1.8.0--r3.4.1_0": "sha256:d6d7e3c6ab8cad002c625c878caac47e6b621925a238734f1da866aee5fd0201", "2.0.0--r42hc0cfd56_0": "sha256:1795b8c5750882461791d8bc6ed298b0cb46b3aec34f7a0a5d13addcc8f2fa21", "1.26.0--r41hc0cfd56_2": "sha256:372592e3f1ea45c31acb4f6f1e562937d9b87d86e6e130f404e2cf54d3155c26", "1.24.0--r41hd029910_0": "sha256:29f274cd65b9f2c893d4386f8f7a4e75c107082ffc69c5a5e668c29bcad50ea6", "1.22.0--r40hd029910_1": "sha256:33ab82f70b77d16da8703f87e2763e48f2f7e66303844a7e3f11cf4e23af6d4c", "1.20.0--r40h037d062_0": "sha256:738058070ac7d24f8a02177642fedf355a96a685f5818eea109c97815ce41dad", "2.0.0--r42ha9d7317_1": "sha256:931fd943478dccf81813f7f8757383e86d0d07a0a4ab13db59f64b878bae1d77", "2.2.0--r43ha9d7317_0": "sha256:c6c1a4d48f3be83baf9c2f3bf97c0308617c8b563687a042a5e47958d4b2d2b7", "2.4.0--r43ha9d7317_1": "sha256:d381d2efb0c4bc19dd5a83d539d9d93a7d5417ac1a4ae85fa83b7d866ca73a61", "2.4.0--r43ha9d7317_2": "sha256:3f84f632b151e34391f93d07d7e3f88f0e37379fe625894d61685762180f7648"}, "docker": "quay.io/biocontainers/bioconductor-rhtslib", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhtslib.
shpc-registry automated BioContainers addition for bioconductor-rhtslib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhtslib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhtslib:2.4.0--r43ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhtslib/2.4.0--r43ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-rhtslib/2.4.0--r43ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhtslib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhtslib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhtslib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhtslib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhtslib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhtslib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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