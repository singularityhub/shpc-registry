---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene/container.yaml"
updated_at: "2025-08-03 04:36:34.244780"
latest: "3.2.2--r44hdfd78af_17"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.2--r40_9"
 - "3.2.2--r41hdfd78af_13"
 - "3.2.2--r42hdfd78af_14"
 - "3.2.2--r43hdfd78af_15"
 - "3.2.2--r43hdfd78af_16"
 - "3.2.2--r44hdfd78af_17"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm9.knowngene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm9.knowngene", "latest": {"3.2.2--r44hdfd78af_17": "sha256:a0ef20649e217fd4f887de68d1ae7c69f476f78bb583bfe43ac6581d53cd7cb0"}, "tags": {"3.2.2--r40_9": "sha256:8415202b978f006380bee7bdd2c09ddb0bc4d6280f3cdc24c5f8042ac4a4c773", "3.2.2--r41hdfd78af_13": "sha256:94429dd582908ea45ce225e104a2b94afb648d06964f0eaae7de9e2b9d9bbd2a", "3.2.2--r42hdfd78af_14": "sha256:c990d0531c35d9704b7fae1129d3a7a5b1b295348a5ca14b0ce83607fcb8c2f3", "3.2.2--r43hdfd78af_15": "sha256:f5d97f61d16022ba4a691979e6cfe555e9c125e3aa94542632662a833cf527bb", "3.2.2--r43hdfd78af_16": "sha256:7a754787b60f302990ec373f5b8b7aba00dcacaafa78959eeead585a749b4a01", "3.2.2--r44hdfd78af_17": "sha256:a0ef20649e217fd4f887de68d1ae7c69f476f78bb583bfe43ac6581d53cd7cb0"}, "docker": "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene.
shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm9.knowngene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene:3.2.2--r44hdfd78af_17
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene/3.2.2--r44hdfd78af_17
$ module help quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm9.knowngene/3.2.2--r44hdfd78af_17
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm9.knowngene-inspect-deffile:

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