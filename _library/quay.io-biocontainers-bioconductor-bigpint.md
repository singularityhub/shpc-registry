---
layout: container
name:  "quay.io/biocontainers/bioconductor-bigpint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bigpint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bigpint/container.yaml"
updated_at: "2025-07-27 04:18:39.849705"
latest: "1.15.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bigpint"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.15.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bigpint"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bigpint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bigpint", "latest": {"1.15.0--r43hdfd78af_0": "sha256:8d70fa49ff29d8e75dae4e83291c4e48e601f486e77ad78a49bab2a80f577309"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:369eea5632d623a45da1b0c3561607b9750a7f7054bbab8260dab59e8c3e53b8", "1.14.0--r42hdfd78af_0": "sha256:360160f6e390c99467963e7e4ddfdd0179c57d7ce1c8ed06d6dbd2b04c24fdc0", "1.10.0--r41hdfd78af_0": "sha256:cc6f0fbbd0296fa3afce05d6afaaee6f1c9fcddaf898066b57336ebd8880919b", "1.15.0--r43hdfd78af_0": "sha256:8d70fa49ff29d8e75dae4e83291c4e48e601f486e77ad78a49bab2a80f577309"}, "docker": "quay.io/biocontainers/bioconductor-bigpint", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bigpint.
shpc-registry automated BioContainers addition for bioconductor-bigpint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bigpint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bigpint:1.15.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bigpint/1.15.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bigpint/1.15.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bigpint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bigpint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bigpint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bigpint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bigpint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bigpint-inspect-deffile:

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