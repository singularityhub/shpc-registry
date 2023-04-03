---
layout: container
name:  "quay.io/biocontainers/bioconductor-copyneutralima"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copyneutralima/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copyneutralima/container.yaml"
updated_at: "2023-04-03 04:04:39.625416"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-copyneutralima"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-copyneutralima"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copyneutralima", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copyneutralima", "latest": {"1.16.0--r42hdfd78af_0": "sha256:63b60f0a575013d0d9b174818d794a4d454eeab9b290da09be9f271758b0da16"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:0728f30629f1046cfb6e6595cd460cf524628a5a62b399a134101f4eb424ce36", "1.12.0--r41hdfd78af_1": "sha256:29a306b21f5c19a8d9a3f0430717dcf13429e27891bb5de9471bed59baea118a", "1.10.0--r41hdfd78af_0": "sha256:4db48ef61609205e229641abac8f316ee77c356b943dc1740c921bcdb4b926e3", "1.16.0--r42hdfd78af_0": "sha256:63b60f0a575013d0d9b174818d794a4d454eeab9b290da09be9f271758b0da16"}, "docker": "quay.io/biocontainers/bioconductor-copyneutralima", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copyneutralima.
shpc-registry automated BioContainers addition for bioconductor-copyneutralima
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copyneutralima
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copyneutralima:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copyneutralima/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-copyneutralima/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copyneutralima-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copyneutralima-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copyneutralima-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copyneutralima-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copyneutralima-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copyneutralima-inspect-deffile:

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