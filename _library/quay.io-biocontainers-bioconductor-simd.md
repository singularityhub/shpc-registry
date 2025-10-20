---
layout: container
name:  "quay.io/biocontainers/bioconductor-simd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simd/container.yaml"
updated_at: "2025-10-20 03:50:20.868771"
latest: "1.20.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simd"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hd029910_1"
 - "1.16.0--r42hc0cfd56_0"
 - "1.12.0--r41hc0cfd56_2"
 - "1.10.0--r41hd029910_0"
 - "1.16.0--r42ha9d7317_1"
 - "1.18.0--r43ha9d7317_0"
 - "1.20.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simd"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simd", "latest": {"1.20.0--r43ha9d7317_0": "sha256:fc6d60c3b2644cf976d0f5aa5ce94f60171cbc6113ed6cf7d399cbd850e51684"}, "tags": {"1.8.0--r40hd029910_1": "sha256:41135bd62c1dfada774280070b2ad4e7088def851857bb0025aafad5cd6ae277", "1.16.0--r42hc0cfd56_0": "sha256:945b409d9c9096b82c4923ca75ef58153d09ace99ea7f2100da4f8e8a60c8201", "1.12.0--r41hc0cfd56_2": "sha256:6dfd6dddeecab262d27191f16ded42db6f1650a7b88122e42e02b803198782c7", "1.10.0--r41hd029910_0": "sha256:0370c7870c0ec7067d01084b64b8b5a587b3548d43e04e5e9caf96dcd7a75dea", "1.16.0--r42ha9d7317_1": "sha256:c30d2644f20510dee9f73e45103394c250b42b1b58a2744422e1139184a3ec03", "1.18.0--r43ha9d7317_0": "sha256:5ded394dace046a1d15d83d03c256a1a20fdaee3112190f62037e04c8456555a", "1.20.0--r43ha9d7317_0": "sha256:fc6d60c3b2644cf976d0f5aa5ce94f60171cbc6113ed6cf7d399cbd850e51684"}, "docker": "quay.io/biocontainers/bioconductor-simd", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simd.
shpc-registry automated BioContainers addition for bioconductor-simd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simd:1.20.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simd/1.20.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-simd/1.20.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simd-inspect-deffile:

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