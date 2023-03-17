---
layout: container
name:  "quay.io/biocontainers/r-aroma.core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-aroma.core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-aroma.core/container.yaml"
updated_at: "2023-03-17 02:54:03.567096"
latest: "3.3.0--r42h3121a25_0"
container_url: "https://biocontainers.pro/tools/r-aroma.core"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.2--r41h3121a25_1"
 - "3.3.0--r42h3121a25_0"
 - "3.2.2--r42h3121a25_2"
description: "shpc-registry automated BioContainers addition for r-aroma.core"
config: {"url": "https://biocontainers.pro/tools/r-aroma.core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-aroma.core", "latest": {"3.3.0--r42h3121a25_0": "sha256:d44b3cd58199079c5a52d5f9aa3c79136d48406ade66ea8f792f741eee7d03e3"}, "tags": {"3.2.2--r41h3121a25_1": "sha256:99a2048cfa648bf013f4ac1e053d9c0db925aa0445e668fcf0ab45dee5b523b5", "3.3.0--r42h3121a25_0": "sha256:d44b3cd58199079c5a52d5f9aa3c79136d48406ade66ea8f792f741eee7d03e3", "3.2.2--r42h3121a25_2": "sha256:37b53a031ce27380cee6a5acdb1b3fd646f46fbea54ab22381344c9be22f294d"}, "docker": "quay.io/biocontainers/r-aroma.core", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-aroma.core.
shpc-registry automated BioContainers addition for r-aroma.core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-aroma.core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-aroma.core:3.3.0--r42h3121a25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-aroma.core/3.3.0--r42h3121a25_0
$ module help quay.io/biocontainers/r-aroma.core/3.3.0--r42h3121a25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-aroma.core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-aroma.core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-aroma.core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-aroma.core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-aroma.core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-aroma.core-inspect-deffile:

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