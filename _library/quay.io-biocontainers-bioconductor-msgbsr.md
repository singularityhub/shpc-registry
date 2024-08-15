---
layout: container
name:  "quay.io/biocontainers/bioconductor-msgbsr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msgbsr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msgbsr/container.yaml"
updated_at: "2024-08-15 03:41:55.238898"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msgbsr"
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
description: "shpc-registry automated BioContainers addition for bioconductor-msgbsr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msgbsr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msgbsr", "latest": {"1.26.0--r43hdfd78af_0": "sha256:e3e68a82ff6653bca8c449f40b9ddf59301c2ac7b54daa82c4b5738b7cd70271"}, "tags": {"1.8.0--r36_1": "sha256:8d79d72f040e7cc9228d8fff98b2fdc62cc4c9e98e014526d64176695089db4c", "1.22.0--r42hdfd78af_0": "sha256:e4b156e530911c72dc782e2d50bad0cf99bbdcdbdbf1744e9940248475ac5a8a", "1.18.0--r41hdfd78af_0": "sha256:c49653df11c7a04694465acb3a32530cf5c5bdae3386c77e54624242c70ce814", "1.16.0--r41hdfd78af_0": "sha256:3482905bb59f96c9af05f7fc635cada68743c37af424d229c9a7b8fdca7cf6b3", "1.12.0--r40_0": "sha256:669345d7ce3d9a995f5dcd07de5b8a9777db6578332e2355ca9803b569b10d7e", "1.10.0--r36_0": "sha256:d03a0f16a6a3a850b7dc41c2ab2d3c0ce9d6c26942800211ca5efa89e8b2b4bc", "1.24.0--r43hdfd78af_0": "sha256:c425cdbff409e374d90420a6843b80401817b0dde445818ed354d0934e9b94ce", "1.26.0--r43hdfd78af_0": "sha256:e3e68a82ff6653bca8c449f40b9ddf59301c2ac7b54daa82c4b5738b7cd70271"}, "docker": "quay.io/biocontainers/bioconductor-msgbsr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msgbsr.
shpc-registry automated BioContainers addition for bioconductor-msgbsr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msgbsr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msgbsr:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msgbsr/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msgbsr/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msgbsr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msgbsr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msgbsr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msgbsr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msgbsr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msgbsr-inspect-deffile:

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