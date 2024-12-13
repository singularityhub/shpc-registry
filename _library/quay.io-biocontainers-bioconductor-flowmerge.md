---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowmerge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowmerge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowmerge/container.yaml"
updated_at: "2024-12-13 03:40:15.948431"
latest: "2.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowmerge"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.40.0--r41hdfd78af_0"
 - "2.46.0--r42hdfd78af_0"
 - "2.48.0--r43hdfd78af_0"
 - "2.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowmerge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowmerge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowmerge", "latest": {"2.50.0--r43hdfd78af_0": "sha256:97205351570c402beac048461781b8359e90b46eea05de3692f66e7ca5591848"}, "tags": {"2.40.0--r41hdfd78af_0": "sha256:46190eb2cc7985afea40b6494d42b2077e89942686bd0b9d1386264cdf66dfa5", "2.46.0--r42hdfd78af_0": "sha256:794aeb400b2d7726598fd2da50cacae6672693343c4e8da121d5da59586da267", "2.48.0--r43hdfd78af_0": "sha256:899bac47d1fbe10c1c788f7a0ce6b82d2ea66aa9792fe0b75eccfdcd6903e278", "2.50.0--r43hdfd78af_0": "sha256:97205351570c402beac048461781b8359e90b46eea05de3692f66e7ca5591848"}, "docker": "quay.io/biocontainers/bioconductor-flowmerge", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowmerge.
shpc-registry automated BioContainers addition for bioconductor-flowmerge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmerge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowmerge:2.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowmerge/2.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowmerge/2.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowmerge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmerge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowmerge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowmerge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowmerge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowmerge-inspect-deffile:

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