---
layout: container
name:  "quay.io/biocontainers/bioconductor-batchelor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-batchelor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-batchelor/container.yaml"
updated_at: "2023-12-30 04:17:08.846850"
latest: "1.16.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-batchelor"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-batchelor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-batchelor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-batchelor", "latest": {"1.16.0--r43hf17093f_0": "sha256:e2fe0062c7af9fb6202a779d4283fd724740edc808a41cfb9706b77f1f45b92c"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:ee7381d35bd584376c2b50254c36edfeffbd637a10d1246b510a28ec3d867b9c", "1.14.0--r42hc247a5b_0": "sha256:9180ba84ccef356d4c778c238b6616ef0c672d95a624a13370ad7e64bca06c07", "1.10.0--r41hc247a5b_2": "sha256:49ca851c4acfbcd7e3403a10d7a34fed7580f6b3587c2c9ddb3d3c2d3d54befa", "1.14.0--r42hf17093f_1": "sha256:91679bca13ea1b6173af68d0942b094c34e48db192776cc89ef25c46f0f5b00f", "1.16.0--r43hf17093f_0": "sha256:e2fe0062c7af9fb6202a779d4283fd724740edc808a41cfb9706b77f1f45b92c"}, "docker": "quay.io/biocontainers/bioconductor-batchelor", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-batchelor.
shpc-registry automated BioContainers addition for bioconductor-batchelor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-batchelor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-batchelor:1.16.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-batchelor/1.16.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-batchelor/1.16.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-batchelor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-batchelor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-batchelor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-batchelor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-batchelor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-batchelor-inspect-deffile:

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