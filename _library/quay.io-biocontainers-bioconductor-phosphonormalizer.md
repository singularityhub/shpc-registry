---
layout: container
name:  "quay.io/biocontainers/bioconductor-phosphonormalizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phosphonormalizer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phosphonormalizer/container.yaml"
updated_at: "2025-07-20 00:40:49.741392"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phosphonormalizer"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phosphonormalizer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phosphonormalizer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phosphonormalizer", "latest": {"1.30.0--r44hdfd78af_0": "sha256:da684034f7c73d49f02ddd7742e50b78a6957cf056db9b707c41f3ea747c1da4"}, "tags": {"1.8.0--r36_1": "sha256:0dca0b17320d758506d82a001d677456bce030025419fa8830f479a6a4a2a3b4", "1.22.0--r42hdfd78af_0": "sha256:8c00831afbd9bbad3be0d3d24443fddd39dcddb75e717423087bb00e3530ad2a", "1.18.0--r41hdfd78af_0": "sha256:dc1a8eb704c92a8a578ab0ca66bacc00c78ad2ab3aa5676494bc962f1f0cab46", "1.16.0--r41hdfd78af_0": "sha256:aa02c79a2fb64e4d9048f8bc5f8856b7637d2c3438cf89f612b7255df43ad565", "1.12.0--r40_0": "sha256:725a2fce614e30bfa39c24a29055613c3c843e27a404093ddff912befae93522", "1.10.0--r36_0": "sha256:70e1b749a0c09d9bdd2254a61dbc79a2f599929f987bbd92a41d77a2df88db3a", "1.24.0--r43hdfd78af_0": "sha256:117a5b5e5a76f15e40bd90d804a6b647f302408a12f82ebbd65388de701ab05b", "1.26.0--r43hdfd78af_0": "sha256:0afea823097734c6bbcbd255b6de348feabcffbee056fc2a30eae988056b9d0e", "1.30.0--r44hdfd78af_0": "sha256:da684034f7c73d49f02ddd7742e50b78a6957cf056db9b707c41f3ea747c1da4"}, "docker": "quay.io/biocontainers/bioconductor-phosphonormalizer", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phosphonormalizer.
shpc-registry automated BioContainers addition for bioconductor-phosphonormalizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phosphonormalizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phosphonormalizer:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phosphonormalizer/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phosphonormalizer/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phosphonormalizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phosphonormalizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phosphonormalizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phosphonormalizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phosphonormalizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phosphonormalizer-inspect-deffile:

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