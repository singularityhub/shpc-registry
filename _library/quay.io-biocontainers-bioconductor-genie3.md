---
layout: container
name:  "quay.io/biocontainers/bioconductor-genie3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genie3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genie3/container.yaml"
updated_at: "2024-09-06 02:46:09.018494"
latest: "1.24.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-genie3"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_0"
 - "1.20.0--r42hc0cfd56_0"
 - "1.16.0--r41hc0cfd56_2"
 - "1.14.0--r41hd029910_0"
 - "1.12.0--r40hd029910_1"
 - "1.10.0--r40h037d062_0"
 - "1.20.0--r42hc0cfd56_1"
 - "1.20.0--r42ha9d7317_2"
 - "1.22.0--r43ha9d7317_0"
 - "1.24.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-genie3"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genie3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genie3", "latest": {"1.24.0--r43ha9d7317_1": "sha256:353d407ab7a23d08b0e4c7774a2b02e903624feab437a8f72789d0b5c8f9b804"}, "tags": {"1.8.0--r36h516909a_0": "sha256:c3b75ec10a7f4906a51d415a1bccfa3ffb3fa46c70d51c766a5df7881cb3c1c9", "1.20.0--r42hc0cfd56_0": "sha256:18dd62747736cebd8d2c08da3e8f34afbd5fd42be47e949955513739c9c34e90", "1.16.0--r41hc0cfd56_2": "sha256:6f2cb996ffa0df0631822d00517d27fe139d17f2a79fe53c9d18c79d7286c2ff", "1.14.0--r41hd029910_0": "sha256:7b7d2ff41a4aa0a74648475604541f236f03bc2b310ed60fdb627e8043581e5f", "1.12.0--r40hd029910_1": "sha256:5b70b078a4f7d2abf17897b3dd56cd61b5bc7f3c9842d093fd7d8d2f248f753b", "1.10.0--r40h037d062_0": "sha256:726f864a10998dd519dd6978004ce08aa3c1b3f9ecfe53abc2cb36a109472171", "1.20.0--r42hc0cfd56_1": "sha256:d200866c76c6b43a825517a3a8c1632f20f6efed9b054dd1d0e9847901d6708e", "1.20.0--r42ha9d7317_2": "sha256:841636d5cbe2b85ff39057ce5c447a52d78b42ac1719dbec6fbf6126dfd9c6b7", "1.22.0--r43ha9d7317_0": "sha256:538f099ccc558379f9f527f417fb56760e767174ce3afa900ec93a6a19ce7ff9", "1.24.0--r43ha9d7317_1": "sha256:353d407ab7a23d08b0e4c7774a2b02e903624feab437a8f72789d0b5c8f9b804"}, "docker": "quay.io/biocontainers/bioconductor-genie3", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genie3.
shpc-registry automated BioContainers addition for bioconductor-genie3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genie3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genie3:1.24.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genie3/1.24.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-genie3/1.24.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genie3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genie3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genie3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genie3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genie3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genie3-inspect-deffile:

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