---
layout: container
name:  "quay.io/biocontainers/bioconductor-oncomix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oncomix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oncomix/container.yaml"
updated_at: "2022-11-21 00:07:32.436810"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oncomix"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oncomix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oncomix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oncomix", "latest": {"1.20.0--r42hdfd78af_0": "sha256:826134bf2f77dde72444d2572290a2669724cd92b9715f19e558ea4c66a856f6"}, "tags": {"1.8.0--r36_0": "sha256:4a2409ada37d0d7d092d7004d1b5cec1a107cec25df20941b16afad58ddab7c8", "1.20.0--r42hdfd78af_0": "sha256:826134bf2f77dde72444d2572290a2669724cd92b9715f19e558ea4c66a856f6", "1.16.0--r41hdfd78af_0": "sha256:6a31f07a9d5f327d6d5004e1cf22770bf65d3d7bbd5109ef506817e4a4bcaff4", "1.14.0--r41hdfd78af_0": "sha256:35b99766d04432d3aad72c957728b6b0d3eff45bcccf6d8cacd310571589e0ce", "1.12.0--r40hdfd78af_1": "sha256:63b4d817894894a94fbc02aa2537b087cb029e2c610080984a81fd3017de1f86", "1.10.0--r40_0": "sha256:04bf08cf5dfa0b9dbec82b84fc0ac90e97c4643e12479e09b3c9c3b3d03c1edd"}, "docker": "quay.io/biocontainers/bioconductor-oncomix", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oncomix.
shpc-registry automated BioContainers addition for bioconductor-oncomix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oncomix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oncomix:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oncomix/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-oncomix/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oncomix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oncomix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oncomix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oncomix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oncomix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oncomix-inspect-deffile:

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