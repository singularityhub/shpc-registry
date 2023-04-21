---
layout: container
name:  "quay.io/biocontainers/bioconductor-erssa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-erssa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-erssa/container.yaml"
updated_at: "2023-04-21 02:34:26.238223"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-erssa"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-erssa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-erssa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-erssa", "latest": {"1.16.0--r42hdfd78af_0": "sha256:69e0a9ed8f498fe04b7e42f63dd73329cdae668f25eddb4c7bb7ab019bf4570b"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:b33eb925dc6d19f82024b60bddbfa5a6316b551f11cc1041fb8b1517208f680c", "1.16.0--r42hdfd78af_0": "sha256:69e0a9ed8f498fe04b7e42f63dd73329cdae668f25eddb4c7bb7ab019bf4570b", "1.12.0--r41hdfd78af_0": "sha256:08491a6726145828c7a3b2bb91ffed59df4d036dd28e5ca37c8fe45fe1f99774", "1.10.0--r41hdfd78af_0": "sha256:47b451edd788ee9190658f5e005bec67f381011bfad76867c0717d7c625cd4ce"}, "docker": "quay.io/biocontainers/bioconductor-erssa", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-erssa.
shpc-registry automated BioContainers addition for bioconductor-erssa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-erssa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-erssa:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-erssa/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-erssa/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-erssa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erssa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erssa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-erssa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-erssa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-erssa-inspect-deffile:

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