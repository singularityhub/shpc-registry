---
layout: container
name:  "quay.io/biocontainers/bioconductor-sesame"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sesame/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sesame/container.yaml"
updated_at: "2023-10-21 02:47:14.959489"
latest: "1.18.4--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sesame"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.2--r40hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.3--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.18.4--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sesame"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sesame", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sesame", "latest": {"1.18.4--r43hdfd78af_0": "sha256:8ccec482764e889b995b604787aa69e853fdf15785eccfcfb4a375e568a9a954"}, "tags": {"1.8.2--r40hdfd78af_0": "sha256:4695c2afe25ac3ce5908e7f878466870d6129796f9e3d3c7bb6cfb640bcd3d25", "1.12.0--r41hdfd78af_0": "sha256:5c122a1473543183127a7adeb4440ff10124b6997c8476864c76b1d95e8f50ad", "1.10.3--r41hdfd78af_0": "sha256:007b12a01e3653b2aedf514cbd0b94dd73fa1e7f259f1ef1adb5c031d77b14d4", "1.16.0--r42hdfd78af_0": "sha256:40259f34661ed7c98bc2481c704c8f581bfff7fd8c8e7be851ca615501db7982", "1.18.4--r43hdfd78af_0": "sha256:8ccec482764e889b995b604787aa69e853fdf15785eccfcfb4a375e568a9a954"}, "docker": "quay.io/biocontainers/bioconductor-sesame", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sesame.
shpc-registry automated BioContainers addition for bioconductor-sesame
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sesame
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sesame:1.18.4--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sesame/1.18.4--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sesame/1.18.4--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sesame-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sesame-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sesame-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sesame-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sesame-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sesame-inspect-deffile:

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