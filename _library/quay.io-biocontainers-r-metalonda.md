---
layout: container
name:  "quay.io/biocontainers/r-metalonda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-metalonda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-metalonda/container.yaml"
updated_at: "2022-11-20 23:53:39.174233"
latest: "1.1.8--r41h3121a25_3"
container_url: "https://biocontainers.pro/tools/r-metalonda"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.8--r41h3121a25_3"
description: "shpc-registry automated BioContainers addition for r-metalonda"
config: {"url": "https://biocontainers.pro/tools/r-metalonda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-metalonda", "latest": {"1.1.8--r41h3121a25_3": "sha256:e696bc54d78c7a05db3604cecddda9809fd00eeb82b3b80d1d9db99366b41e06"}, "tags": {"1.1.8--r41h3121a25_3": "sha256:e696bc54d78c7a05db3604cecddda9809fd00eeb82b3b80d1d9db99366b41e06"}, "docker": "quay.io/biocontainers/r-metalonda", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-metalonda.
shpc-registry automated BioContainers addition for r-metalonda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-metalonda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-metalonda:1.1.8--r41h3121a25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-metalonda/1.1.8--r41h3121a25_3
$ module help quay.io/biocontainers/r-metalonda/1.1.8--r41h3121a25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-metalonda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-metalonda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-metalonda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-metalonda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-metalonda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-metalonda-inspect-deffile:

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