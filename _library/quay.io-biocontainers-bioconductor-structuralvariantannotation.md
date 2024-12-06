---
layout: container
name:  "quay.io/biocontainers/bioconductor-structuralvariantannotation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-structuralvariantannotation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-structuralvariantannotation/container.yaml"
updated_at: "2024-12-06 03:43:39.598544"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-structuralvariantannotation"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-structuralvariantannotation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-structuralvariantannotation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-structuralvariantannotation", "latest": {"1.18.0--r43hdfd78af_0": "sha256:0e2abf54ba0579a8e198f197af820da40001fb0bb8d0bfa02de260e898d7387b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:70a34ebffa62d1c3e2d9af0da0825a71d58a314a6fe0e0b156a20f7a03c05f8f", "1.13.0--r42hdfd78af_0": "sha256:e43df95940d5ee24ecd86e4d33aa26341ca2b555889818c1df0ae6383782f8fd", "1.10.0--r41hdfd78af_0": "sha256:b74008a8312cb0f21550ce10e220de118fceffeecf0931812d5ef3cf82e69a48", "1.16.0--r43hdfd78af_0": "sha256:a8cf7ef3481615a67a5c110758be542bf3348199933f8ec8c22c71d0165bb8ab", "1.18.0--r43hdfd78af_0": "sha256:0e2abf54ba0579a8e198f197af820da40001fb0bb8d0bfa02de260e898d7387b"}, "docker": "quay.io/biocontainers/bioconductor-structuralvariantannotation", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-structuralvariantannotation.
shpc-registry automated BioContainers addition for bioconductor-structuralvariantannotation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-structuralvariantannotation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-structuralvariantannotation:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-structuralvariantannotation/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-structuralvariantannotation/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-structuralvariantannotation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-structuralvariantannotation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-structuralvariantannotation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-structuralvariantannotation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-structuralvariantannotation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-structuralvariantannotation-inspect-deffile:

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