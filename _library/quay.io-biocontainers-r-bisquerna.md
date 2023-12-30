---
layout: container
name:  "quay.io/biocontainers/r-bisquerna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bisquerna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bisquerna/container.yaml"
updated_at: "2023-12-30 02:36:07.897440"
latest: "1.0.5--r43h3342da4_2"
container_url: "https://biocontainers.pro/tools/r-bisquerna"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.5--r41h3342da4_0"
 - "1.0.5--r42h3342da4_1"
 - "1.0.5--r43h3342da4_2"
description: "shpc-registry automated BioContainers addition for r-bisquerna"
config: {"url": "https://biocontainers.pro/tools/r-bisquerna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bisquerna", "latest": {"1.0.5--r43h3342da4_2": "sha256:29f1effcda6b45c575c9751d7f71e15538b755d15de08063a332d4e9070557b3"}, "tags": {"1.0.5--r41h3342da4_0": "sha256:84b55f1f8ceddd24767747c359efa63d1cb4eb9c790ed7e26bc02a083401ba7c", "1.0.5--r42h3342da4_1": "sha256:34bdce92bf6dc3f6d9096fe92351867a5722b42c8c822f2bf23b0bdbbe471c99", "1.0.5--r43h3342da4_2": "sha256:29f1effcda6b45c575c9751d7f71e15538b755d15de08063a332d4e9070557b3"}, "docker": "quay.io/biocontainers/r-bisquerna", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bisquerna.
shpc-registry automated BioContainers addition for r-bisquerna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bisquerna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bisquerna:1.0.5--r43h3342da4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bisquerna/1.0.5--r43h3342da4_2
$ module help quay.io/biocontainers/r-bisquerna/1.0.5--r43h3342da4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bisquerna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bisquerna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bisquerna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bisquerna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bisquerna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bisquerna-inspect-deffile:

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