---
layout: container
name:  "quay.io/biocontainers/bioconductor-nestlink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nestlink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nestlink/container.yaml"
updated_at: "2024-05-27 03:14:12.609938"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nestlink"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nestlink"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nestlink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nestlink", "latest": {"1.18.0--r43hdfd78af_0": "sha256:c573b0918bc222338f81eb477fe9316748dc5b59e55db9a138e9875c35570c2e"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:2cfa15a73d82a9c7221fb3a5639c249f35befdab4ccc81d8f9a08aec04826093", "1.10.0--r41hdfd78af_1": "sha256:69db6e6a2cdc4651683c2988ac0cba688db3f962ffe8d4de81ec74084158beee", "1.14.0--r42hdfd78af_0": "sha256:25138e51996f1fba81050ebf798ef56721739709b3e6b922cea33275cf9949cc", "1.16.0--r43hdfd78af_0": "sha256:2c390ffb720c9504dd6c2bdf6f419a1e34e2688e883e80b73d6ceb454851718e", "1.18.0--r43hdfd78af_0": "sha256:c573b0918bc222338f81eb477fe9316748dc5b59e55db9a138e9875c35570c2e"}, "docker": "quay.io/biocontainers/bioconductor-nestlink", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nestlink.
shpc-registry automated BioContainers addition for bioconductor-nestlink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nestlink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nestlink:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nestlink/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nestlink/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nestlink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nestlink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nestlink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nestlink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nestlink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nestlink-inspect-deffile:

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