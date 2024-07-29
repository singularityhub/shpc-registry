---
layout: container
name:  "quay.io/biocontainers/r-ddir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ddir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ddir/container.yaml"
updated_at: "2024-07-29 02:52:56.481599"
latest: "0.0.3--r43hdfd78af_5"
container_url: "https://biocontainers.pro/tools/r-ddir"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.3--r41hdfd78af_3"
 - "0.0.3--r42hdfd78af_4"
 - "0.0.3--r43hdfd78af_5"
description: "shpc-registry automated BioContainers addition for r-ddir"
config: {"url": "https://biocontainers.pro/tools/r-ddir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ddir", "latest": {"0.0.3--r43hdfd78af_5": "sha256:a0f93c6205afc6c7532f9386e3772accb0020030cb3e1095e643dbd49c46717a"}, "tags": {"0.0.3--r41hdfd78af_3": "sha256:b3e2b04a7cd1161f5b4b8af4d6f7eea37d6d84cd4ea0cd74cf59cc90afa357b3", "0.0.3--r42hdfd78af_4": "sha256:9b48b1fd17ea5b156733a803cd65c0cdae298e35d46b1d953a0dea6b0a2c0a6d", "0.0.3--r43hdfd78af_5": "sha256:a0f93c6205afc6c7532f9386e3772accb0020030cb3e1095e643dbd49c46717a"}, "docker": "quay.io/biocontainers/r-ddir", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ddir.
shpc-registry automated BioContainers addition for r-ddir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ddir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ddir:0.0.3--r43hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ddir/0.0.3--r43hdfd78af_5
$ module help quay.io/biocontainers/r-ddir/0.0.3--r43hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ddir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ddir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ddir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ddir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ddir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ddir-inspect-deffile:

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