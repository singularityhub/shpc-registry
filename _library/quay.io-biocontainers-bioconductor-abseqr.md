---
layout: container
name:  "quay.io/biocontainers/bioconductor-abseqr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-abseqr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-abseqr/container.yaml"
updated_at: "2024-01-01 02:50:42.974595"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-abseqr"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-abseqr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-abseqr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-abseqr", "latest": {"1.20.0--r43hdfd78af_0": "sha256:7fa7b7a2bf3aa4330ed992d9880cf2ffd044f231e76527a7c3da44fe37eeeef0"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:11aba41abfea4cbcbd1451f0f4e74584b89e53101327dd5aa6f6e9106b928f98", "1.16.0--r42hdfd78af_0": "sha256:4598bcec2c8faad9fae2931cd77ea81acda28cc8996d863f9aeaf2e9109e7d68", "1.12.0--r41hdfd78af_0": "sha256:e5b5d715b8836789539af9bc4e5116502cb2178756c7882c64eae8e6e23b4c39", "1.10.0--r41hdfd78af_0": "sha256:a9d30644c9fb56d9535f7de1df1626834f167605c8cc372809afdc85e5864ab7", "1.18.0--r43hdfd78af_0": "sha256:d2d48e502a9af93f745068c74472788aa5e939de13d0a4098d486bac5098006e", "1.20.0--r43hdfd78af_0": "sha256:7fa7b7a2bf3aa4330ed992d9880cf2ffd044f231e76527a7c3da44fe37eeeef0"}, "docker": "quay.io/biocontainers/bioconductor-abseqr", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-abseqr.
shpc-registry automated BioContainers addition for bioconductor-abseqr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-abseqr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-abseqr:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-abseqr/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-abseqr/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-abseqr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abseqr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abseqr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-abseqr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-abseqr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-abseqr-inspect-deffile:

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