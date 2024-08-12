---
layout: container
name:  "quay.io/biocontainers/bioconductor-tabulamurisdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tabulamurisdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tabulamurisdata/container.yaml"
updated_at: "2024-08-12 03:21:41.156115"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tabulamurisdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tabulamurisdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tabulamurisdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tabulamurisdata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:2a7fb60ae12b1716e06566c640a20ee454f2e80d34df8bf684318c7149e10bf6"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:9abed4edeb2be03b4cd4fd9e3fdb3d860419b4581ac3fb0ed720e2945b4b0855", "1.16.0--r42hdfd78af_0": "sha256:597cd3bf425816d8bb24eb4db10039def963f6f6621011a5cc6902d6c649f244", "1.12.0--r41hdfd78af_1": "sha256:67e7ff7446c0c1510162ea45b6125dd4729c4dd66add7a0bc297918746eb5cb8", "1.10.0--r41hdfd78af_0": "sha256:d947b71460f6e114d564b79e40ef3b44282c45e25674a9442ee5545fa1b0a947", "1.18.0--r43hdfd78af_0": "sha256:17caef36a3d2d770105bf3b14b7b68299f5f3be88324c1e2dfe43682cb33ee90", "1.20.0--r43hdfd78af_0": "sha256:2a7fb60ae12b1716e06566c640a20ee454f2e80d34df8bf684318c7149e10bf6"}, "docker": "quay.io/biocontainers/bioconductor-tabulamurisdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tabulamurisdata.
shpc-registry automated BioContainers addition for bioconductor-tabulamurisdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tabulamurisdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tabulamurisdata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tabulamurisdata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tabulamurisdata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tabulamurisdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tabulamurisdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tabulamurisdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tabulamurisdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tabulamurisdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tabulamurisdata-inspect-deffile:

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