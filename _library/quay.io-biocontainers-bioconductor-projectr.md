---
layout: container
name:  "quay.io/biocontainers/bioconductor-projectr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-projectr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-projectr/container.yaml"
updated_at: "2025-05-17 03:18:33.468392"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-projectr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-projectr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-projectr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-projectr", "latest": {"1.22.0--r44hdfd78af_0": "sha256:97ca32daa7bc552c8363f9815b1149e73b3f1522d9dae2185d4106feb11a584a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:4368ce3dff1872715f03b2d6fd60eb989253c60d1dc8805dc2af17a429ac0e36", "1.14.0--r42hdfd78af_0": "sha256:0ac1e0a478cd2a62a72c4c80e2d3dbe09018df2ca4d5dd7e7d441588b1ff4cd3", "1.10.0--r41hdfd78af_0": "sha256:dbca4f96bcc5b0dbe268e4d6d738089928444f31c8be9b0891dc5442a310428d", "1.16.0--r43hdfd78af_0": "sha256:a3b5ec35c11cebf26300680450f2efe569e999c05980dfea81687764e409915d", "1.18.0--r43hdfd78af_0": "sha256:2f226518236c7f5eedb75e01572cecf01d135ba01c96546b6e1053d921e68cf1", "1.22.0--r44hdfd78af_0": "sha256:97ca32daa7bc552c8363f9815b1149e73b3f1522d9dae2185d4106feb11a584a"}, "docker": "quay.io/biocontainers/bioconductor-projectr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-projectr.
shpc-registry automated BioContainers addition for bioconductor-projectr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-projectr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-projectr:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-projectr/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-projectr/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-projectr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-projectr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-projectr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-projectr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-projectr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-projectr-inspect-deffile:

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