---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75/container.yaml"
updated_at: "2026-02-02 05:00:44.690750"
latest: "2.99.0--r44hdfd78af_16"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.hsapiens.v75"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.99.0--r40hdfd78af_9"
 - "2.99.0--r42hdfd78af_13"
 - "2.99.0--r43hdfd78af_14"
 - "2.99.0--r43hdfd78af_15"
 - "2.99.0--r44hdfd78af_16"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v75"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.hsapiens.v75", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v75", "latest": {"2.99.0--r44hdfd78af_16": "sha256:2adb6d3be5195b824a1d892da4b089d931ccced9b0ea21fb2a67141d299e3c2b"}, "tags": {"2.99.0--r40hdfd78af_9": "sha256:0af9ffae60af053bd2d6c2bc5bdedd02d5539fd0b7aa2558848957919b90c319", "2.99.0--r42hdfd78af_13": "sha256:d40414d2dd25e918595e2df5542456559b5e08935c557790662196f14e7a921d", "2.99.0--r43hdfd78af_14": "sha256:776a3db37ad8db58d36b5857721f9a006035fe2199e4d4e2c4b3efd10520ef3a", "2.99.0--r43hdfd78af_15": "sha256:92df4c082d6a925dd05b3ba004dfa57a9f4b1d988ebd8081db3f2479260e2506", "2.99.0--r44hdfd78af_16": "sha256:2adb6d3be5195b824a1d892da4b089d931ccced9b0ea21fb2a67141d299e3c2b"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75.
shpc-registry automated BioContainers addition for bioconductor-ensdb.hsapiens.v75
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75:2.99.0--r44hdfd78af_16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75/2.99.0--r44hdfd78af_16
$ module help quay.io/biocontainers/bioconductor-ensdb.hsapiens.v75/2.99.0--r44hdfd78af_16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.hsapiens.v75-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.hsapiens.v75-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.hsapiens.v75-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.hsapiens.v75-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.hsapiens.v75-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.hsapiens.v75-inspect-deffile:

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