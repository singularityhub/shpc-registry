---
layout: container
name:  "quay.io/biocontainers/bioconductor-sspa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sspa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sspa/container.yaml"
updated_at: "2025-03-20 04:22:06.384036"
latest: "2.30.0--r40hd029910_1"
container_url: "https://biocontainers.pro/tools/bioconductor-sspa"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.30.0--r40hd029910_1"
description: "shpc-registry automated BioContainers addition for bioconductor-sspa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sspa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sspa", "latest": {"2.30.0--r40hd029910_1": "sha256:9c4545220a5dfc2be96b8c523e902f4099d78b8cb4c3da011381fc3d5fe6af8f"}, "tags": {"2.30.0--r40hd029910_1": "sha256:9c4545220a5dfc2be96b8c523e902f4099d78b8cb4c3da011381fc3d5fe6af8f"}, "docker": "quay.io/biocontainers/bioconductor-sspa", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sspa.
shpc-registry automated BioContainers addition for bioconductor-sspa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sspa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sspa:2.30.0--r40hd029910_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sspa/2.30.0--r40hd029910_1
$ module help quay.io/biocontainers/bioconductor-sspa/2.30.0--r40hd029910_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sspa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sspa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sspa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sspa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sspa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sspa-inspect-deffile:

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