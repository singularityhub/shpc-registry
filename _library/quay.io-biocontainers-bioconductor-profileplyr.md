---
layout: container
name:  "quay.io/biocontainers/bioconductor-profileplyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-profileplyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-profileplyr/container.yaml"
updated_at: "2024-07-27 02:57:43.354110"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-profileplyr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-profileplyr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-profileplyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-profileplyr", "latest": {"1.18.0--r43hdfd78af_0": "sha256:db377a57762517e184f93f594b05eb805dafe677d039d686e4b3ae5cac736ffb"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:c834dded7a708fa474d73436aa5f2c17676c641d4c5327bea8bc449d8686076d", "1.14.0--r42hdfd78af_0": "sha256:87e42ace19effa29fe0101bd402f791a43c67a389a0fcb344e89fd61844722cf", "1.10.0--r41hdfd78af_0": "sha256:4440f951c384b14b7f3833b01d6bc3d8ea526f177614b6498522e00a5a4efa91", "1.16.0--r43hdfd78af_0": "sha256:81e1a135a48769e953e0cba80430ea14457e18ebf5639b7e3b8501e3a40732c2", "1.18.0--r43hdfd78af_0": "sha256:db377a57762517e184f93f594b05eb805dafe677d039d686e4b3ae5cac736ffb"}, "docker": "quay.io/biocontainers/bioconductor-profileplyr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-profileplyr.
shpc-registry automated BioContainers addition for bioconductor-profileplyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-profileplyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-profileplyr:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-profileplyr/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-profileplyr/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-profileplyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profileplyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profileplyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-profileplyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-profileplyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-profileplyr-inspect-deffile:

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