---
layout: container
name:  "quay.io/biocontainers/r-phylomeasures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-phylomeasures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-phylomeasures/container.yaml"
updated_at: "2025-09-10 03:20:24.529898"
latest: "2.1--r44h40dc89f_10"
container_url: "https://biocontainers.pro/tools/r-phylomeasures"

versions:
 - "2.1--r41hecf12ef_6"
 - "2.1--r42hecf12ef_7"
 - "2.1--r42h21a89ab_8"
 - "2.1--r43h21a89ab_9"
 - "2.1--r44h40dc89f_10"
description: "shpc-registry automated BioContainers addition for r-phylomeasures"
config: {"url": "https://biocontainers.pro/tools/r-phylomeasures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-phylomeasures", "latest": {"2.1--r44h40dc89f_10": "sha256:22c55c4363687f0dddbc364f31d7cb21446c13d79fd19119e49fe50657c128b3"}, "tags": {"2.1--r41hecf12ef_6": "sha256:7d029f2fe087adb567e769721cda436ee9dd1e46d5656975f3e69aaa7abc940b", "2.1--r42hecf12ef_7": "sha256:91568c9c1071573a2621ac9daa64af2af86804fca73b29ad733ea9a443570c07", "2.1--r42h21a89ab_8": "sha256:d42e475f9d4e2f63b92dce5fc1c82571f1d0943d4b48406f52e4f9e27aea06c3", "2.1--r43h21a89ab_9": "sha256:48693fb17b2171bc3973e564ac2d2a1073d6e3eedc923b3e888bf82ca1a73a09", "2.1--r44h40dc89f_10": "sha256:22c55c4363687f0dddbc364f31d7cb21446c13d79fd19119e49fe50657c128b3"}, "docker": "quay.io/biocontainers/r-phylomeasures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-phylomeasures.
shpc-registry automated BioContainers addition for r-phylomeasures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-phylomeasures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-phylomeasures:2.1--r44h40dc89f_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-phylomeasures/2.1--r44h40dc89f_10
$ module help quay.io/biocontainers/r-phylomeasures/2.1--r44h40dc89f_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-phylomeasures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-phylomeasures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-phylomeasures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-phylomeasures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-phylomeasures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-phylomeasures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-phylomeasures

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