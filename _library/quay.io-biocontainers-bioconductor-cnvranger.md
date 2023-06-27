---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvranger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvranger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvranger/container.yaml"
updated_at: "2023-06-27 03:17:36.441120"
latest: "1.14.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvranger"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvranger"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvranger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvranger", "latest": {"1.14.0--r42hdfd78af_0": "sha256:b654516ae818115f05f4499265c5917992aff12d0da95029d2add1157045f275"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:cfb424da9abb5eadd1548300b1e32adf979cc6edd6f746664a4936cf7f508910", "1.14.0--r42hdfd78af_0": "sha256:b654516ae818115f05f4499265c5917992aff12d0da95029d2add1157045f275", "1.10.0--r41hdfd78af_0": "sha256:178d4e3eac95e42fcc54cad6ecdca3bad724626a360934c28b6b42d368ae1c84"}, "docker": "quay.io/biocontainers/bioconductor-cnvranger", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvranger.
shpc-registry automated BioContainers addition for bioconductor-cnvranger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvranger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvranger:1.14.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvranger/1.14.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvranger/1.14.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvranger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvranger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvranger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvranger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvranger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvranger-inspect-deffile:

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