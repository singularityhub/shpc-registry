---
layout: container
name:  "quay.io/biocontainers/bioconductor-shinymethyldata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-shinymethyldata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-shinymethyldata/container.yaml"
updated_at: "2024-12-09 03:37:29.823125"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-shinymethyldata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-shinymethyldata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-shinymethyldata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-shinymethyldata", "latest": {"1.22.0--r43hdfd78af_0": "sha256:267e4e851f10022556b91e050af6b5327fa40913fd3b18e4cce350ab7d9955cb"}, "tags": {"1.9.0--r40_0": "sha256:01635ba91ffa3b891fdadde837242c16b228c6badb6a4779d8cb56f1a0713546", "1.17.0--r42hdfd78af_0": "sha256:a7cd0c2802c81bd058df9643601358ad2bc2db0c77e3a327c7ee35108f4bf69c", "1.14.0--r41hdfd78af_1": "sha256:af532433984b084bfd9ce37287c3d3a20f4ca8680c24330827088ee07788d1d8", "1.12.0--r41hdfd78af_0": "sha256:26f3d0ec99aacf852fd91e79013087fccd56b0e1b3170d3d78331f036d330eee", "1.10.0--r40hdfd78af_1": "sha256:8f6ca95efdb1782de6f6456bd73f8b38f1ebbfcdb6df965ec6ef0dbb03875e55", "1.20.0--r43hdfd78af_0": "sha256:7d4590fcf16e4aaea824dc321d4bc94e07e67c885ef6f0ed6d7568a614e7fdb6", "1.22.0--r43hdfd78af_0": "sha256:267e4e851f10022556b91e050af6b5327fa40913fd3b18e4cce350ab7d9955cb"}, "docker": "quay.io/biocontainers/bioconductor-shinymethyldata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-shinymethyldata.
shpc-registry automated BioContainers addition for bioconductor-shinymethyldata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyldata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-shinymethyldata:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-shinymethyldata/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-shinymethyldata/1.22.0--r43hdfd78af_0
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