---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19/container.yaml"
updated_at: "2025-02-20 03:38:34.364986"
latest: "1.12.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgawgbsdata.hg19"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgawgbsdata.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgawgbsdata.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgawgbsdata.hg19", "latest": {"1.12.0--r41hdfd78af_1": "sha256:7b908be7771fa4bba796f3a18014c672025710e70fffdd022c96ff70e622da2a"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:2c202a09d1ddba8190dc457cdcb27a88c07da16eb190a37e387f686ef105949c", "1.12.0--r41hdfd78af_1": "sha256:7b908be7771fa4bba796f3a18014c672025710e70fffdd022c96ff70e622da2a", "1.10.0--r41hdfd78af_0": "sha256:7af0f1e1d40b523188733be3e310b3673083ad70637b8e8e631f16963f46ec9f"}, "docker": "quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19.
shpc-registry automated BioContainers addition for bioconductor-tcgawgbsdata.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19:1.12.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19/1.12.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-tcgawgbsdata.hg19/1.12.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgawgbsdata.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgawgbsdata.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgawgbsdata.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgawgbsdata.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgawgbsdata.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgawgbsdata.hg19-inspect-deffile:

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