---
layout: container
name:  "quay.io/biocontainers/r-structssi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-structssi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-structssi/container.yaml"
updated_at: "2023-10-12 02:38:31.695233"
latest: "1.1.1--r43h3121a25_10"
container_url: "https://biocontainers.pro/tools/r-structssi"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.1--r41h3121a25_8"
 - "1.1.1--r42h3121a25_9"
 - "1.1.1--r43h3121a25_10"
description: "shpc-registry automated BioContainers addition for r-structssi"
config: {"url": "https://biocontainers.pro/tools/r-structssi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-structssi", "latest": {"1.1.1--r43h3121a25_10": "sha256:bd33e18fc7c95e312f18d99186c426db79b450f806d8c65b14ac089c221f7260"}, "tags": {"1.1.1--r41h3121a25_8": "sha256:abcd68b8982fc07a9a122df3224efcfdc1d084c361e1a189c66c195e0dabb48b", "1.1.1--r42h3121a25_9": "sha256:8a3104d5e408707a6b72d3791d003916be97d6d1fd2a76971cf00ad5a3f52357", "1.1.1--r43h3121a25_10": "sha256:bd33e18fc7c95e312f18d99186c426db79b450f806d8c65b14ac089c221f7260"}, "docker": "quay.io/biocontainers/r-structssi", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-structssi.
shpc-registry automated BioContainers addition for r-structssi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-structssi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-structssi:1.1.1--r43h3121a25_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-structssi/1.1.1--r43h3121a25_10
$ module help quay.io/biocontainers/r-structssi/1.1.1--r43h3121a25_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-structssi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-structssi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-structssi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-structssi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-structssi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-structssi-inspect-deffile:

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