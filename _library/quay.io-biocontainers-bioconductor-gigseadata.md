---
layout: container
name:  "quay.io/biocontainers/bioconductor-gigseadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gigseadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gigseadata/container.yaml"
updated_at: "2024-12-28 03:05:45.445599"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gigseadata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gigseadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gigseadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gigseadata", "latest": {"1.24.0--r44hdfd78af_0": "sha256:1f379367d894f5b27579ce089084c179ae4aa72b0fb2927782ff02717a913f9b"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:5dddcf66426e1422a288fb09ac6a489607426b6aa68231b5fa716c7c9fe373fd", "1.15.0--r42hdfd78af_0": "sha256:8a632c9eebd92cb40e5f84f46c77d432ec29855115c348a806c78ff6d132095a", "1.12.0--r41hdfd78af_1": "sha256:d8a01be4d036696a50346776b02608b2691c9a07e9b8d1585c97faf1e0207c62", "1.10.0--r41hdfd78af_0": "sha256:39d9b2da1b01e35a043327bf27a1de76f15de893d20001b43ccdadfbc4942282", "1.18.0--r43hdfd78af_0": "sha256:5b1e0487c32042478db434947cf0d3a5c931770926b8539a227d3df7dbb25878", "1.20.0--r43hdfd78af_0": "sha256:f0367ea5b13e519d9b44d9b33edf44bd4cc9e9e56beb98c5bd898cd377899db0", "1.24.0--r44hdfd78af_0": "sha256:1f379367d894f5b27579ce089084c179ae4aa72b0fb2927782ff02717a913f9b"}, "docker": "quay.io/biocontainers/bioconductor-gigseadata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gigseadata.
shpc-registry automated BioContainers addition for bioconductor-gigseadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gigseadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gigseadata:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gigseadata/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gigseadata/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gigseadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gigseadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gigseadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gigseadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gigseadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gigseadata-inspect-deffile:

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