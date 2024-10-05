---
layout: container
name:  "quay.io/biocontainers/bioconductor-genogam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genogam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genogam/container.yaml"
updated_at: "2024-10-05 03:29:06.079462"
latest: "2.11.0--r41h619a076_1"
container_url: "https://biocontainers.pro/tools/bioconductor-genogam"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r40h399db7b_1"
 - "2.11.0--r41h619a076_1"
 - "2.10.0--r41h399db7b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genogam"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genogam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genogam", "latest": {"2.11.0--r41h619a076_1": "sha256:e3e5bf20282e699d17fbf5657e89a2bdf3a1820a74f67b3e1d5229ec67919007"}, "tags": {"2.8.0--r40h399db7b_1": "sha256:25aea260743100774e955088b36bf97dee07961fb39297d8effe4f5d1f9c642d", "2.11.0--r41h619a076_1": "sha256:e3e5bf20282e699d17fbf5657e89a2bdf3a1820a74f67b3e1d5229ec67919007", "2.10.0--r41h399db7b_0": "sha256:edfa41ad7908a866e81fec7f193ac5b26f8fff5026f1204cc395fbc8d90728f5"}, "docker": "quay.io/biocontainers/bioconductor-genogam", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genogam.
shpc-registry automated BioContainers addition for bioconductor-genogam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genogam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genogam:2.11.0--r41h619a076_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genogam/2.11.0--r41h619a076_1
$ module help quay.io/biocontainers/bioconductor-genogam/2.11.0--r41h619a076_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genogam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genogam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genogam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genogam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genogam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genogam-inspect-deffile:

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