---
layout: container
name:  "quay.io/biocontainers/r-ic10"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ic10/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ic10/container.yaml"
updated_at: "2024-04-05 02:55:49.129078"
latest: "1.5--r43h3121a25_6"
container_url: "https://biocontainers.pro/tools/r-ic10"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.5--r41h3121a25_4"
 - "1.5--r42h3121a25_5"
 - "1.5--r43h3121a25_6"
description: "shpc-registry automated BioContainers addition for r-ic10"
config: {"url": "https://biocontainers.pro/tools/r-ic10", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ic10", "latest": {"1.5--r43h3121a25_6": "sha256:48403415ff51b1ab119ea5946558977a8d312d69738e8c967bde4e01b6d4d518"}, "tags": {"1.5--r41h3121a25_4": "sha256:28f13f2b9420ed43859cff4bb2c1ede4e86a9d8d73b237e24f774e8c2729ea6f", "1.5--r42h3121a25_5": "sha256:cd3099f8b5b49a089ef3c46da6400d7b6880826c34e075718fdd5b037b28927c", "1.5--r43h3121a25_6": "sha256:48403415ff51b1ab119ea5946558977a8d312d69738e8c967bde4e01b6d4d518"}, "docker": "quay.io/biocontainers/r-ic10", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ic10.
shpc-registry automated BioContainers addition for r-ic10
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ic10
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ic10:1.5--r43h3121a25_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ic10/1.5--r43h3121a25_6
$ module help quay.io/biocontainers/r-ic10/1.5--r43h3121a25_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ic10-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ic10-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ic10-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ic10-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ic10-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ic10-inspect-deffile:

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