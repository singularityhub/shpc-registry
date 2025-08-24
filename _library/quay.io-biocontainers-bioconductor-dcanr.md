---
layout: container
name:  "quay.io/biocontainers/bioconductor-dcanr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dcanr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dcanr/container.yaml"
updated_at: "2025-08-24 03:42:19.193713"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dcanr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dcanr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dcanr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dcanr", "latest": {"1.22.0--r44hdfd78af_0": "sha256:4b6be7cf9c63c5cfd1f5b1bec6da088755fa6d1f7550af0e71932a9f42f0100b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:3f5bba028b64dc33be0cc4543a3ebf4d2fd2410fb68d488156c606a9d033cfa6", "1.14.0--r42hdfd78af_0": "sha256:9e7603a1baa961a987715cc9eafada99e07447bfa73b58e5daba77d836cc3cff", "1.10.0--r41hdfd78af_0": "sha256:f45a8aa158c5868b8ef991d5476498b384f83dce1ff550d5ef563a3b5995f49f", "1.16.0--r43hdfd78af_0": "sha256:85098a02d91e8ec93b05e600449812588d0a354da8ef947ed93556a9777c84c5", "1.18.0--r43hdfd78af_0": "sha256:0be13e2fd8a9cab0f13625465cc0471c0fbf0fe9f92a01e7deb41cf15835c85f", "1.22.0--r44hdfd78af_0": "sha256:4b6be7cf9c63c5cfd1f5b1bec6da088755fa6d1f7550af0e71932a9f42f0100b"}, "docker": "quay.io/biocontainers/bioconductor-dcanr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dcanr.
shpc-registry automated BioContainers addition for bioconductor-dcanr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dcanr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dcanr:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dcanr/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dcanr/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dcanr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dcanr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dcanr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dcanr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dcanr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dcanr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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