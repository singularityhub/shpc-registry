---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene/container.yaml"
updated_at: "2024-01-01 03:18:28.466193"
latest: "3.2.2--r43hdfd78af_15"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.2--r40_9"
 - "3.2.2--r41hdfd78af_13"
 - "3.2.2--r42hdfd78af_14"
 - "3.2.2--r43hdfd78af_15"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg19.knowngene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg19.knowngene", "latest": {"3.2.2--r43hdfd78af_15": "sha256:457d19992288064fa9a2cd2b25191a890753ef429abb57958a18d0b10b40920c"}, "tags": {"3.2.2--r40_9": "sha256:0b83400fbef270c9a2cc6da052178d23e4f45be76216783cd0afe0eb32924a08", "3.2.2--r41hdfd78af_13": "sha256:2e032e5b8e95ac55031d314df8ab512e743938d79b022bc911bbf235c9893de3", "3.2.2--r42hdfd78af_14": "sha256:d7dd700466f59c18d6a7e453c38f2fbef201937e81deff085dd6607f196c1781", "3.2.2--r43hdfd78af_15": "sha256:457d19992288064fa9a2cd2b25191a890753ef429abb57958a18d0b10b40920c"}, "docker": "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene.
shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg19.knowngene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene:3.2.2--r43hdfd78af_15
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene/3.2.2--r43hdfd78af_15
$ module help quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg19.knowngene/3.2.2--r43hdfd78af_15
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-inspect-deffile:

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