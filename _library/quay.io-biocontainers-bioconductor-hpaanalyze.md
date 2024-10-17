---
layout: container
name:  "quay.io/biocontainers/bioconductor-hpaanalyze"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hpaanalyze/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hpaanalyze/container.yaml"
updated_at: "2024-10-17 18:21:19.590970"
latest: "1.20.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hpaanalyze"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.1--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.1--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hpaanalyze"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hpaanalyze", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hpaanalyze", "latest": {"1.20.0--r43hdfd78af_1": "sha256:c05d3213e840a305183e747296b52eb8f1469f1b46e7499b2213963208bdfe85"}, "tags": {"1.8.1--r40hdfd78af_0": "sha256:9c4ca679c787cb7d2e8b09acebeef7a8b0ab4592b027623cfcd112fa3fc41eb5", "1.16.0--r42hdfd78af_0": "sha256:946332e367e75963fad4d6c236ade6234aaad170716f9fed7a4dad520b7cc171", "1.12.0--r41hdfd78af_0": "sha256:048c4c1631f7a015394448506e4987d9c8876bc5d972065165a74fa2a5a948f7", "1.10.0--r41hdfd78af_0": "sha256:594961da93c133d021178edde6c26f6d5f05c7189a505a99bbe66c259b8f762c", "1.18.1--r43hdfd78af_0": "sha256:7e3a3647092aa22eb5920b0498466c263141484e3bfd09d3862200d4bd65c446", "1.20.0--r43hdfd78af_1": "sha256:c05d3213e840a305183e747296b52eb8f1469f1b46e7499b2213963208bdfe85"}, "docker": "quay.io/biocontainers/bioconductor-hpaanalyze", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hpaanalyze.
shpc-registry automated BioContainers addition for bioconductor-hpaanalyze
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hpaanalyze
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hpaanalyze:1.20.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hpaanalyze/1.20.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-hpaanalyze/1.20.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hpaanalyze-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpaanalyze-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpaanalyze-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hpaanalyze-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hpaanalyze-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hpaanalyze-inspect-deffile:

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