---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene/container.yaml"
updated_at: "2023-03-30 03:33:31.813505"
latest: "3.2.2--r42hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.2--r40_9"
 - "3.2.2--r42hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg18.knowngene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg18.knowngene", "latest": {"3.2.2--r42hdfd78af_14": "sha256:9c4841299fd129d265a411b3d6831c559a8119a8aa2ca1256bc8aae3035f31b6"}, "tags": {"3.2.2--r40_9": "sha256:c1ee7af71dd5efdfa491302da0cd86e441a8d2bccdc1b1c92166a2ba09f6be32", "3.2.2--r42hdfd78af_14": "sha256:9c4841299fd129d265a411b3d6831c559a8119a8aa2ca1256bc8aae3035f31b6"}, "docker": "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene.
shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg18.knowngene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene:3.2.2--r42hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene/3.2.2--r42hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg18.knowngene/3.2.2--r42hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg18.knowngene-inspect-deffile:

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