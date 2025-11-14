---
layout: container
name:  "quay.io/biocontainers/bioconductor-qsmooth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qsmooth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qsmooth/container.yaml"
updated_at: "2025-11-14 03:48:08.055670"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qsmooth"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qsmooth"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qsmooth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qsmooth", "latest": {"1.22.0--r44hdfd78af_0": "sha256:a09e950bf3785fe3ab4a13d31f143dde4363e54af794710e448e34278df57a09"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:d50b34489fcadd9336fd795d8a886e8ef5057a62f2a563762e534ee910d287a7", "1.10.0--r41hdfd78af_0": "sha256:64894bda9343e45573e5e162bd3925b87b15ef310510eefaf153d874817aa902", "1.14.0--r42hdfd78af_0": "sha256:f7c290f69d93d07775dc04ce522430f34dc7121a2a6eafea961b1de28a1ec1f2", "1.16.0--r43hdfd78af_0": "sha256:9f8f599ca46a8a4d849508fbaf0e0c50f32716f80652552fee217ee349c9d0a6", "1.18.0--r43hdfd78af_0": "sha256:2c572d1d81898ad64bf444289d4f84031906df8bb394583415246e12aff2c58f", "1.22.0--r44hdfd78af_0": "sha256:a09e950bf3785fe3ab4a13d31f143dde4363e54af794710e448e34278df57a09"}, "docker": "quay.io/biocontainers/bioconductor-qsmooth", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qsmooth.
shpc-registry automated BioContainers addition for bioconductor-qsmooth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qsmooth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qsmooth:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qsmooth/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qsmooth/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qsmooth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qsmooth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qsmooth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qsmooth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qsmooth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qsmooth-inspect-deffile:

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