---
layout: container
name:  "quay.io/biocontainers/r-umi4c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-umi4c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-umi4c/container.yaml"
updated_at: "2023-08-08 02:52:27.326151"
latest: "0.0.1--r42hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-umi4c"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.1--r41hdfd78af_0"
 - "0.0.1--r42hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-umi4c"
config: {"url": "https://biocontainers.pro/tools/r-umi4c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-umi4c", "latest": {"0.0.1--r42hdfd78af_1": "sha256:f738399c16d0bf252db12ce39dd2030c874c84661e8d3bedf67455f706c6811a"}, "tags": {"0.0.1--r41hdfd78af_0": "sha256:6da7729e46ad34039d086f7c19692a0be07998157fd253b8dafa1132ae857f26", "0.0.1--r42hdfd78af_1": "sha256:f738399c16d0bf252db12ce39dd2030c874c84661e8d3bedf67455f706c6811a"}, "docker": "quay.io/biocontainers/r-umi4c", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-umi4c.
shpc-registry automated BioContainers addition for r-umi4c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-umi4c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-umi4c:0.0.1--r42hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-umi4c/0.0.1--r42hdfd78af_1
$ module help quay.io/biocontainers/r-umi4c/0.0.1--r42hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-umi4c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-umi4c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-umi4c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-umi4c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-umi4c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-umi4c-inspect-deffile:

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