---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene/container.yaml"
updated_at: "2025-12-29 05:06:45.172288"
latest: "3.2.2--r44hdfd78af_17"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce6.ensgene"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.2--r40_9"
 - "3.2.2--r42hdfd78af_14"
 - "3.2.2--r43hdfd78af_15"
 - "3.2.2--r43hdfd78af_16"
 - "3.2.2--r44hdfd78af_17"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce6.ensgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce6.ensgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce6.ensgene", "latest": {"3.2.2--r44hdfd78af_17": "sha256:e3b2209c29a3af9fc4905b8dd2d63b12aecc8012f1e30af797aa74b1ffa33be7"}, "tags": {"3.2.2--r40_9": "sha256:f399d3f669c3e153c49b6e2da6d553d28d9b199b2050c417220ca393b9acfa30", "3.2.2--r42hdfd78af_14": "sha256:f125cc78d2001a05aa6d4ab4ead7ae4141979b73d4afc73bde7036363804111b", "3.2.2--r43hdfd78af_15": "sha256:64e792aea524a87f4a17bf5c54631d6c426e7bb461e57264254e98b372dc6f32", "3.2.2--r43hdfd78af_16": "sha256:869b04cb9048d6c2c8148b4a979e76fc8341178a0dbb050acf6692317976de25", "3.2.2--r44hdfd78af_17": "sha256:e3b2209c29a3af9fc4905b8dd2d63b12aecc8012f1e30af797aa74b1ffa33be7"}, "docker": "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce6.ensgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene:3.2.2--r44hdfd78af_17
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene/3.2.2--r44hdfd78af_17
$ module help quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce6.ensgene/3.2.2--r44hdfd78af_17
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.celegans.ucsc.ce6.ensgene-inspect-deffile:

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