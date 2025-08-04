---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133pluspmprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133pluspmprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133pluspmprobe/container.yaml"
updated_at: "2025-08-04 04:27:37.615726"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133pluspmprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspmprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133pluspmprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspmprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:62fe08227ad5fd5d6fa75fec1ccca4f633af2b0a01f88c42d566c6088838bb4d"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c469892e338e43ab7e634c194650a0347b49c9cffc560a1f50e1a7d9e8b87de2", "2.18.0--r42hdfd78af_10": "sha256:ea0d5fac635d580d63bcd97d8c56b06f72ec7ce9ff364ff5cc4d5fdfbc9c60dc", "2.18.0--r43hdfd78af_11": "sha256:796a1648fae865342928bd7808b85fc076ca8c9f809c4382ea2a4592cb0e7c5c", "2.18.0--r43hdfd78af_12": "sha256:82a3453624a68ce5e88dfa6fdf7f73c5d6a71d6e68f346da6c2f2c923b5b43ff", "2.18.0--r44hdfd78af_13": "sha256:62fe08227ad5fd5d6fa75fec1ccca4f633af2b0a01f88c42d566c6088838bb4d"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133pluspmprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133pluspmprobe.
shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspmprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133pluspmprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133pluspmprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133pluspmprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hthgu133pluspmprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133pluspmprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133pluspmprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133pluspmprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133pluspmprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133pluspmprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133pluspmprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hthgu133pluspmprobe

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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