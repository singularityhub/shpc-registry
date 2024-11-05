---
layout: container
name:  "quay.io/biocontainers/bioconductor-alevinqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alevinqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alevinqc/container.yaml"
updated_at: "2024-11-05 03:10:55.418947"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-alevinqc"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.12.1--r41h9f5acd7_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-alevinqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alevinqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alevinqc", "latest": {"1.18.0--r43hf17093f_0": "sha256:81f51b86ddee970bd27bbdd754a6ef65f427919b47fe6401b03a7949678f8ea6"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:f2b65a2313e0842a429c2380314b17275fb11d282bd11d895a86d8331b0d0e5c", "1.14.0--r42hc247a5b_0": "sha256:71e7e7d00b492ad8912cfa9e6a1f641b007f88220318e56651a4a43ad7bc3656", "1.12.1--r41h9f5acd7_0": "sha256:d8ff55d336d1c45cb5d06037b8c094eced2375e54bf6ca9d72bbc725c403731d", "1.10.0--r41hdfd78af_0": "sha256:5b2bab5fcd35a9ba373412ee1805ad83e56c117f8f1057b890ad53933cf48182", "1.14.0--r42hf17093f_1": "sha256:4b8952d75dbf91e87072b8521c48c5b3c3042a97d204ee5b9fa50aa138330364", "1.16.0--r43hf17093f_0": "sha256:f22205e28d085034c19b5d08dc2461e919c5df34a098063ca620c281b55cd23a", "1.18.0--r43hf17093f_0": "sha256:81f51b86ddee970bd27bbdd754a6ef65f427919b47fe6401b03a7949678f8ea6"}, "docker": "quay.io/biocontainers/bioconductor-alevinqc", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alevinqc.
shpc-registry automated BioContainers addition for bioconductor-alevinqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alevinqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alevinqc:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alevinqc/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-alevinqc/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alevinqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alevinqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alevinqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alevinqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alevinqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alevinqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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