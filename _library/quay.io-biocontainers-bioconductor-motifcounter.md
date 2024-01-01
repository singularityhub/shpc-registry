---
layout: container
name:  "quay.io/biocontainers/bioconductor-motifcounter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-motifcounter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-motifcounter/container.yaml"
updated_at: "2024-01-01 03:07:43.061609"
latest: "1.26.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-motifcounter"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_1"
 - "1.22.0--r42hc0cfd56_0"
 - "1.18.0--r41hc0cfd56_2"
 - "1.16.0--r41hd029910_0"
 - "1.14.0--r40hd029910_1"
 - "1.12.0--r40h037d062_0"
 - "1.22.0--r42ha9d7317_1"
 - "1.24.0--r43ha9d7317_0"
 - "1.26.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-motifcounter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-motifcounter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-motifcounter", "latest": {"1.26.0--r43ha9d7317_0": "sha256:d1f8182d950fd87c05ad6bca0b904e9acbc1472cd6351e58cd89beb02e99d802"}, "tags": {"1.8.0--r36h516909a_1": "sha256:2b5e25ef1d4bc7e99a9b168a67560f435827fc2246fdc4437a43fb49b84ea4cf", "1.22.0--r42hc0cfd56_0": "sha256:019216de19c03254c9e0bf987ac768753c21f2fa11f2d9c34f17cc5614d81afc", "1.18.0--r41hc0cfd56_2": "sha256:ea87fd8d4e1d1fa3f417c52a8d49f2de1ed8f81bf3e4bc31b40a851acfa602bf", "1.16.0--r41hd029910_0": "sha256:eda5498a5c8b508a24d54f6d97384b054089544ba238ae1baa3b555ecb3c9085", "1.14.0--r40hd029910_1": "sha256:42553b0209f2f6a76a56add49ad53804b8a4e935302274fe9c773dafb0e556d9", "1.12.0--r40h037d062_0": "sha256:032578b84c09cc310ed81b39d1471910b6ab7fb734b9cbc2cb500a4ae3406192", "1.22.0--r42ha9d7317_1": "sha256:a856bdae19292f03405b814b02f313712a258f7c0239076e63bce1a788b4a305", "1.24.0--r43ha9d7317_0": "sha256:8ce8a74a353a349714ec8a6b7ce56705f9b3e61a4d69ce07947fa83daec5514e", "1.26.0--r43ha9d7317_0": "sha256:d1f8182d950fd87c05ad6bca0b904e9acbc1472cd6351e58cd89beb02e99d802"}, "docker": "quay.io/biocontainers/bioconductor-motifcounter", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-motifcounter.
shpc-registry automated BioContainers addition for bioconductor-motifcounter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-motifcounter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-motifcounter:1.26.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-motifcounter/1.26.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-motifcounter/1.26.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-motifcounter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifcounter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifcounter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-motifcounter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-motifcounter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-motifcounter-inspect-deffile:

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