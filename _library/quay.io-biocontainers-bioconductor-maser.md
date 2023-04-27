---
layout: container
name:  "quay.io/biocontainers/bioconductor-maser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maser/container.yaml"
updated_at: "2023-04-27 03:12:33.547495"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maser"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maser", "latest": {"1.16.0--r42hdfd78af_0": "sha256:e9f90d75476e856141ef2c4d6ae896a5224b606ebf8795852bad1fd1e536638c"}, "tags": {"1.8.0--r40hdfd78af_0": "sha256:d20a73643300ba80f8461a8bc9af1b670f6c2c64f76d203bece8d807a6e0fd40", "1.12.0--r41hdfd78af_0": "sha256:9d6b3be3c3082465febb1536af8af0affe50ddcf18dbafa48a2c28b87def0300", "1.10.0--r41hdfd78af_0": "sha256:7691544c91c4c79271889d1b77228b7f99870cb54bf0d733bdc1be49df632120", "1.16.0--r42hdfd78af_0": "sha256:e9f90d75476e856141ef2c4d6ae896a5224b606ebf8795852bad1fd1e536638c"}, "docker": "quay.io/biocontainers/bioconductor-maser", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maser.
shpc-registry automated BioContainers addition for bioconductor-maser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maser:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maser/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maser/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maser-inspect-deffile:

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