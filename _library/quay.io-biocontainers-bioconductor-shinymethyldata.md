---
layout: container
name:  "quay.io/biocontainers/bioconductor-shinymethyldata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shinymethyldata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shinymethyldata/container.yaml"
updated_at: "2022-11-03 01:06:17.878136"
latest: "1.9.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shinymethyldata"
aliases:
 - ".bioconductor-shinymethyldata-post-link.sh"
 - ".bioconductor-shinymethyldata-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shinymethyldata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shinymethyldata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shinymethyldata", "latest": {"1.9.0--r40_0": "sha256:01635ba91ffa3b891fdadde837242c16b228c6badb6a4779d8cb56f1a0713546"}, "tags": {"1.9.0--r40_0": "sha256:01635ba91ffa3b891fdadde837242c16b228c6badb6a4779d8cb56f1a0713546"}, "docker": "quay.io/biocontainers/bioconductor-shinymethyldata", "aliases": {".bioconductor-shinymethyldata-post-link.sh": "/usr/local/bin/.bioconductor-shinymethyldata-post-link.sh", ".bioconductor-shinymethyldata-pre-unlink.sh": "/usr/local/bin/.bioconductor-shinymethyldata-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shinymethyldata.
shpc-registry automated BioContainers addition for bioconductor-shinymethyldata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyldata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyldata:1.9.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shinymethyldata/1.9.0--r40_0
$ module help quay.io/biocontainers/bioconductor-shinymethyldata/1.9.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-shinymethyldata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinymethyldata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-shinymethyldata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-shinymethyldata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-shinymethyldata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-shinymethyldata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-shinymethyldata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-shinymethyldata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-shinymethyldata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-shinymethyldata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-shinymethyldata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-shinymethyldata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-shinymethyldata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-shinymethyldata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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