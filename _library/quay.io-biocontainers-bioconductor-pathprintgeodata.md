---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathprintgeodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathprintgeodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathprintgeodata/container.yaml"
updated_at: "2025-09-01 04:08:53.844847"
latest: "1.20.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-pathprintgeodata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.20.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-pathprintgeodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathprintgeodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathprintgeodata", "latest": {"1.20.0--r40hdfd78af_1": "sha256:5d978a3330421f01c1a68c96ce0895eae6f05fe2dac51ef88963191f5a96918b"}, "tags": {"1.20.0--r40hdfd78af_1": "sha256:5d978a3330421f01c1a68c96ce0895eae6f05fe2dac51ef88963191f5a96918b"}, "docker": "quay.io/biocontainers/bioconductor-pathprintgeodata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathprintgeodata.
shpc-registry automated BioContainers addition for bioconductor-pathprintgeodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathprintgeodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathprintgeodata:1.20.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathprintgeodata/1.20.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-pathprintgeodata/1.20.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathprintgeodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathprintgeodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathprintgeodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathprintgeodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathprintgeodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathprintgeodata-inspect-deffile:

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