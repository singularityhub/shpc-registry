---
layout: container
name:  "quay.io/biocontainers/bioconductor-complexheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-complexheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-complexheatmap/container.yaml"
updated_at: "2024-01-01 03:20:44.004354"
latest: "2.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-complexheatmap"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-complexheatmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-complexheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-complexheatmap", "latest": {"2.18.0--r43hdfd78af_0": "sha256:77a4efc4a56725040fc354ec10b81a0a67d84e0db2cec7d6c2137a13dcc2bd4d"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:d29dedb8362cfca2ecc457310c24c64f92d77762b83cbd2c04cf8b2d881cde94", "2.14.0--r42hdfd78af_0": "sha256:de8bd94b5677e2f1280a1819eb24e0889e40ece916aae343cf80e2822ef19c78", "2.10.0--r41hdfd78af_0": "sha256:0de102719b0332c18a014fe980af8417ac25ed4a82d9283c28db1de9f0f38def", "2.16.0--r43hdfd78af_0": "sha256:e8b4448f0c232a8805baca10a585d4dcaf30028d82e02bbe63f5b398f38d0795", "2.18.0--r43hdfd78af_0": "sha256:77a4efc4a56725040fc354ec10b81a0a67d84e0db2cec7d6c2137a13dcc2bd4d"}, "docker": "quay.io/biocontainers/bioconductor-complexheatmap", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-complexheatmap.
shpc-registry automated BioContainers addition for bioconductor-complexheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-complexheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-complexheatmap:2.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-complexheatmap/2.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-complexheatmap/2.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-complexheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-complexheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-complexheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-complexheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-complexheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-complexheatmap-inspect-deffile:

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