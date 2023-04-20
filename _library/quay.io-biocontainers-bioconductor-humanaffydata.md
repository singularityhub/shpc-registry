---
layout: container
name:  "quay.io/biocontainers/bioconductor-humanaffydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humanaffydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humanaffydata/container.yaml"
updated_at: "2023-04-20 03:00:25.161524"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-humanaffydata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-humanaffydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humanaffydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humanaffydata", "latest": {"1.24.0--r42hdfd78af_0": "sha256:01a15e5467e4a359b0c93336c9f422bde8393bccf9d5bb9f0bc0be3497d20584"}, "tags": {"1.8.0--r351_0": "sha256:1ba79b3dc661daf357d765003cb7bbaf768c5d697f07758eb4a1926f940ce970", "1.24.0--r42hdfd78af_0": "sha256:01a15e5467e4a359b0c93336c9f422bde8393bccf9d5bb9f0bc0be3497d20584", "1.20.0--r41hdfd78af_1": "sha256:b8a727dee3d32268d7b55823634d0da7bbdc73bfda196aef551c38d08946694f", "1.18.0--r41hdfd78af_0": "sha256:731f5f4253491beb2e0cc37aebc41f44acb8c93f6c1359823c2e43a90c5d881f", "1.16.0--r40hdfd78af_1": "sha256:a6f100d44bfec10c16be47316e3d27d6c3a2e0f495d3eba7524e9b80b0fb8dd8", "1.14.0--r40_0": "sha256:407288f6f7ea1ff3f1cba11b90a89be376a16c4424f792a39c0fa2707aaf1bad"}, "docker": "quay.io/biocontainers/bioconductor-humanaffydata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humanaffydata.
shpc-registry automated BioContainers addition for bioconductor-humanaffydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humanaffydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humanaffydata:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humanaffydata/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-humanaffydata/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humanaffydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanaffydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanaffydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humanaffydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humanaffydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humanaffydata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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