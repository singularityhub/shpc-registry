---
layout: container
name:  "quay.io/biocontainers/bioconductor-xeva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xeva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xeva/container.yaml"
updated_at: "2025-05-28 03:39:17.493697"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xeva"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xeva"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xeva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xeva", "latest": {"1.22.0--r44hdfd78af_0": "sha256:89dfb206267ce0fcb41818151e77a0bd02f844b7d9287688b590c06307be99b5"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:43eac95eb0c459a53ea934b8255163e5ce36e52f34fbcd569b01f07e50d9b518", "1.14.0--r42hdfd78af_0": "sha256:036f7d52714230230f72de6df4c18e80ad4327ba0d65140292937406fd0e0458", "1.10.0--r41hdfd78af_0": "sha256:e9d26fab3f7269e6e5d3d86a8d1ba6422ca4dcf9294c0cab98fed6eb0e8d3122", "1.16.0--r43hdfd78af_0": "sha256:8efea98a1851404639df5fe914b25df7f150e026569dbea5c61e227044777a45", "1.18.0--r43hdfd78af_0": "sha256:bd88f062adab229f0b2028a778fb05c283635df0e68b7efa71c9b7e382dc14a1", "1.22.0--r44hdfd78af_0": "sha256:89dfb206267ce0fcb41818151e77a0bd02f844b7d9287688b590c06307be99b5"}, "docker": "quay.io/biocontainers/bioconductor-xeva", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xeva.
shpc-registry automated BioContainers addition for bioconductor-xeva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xeva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xeva:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xeva/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xeva/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xeva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xeva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xeva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xeva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xeva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xeva-inspect-deffile:

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