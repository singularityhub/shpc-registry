---
layout: container
name:  "quay.io/biocontainers/bioconductor-tenxpbmcdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tenxpbmcdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tenxpbmcdata/container.yaml"
updated_at: "2024-07-27 03:03:31.158264"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tenxpbmcdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tenxpbmcdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tenxpbmcdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tenxpbmcdata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:4da4bcefca36f2f9111dabd55ad96370a0a00369112375d769e55a8604409080"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:f804ba7a7e2151819db3a885abbc2210ae8d038614e2a8c12941f1ad5cb6ee84", "1.16.0--r42hdfd78af_0": "sha256:bfffc505bbbde10e571d459d5514c679d08aa5260174e5f4f2aed27f77f96a3d", "1.12.0--r41hdfd78af_1": "sha256:2f9903ed8d926d873b4d0f4c8865a6b8deba3676d3b690d8c94a4f6b0f3dbbc1", "1.10.0--r41hdfd78af_0": "sha256:215700089631d532c5063b0246e26e866794c4b8d65cefc6e0f1ab96ef50c936", "1.18.0--r43hdfd78af_0": "sha256:8f83e641371b71b9cebc8a9042c1a83be8238569c1706847d1904cb4476e7b5b", "1.20.0--r43hdfd78af_0": "sha256:4da4bcefca36f2f9111dabd55ad96370a0a00369112375d769e55a8604409080"}, "docker": "quay.io/biocontainers/bioconductor-tenxpbmcdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tenxpbmcdata.
shpc-registry automated BioContainers addition for bioconductor-tenxpbmcdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxpbmcdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tenxpbmcdata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tenxpbmcdata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tenxpbmcdata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tenxpbmcdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxpbmcdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tenxpbmcdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tenxpbmcdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tenxpbmcdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tenxpbmcdata-inspect-deffile:

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