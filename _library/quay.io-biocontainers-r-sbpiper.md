---
layout: container
name:  "quay.io/biocontainers/r-sbpiper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sbpiper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sbpiper/container.yaml"
updated_at: "2023-09-17 00:15:40.285882"
latest: "1.9.0--r43h3121a25_8"
container_url: "https://biocontainers.pro/tools/r-sbpiper"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r41h3121a25_6"
 - "1.9.0--r42h3121a25_7"
 - "1.9.0--r43h3121a25_8"
description: "shpc-registry automated BioContainers addition for r-sbpiper"
config: {"url": "https://biocontainers.pro/tools/r-sbpiper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sbpiper", "latest": {"1.9.0--r43h3121a25_8": "sha256:c2f2ab39a857c63dbdb3957ad1df8bd7cdbd9f792dc633809b48a0bc749c082c"}, "tags": {"1.9.0--r41h3121a25_6": "sha256:3f018bdabd4ff6d2aa17bbbf9d03fdd9d7ac0c9f6c9743554ef56461c28348d5", "1.9.0--r42h3121a25_7": "sha256:f41c33bc5a85a2dec60059a22f9e717e746c76f1ae1d4e780b6d60d0ce4712a3", "1.9.0--r43h3121a25_8": "sha256:c2f2ab39a857c63dbdb3957ad1df8bd7cdbd9f792dc633809b48a0bc749c082c"}, "docker": "quay.io/biocontainers/r-sbpiper", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sbpiper.
shpc-registry automated BioContainers addition for r-sbpiper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sbpiper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sbpiper:1.9.0--r43h3121a25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sbpiper/1.9.0--r43h3121a25_8
$ module help quay.io/biocontainers/r-sbpiper/1.9.0--r43h3121a25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sbpiper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sbpiper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sbpiper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sbpiper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sbpiper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sbpiper-inspect-deffile:

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