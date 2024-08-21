---
layout: container
name:  "quay.io/biocontainers/bioconductor-scdd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scdd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scdd/container.yaml"
updated_at: "2024-08-21 02:57:58.745732"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scdd"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scdd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scdd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scdd", "latest": {"1.26.0--r43hdfd78af_0": "sha256:701f39176268da033807b1a1283278fd1bec1f940adc2b2747fe8627070f52e9"}, "tags": {"1.8.0--r36_1": "sha256:78bd97a7287a816c7733ac4dfab5e6c39e85a82befbc0bbeff564e03e522be57", "1.18.0--r41hdfd78af_0": "sha256:13d01f7b08bde362ed60b3b7b11617b474bf7995c46eace1392734c75842c1f5", "1.16.0--r41hdfd78af_0": "sha256:9c11a71074cc9b961aa5e11411b5d29610dfb56f51068afd90e7850eea08eb16", "1.14.0--r40hdfd78af_1": "sha256:3e21a3d06a59c21919eebee28569ab12c7eac09b1b7b4bf1ddffd0fbb0554dad", "1.12.0--r40_0": "sha256:e6e1492ea8d732698cea4566ecb411b034b0f03deae5c04d25c33f71ef97c0dc", "1.10.0--r36_0": "sha256:0bc04387bd14518e6ede21096d8af7c32c8375947271aff23a8613f6376da740", "1.22.0--r42hdfd78af_0": "sha256:9800ab289f593513d2d5062dc765b7c4e6ba3af38870aeff1c14f9002cc8d108", "1.24.0--r43hdfd78af_0": "sha256:30d33e5337ba57d046b9df2ca3da974a2cf95249f9a4d02c16465f0e72c54302", "1.26.0--r43hdfd78af_0": "sha256:701f39176268da033807b1a1283278fd1bec1f940adc2b2747fe8627070f52e9"}, "docker": "quay.io/biocontainers/bioconductor-scdd", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scdd.
shpc-registry automated BioContainers addition for bioconductor-scdd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scdd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scdd:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scdd/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scdd/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scdd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scdd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scdd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scdd-inspect-deffile:

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