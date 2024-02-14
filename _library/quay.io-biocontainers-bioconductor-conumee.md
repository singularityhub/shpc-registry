---
layout: container
name:  "quay.io/biocontainers/bioconductor-conumee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-conumee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-conumee/container.yaml"
updated_at: "2024-02-14 02:24:44.580420"
latest: "1.32.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-conumee"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-conumee"
config: {"url": "https://biocontainers.pro/tools/bioconductor-conumee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-conumee", "latest": {"1.32.0--r42hdfd78af_0": "sha256:fa3ad70fda526e0e4111a339fc549adb7289b61cafc1fb61119c90e272a21e28"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:19dead2ba50e3dc6fbbd19c56ba9c1a7651e3f91d559e4b5557fe760ae4695ef", "1.32.0--r42hdfd78af_0": "sha256:fa3ad70fda526e0e4111a339fc549adb7289b61cafc1fb61119c90e272a21e28"}, "docker": "quay.io/biocontainers/bioconductor-conumee", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-conumee.
shpc-registry automated BioContainers addition for bioconductor-conumee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-conumee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-conumee:1.32.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-conumee/1.32.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-conumee/1.32.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-conumee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-conumee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-conumee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-conumee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-conumee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-conumee-inspect-deffile:

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