---
layout: container
name:  "quay.io/biocontainers/bioconductor-rpx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rpx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rpx/container.yaml"
updated_at: "2023-08-01 03:15:50.012736"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rpx"

versions:
 - "2.1.12--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rpx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rpx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rpx", "latest": {"2.8.0--r43hdfd78af_0": "sha256:a684616dce30f077df7213e6f8864bc7f4cf6913d5d255410d9ff106604872a0"}, "tags": {"2.1.12--r41hdfd78af_0": "sha256:06ee8f1d216ca794b4dc97a114461e35c64f21d91ccd6a78e3cf11100d878f9c", "2.6.0--r42hdfd78af_0": "sha256:767b67b91b31f746f1413f68345293b1fd733f779cb45528dbf8b7d90fc3b961", "2.8.0--r43hdfd78af_0": "sha256:a684616dce30f077df7213e6f8864bc7f4cf6913d5d255410d9ff106604872a0"}, "docker": "quay.io/biocontainers/bioconductor-rpx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rpx.
shpc-registry automated BioContainers addition for bioconductor-rpx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rpx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rpx:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rpx/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rpx/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rpx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rpx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rpx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rpx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rpx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rpx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rpx

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