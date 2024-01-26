---
layout: container
name:  "quay.io/biocontainers/bioconductor-twoddpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-twoddpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-twoddpcr/container.yaml"
updated_at: "2024-01-26 02:54:11.155888"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-twoddpcr"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-twoddpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-twoddpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-twoddpcr", "latest": {"1.26.0--r43hdfd78af_0": "sha256:9c298927e07132a2fc877d5a97a9b6e06f43d57f087b176b3050e494a9795795"}, "tags": {"1.8.0--r36_1": "sha256:da1c32951ff006e12061a77381df7e92eefbe20a0f045aeb12d2eecbab0114e8", "1.22.0--r42hdfd78af_0": "sha256:22272cb4003b4701e9db41b3a8222c0bf5d1505a37f5aac40f75659aa28a2608", "1.18.0--r41hdfd78af_0": "sha256:c046a8d0c2899648a3062226f27fbb18cbb17416e313d86c6a073b2ded462807", "1.16.0--r41hdfd78af_0": "sha256:a25b663f2666c5a669b63df5f687cda7ead54bc97432f10020343951e21ec7f3", "1.14.0--r40hdfd78af_1": "sha256:fe8fd916c13012cfb8ab86778012d7d9c643c982076b92e4e26e1d06d3741eb1", "1.12.0--r40_0": "sha256:48905a7bbd1647323f6f5db827c31cffe9c51c0bcbb7c4aba16a1f7f2fe73afe", "1.24.0--r43hdfd78af_0": "sha256:3d4c0ad0b78af70de606ec073c16211f7110282802fd8b781d437cfcda766a4b", "1.26.0--r43hdfd78af_0": "sha256:9c298927e07132a2fc877d5a97a9b6e06f43d57f087b176b3050e494a9795795"}, "docker": "quay.io/biocontainers/bioconductor-twoddpcr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-twoddpcr.
shpc-registry automated BioContainers addition for bioconductor-twoddpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-twoddpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-twoddpcr:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-twoddpcr/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-twoddpcr/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-twoddpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-twoddpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-twoddpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-twoddpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-twoddpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-twoddpcr-inspect-deffile:

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