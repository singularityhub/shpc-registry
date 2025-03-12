---
layout: container
name:  "quay.io/biocontainers/bioconductor-methreg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methreg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methreg/container.yaml"
updated_at: "2025-03-12 03:05:57.147783"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methreg"
aliases:
 - "pandoc"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methreg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methreg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methreg", "latest": {"1.12.0--r43hdfd78af_0": "sha256:fe1b8fecc67cfb2870cc1aeea530cea7426f07b5ee25d6f38055cbe3b3d2b609"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:2d164064507fcda9b82f45ed2dfee45c187afbebdffa5bda93100c9385596426", "1.8.0--r42hdfd78af_0": "sha256:4278f9d59263b52c27214f1a3212cc3e5efcf1ff685aa98b894337c7ae9a722e", "1.10.0--r43hdfd78af_0": "sha256:36777f5527654c0a37555a77e0843987263a79a73ea5c9bb49b88723fbeeea21", "1.12.0--r43hdfd78af_0": "sha256:fe1b8fecc67cfb2870cc1aeea530cea7426f07b5ee25d6f38055cbe3b3d2b609"}, "docker": "quay.io/biocontainers/bioconductor-methreg", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methreg.
shpc-registry automated BioContainers addition for bioconductor-methreg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methreg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methreg:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methreg/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methreg/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methreg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methreg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methreg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methreg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methreg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methreg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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