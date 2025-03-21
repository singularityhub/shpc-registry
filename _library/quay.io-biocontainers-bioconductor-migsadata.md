---
layout: container
name:  "quay.io/biocontainers/bioconductor-migsadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-migsadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-migsadata/container.yaml"
updated_at: "2025-03-21 03:21:11.488787"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-migsadata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.21.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.13.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-migsadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-migsadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-migsadata", "latest": {"1.24.0--r43hdfd78af_0": "sha256:fdd350a7243f3ebe77e0751cc396d066e04da87c4c55d4d1316e3e6678495e98"}, "tags": {"1.8.0--r36_1": "sha256:464afe7c8ae7ca8870948c0c55e2daf685c845eeecdd248c101b4c06a1cf9cd7", "1.21.0--r42hdfd78af_0": "sha256:c76b4303bce641e8feda7814ab463fa214e2399acf470ec3813852e85f794c41", "1.18.0--r41hdfd78af_1": "sha256:767dd9f4653ebae6d2a5182bf4f92b775266faffd0aa42ab58085684364b8de6", "1.16.0--r41hdfd78af_0": "sha256:335f02be142e0d96cefdcd3144f3472dda2b76f19285772f0b5d61262afdf05f", "1.14.0--r40hdfd78af_1": "sha256:8c81d1b5fda518981a95a90d114cf5955135efa55e757036d0a5ce8930f1c624", "1.13.0--r40_0": "sha256:1f86b2b72e5d64fec25aa7a5f4f931743ae16de90aafe931e58e3fb74f3ed556", "1.24.0--r43hdfd78af_0": "sha256:fdd350a7243f3ebe77e0751cc396d066e04da87c4c55d4d1316e3e6678495e98"}, "docker": "quay.io/biocontainers/bioconductor-migsadata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-migsadata.
shpc-registry automated BioContainers addition for bioconductor-migsadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-migsadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-migsadata:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-migsadata/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-migsadata/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-migsadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-migsadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-migsadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-migsadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-migsadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-migsadata-inspect-deffile:

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