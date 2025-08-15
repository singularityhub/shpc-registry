---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74cprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74cprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74cprobe/container.yaml"
updated_at: "2025-08-15 05:52:11.410691"
latest: "2.18.0--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74cprobe"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.18.0--r41hdfd78af_8"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
 - "2.18.0--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74cprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74cprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74cprobe", "latest": {"2.18.0--r44hdfd78af_14": "sha256:2f54508dc415e080c4f4959161f03cb028c4b09b23810bc1a264322044426cb9"}, "tags": {"2.18.0--r41hdfd78af_8": "sha256:d67e3e7247a52753cc3bebc9cfef4ef1b1ee5643108968249accc7cf3b7a7717", "2.18.0--r41hdfd78af_10": "sha256:683724305d90da10a86f27162d25022d17b96567bb9cc351fd3bb06ea321843f", "2.18.0--r42hdfd78af_11": "sha256:57f0b07080918313255be7acf2192b8f6e7332e0eb728db13838c851990e413e", "2.18.0--r43hdfd78af_12": "sha256:19e8b587db2c7d26a8f47b5f1565059da979be1f6aec91f95796016b6e7bc59b", "2.18.0--r43hdfd78af_13": "sha256:b189fed2c4ff33a8861dbeab42c565a40c661e68b8d9a289c4a79c135940bc33", "2.18.0--r44hdfd78af_14": "sha256:2f54508dc415e080c4f4959161f03cb028c4b09b23810bc1a264322044426cb9"}, "docker": "quay.io/biocontainers/bioconductor-mgu74cprobe", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74cprobe.
shpc-registry automated BioContainers addition for bioconductor-mgu74cprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74cprobe:2.18.0--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74cprobe/2.18.0--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-mgu74cprobe/2.18.0--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74cprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74cprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74cprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74cprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74cprobe-inspect-deffile:

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