---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparsenetgls"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparsenetgls/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparsenetgls/container.yaml"
updated_at: "2024-11-20 03:08:22.633525"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sparsenetgls"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sparsenetgls"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparsenetgls", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sparsenetgls", "latest": {"1.20.0--r43hdfd78af_0": "sha256:7022d20870c2d06e8297dd1e319cbadd4367477db9d68e20815854f380fc5436"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:e4e92b80181eaf234f3f1e3b9d2dfa7a43412c526055aa5d1008dd2edceb77a8", "1.16.0--r42hdfd78af_0": "sha256:ed88f3530745cf9b11cf8adfa81398a44c6d75af9ed0db15553492ebab4c94f9", "1.12.0--r41hdfd78af_0": "sha256:b250931556b6a4cf80465f6e5c72d9b62afd17a1ad12fad3b1eb0754b8f9628b", "1.10.0--r41hdfd78af_0": "sha256:58f795e58d2f59abfa94f6cc87a978f6e3eb38d4be5c6528abc47b5ba1d068d4", "1.18.0--r43hdfd78af_0": "sha256:0f66b9da74a33933166d5f2ff2e802833a5729d46cda0a4bfd1fec781c0b0677", "1.20.0--r43hdfd78af_0": "sha256:7022d20870c2d06e8297dd1e319cbadd4367477db9d68e20815854f380fc5436"}, "docker": "quay.io/biocontainers/bioconductor-sparsenetgls", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparsenetgls.
shpc-registry automated BioContainers addition for bioconductor-sparsenetgls
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsenetgls
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsenetgls:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparsenetgls/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sparsenetgls/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparsenetgls-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsenetgls-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsenetgls-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparsenetgls-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparsenetgls-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparsenetgls-inspect-deffile:

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