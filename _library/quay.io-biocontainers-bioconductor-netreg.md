---
layout: container
name:  "quay.io/biocontainers/bioconductor-netreg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netreg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netreg/container.yaml"
updated_at: "2025-04-17 04:44:29.832827"
latest: "1.13.1--r40h399db7b_1"
container_url: "https://biocontainers.pro/tools/bioconductor-netreg"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_1"
 - "1.13.1--r40h399db7b_1"
 - "1.11.0--r40h5f743cb_0"
 - "1.10.0--r36he1b5a44_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netreg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netreg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netreg", "latest": {"1.13.1--r40h399db7b_1": "sha256:32d7b9d62c7c74c58802f18ac833d4bc8ba4adfe95b1c96298e6f85a807e9aaa"}, "tags": {"1.8.0--r36he1b5a44_1": "sha256:36920b999f654b396fbf898abef41eeefb962391099e19a2cde471994aa02bc9", "1.13.1--r40h399db7b_1": "sha256:32d7b9d62c7c74c58802f18ac833d4bc8ba4adfe95b1c96298e6f85a807e9aaa", "1.11.0--r40h5f743cb_0": "sha256:eac09d99ced2357a0fa3c1b8e3d0a275c225e004c5b5a59563281cbc9feb725f", "1.10.0--r36he1b5a44_0": "sha256:00fef331efeeb88ff68c3b11ee4da134c39e90e7cd58dc5bda63b65b6ee6024d"}, "docker": "quay.io/biocontainers/bioconductor-netreg", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netreg.
shpc-registry automated BioContainers addition for bioconductor-netreg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netreg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netreg:1.13.1--r40h399db7b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netreg/1.13.1--r40h399db7b_1
$ module help quay.io/biocontainers/bioconductor-netreg/1.13.1--r40h399db7b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netreg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netreg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netreg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netreg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netreg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netreg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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