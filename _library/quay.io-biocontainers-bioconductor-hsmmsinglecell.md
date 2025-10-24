---
layout: container
name:  "quay.io/biocontainers/bioconductor-hsmmsinglecell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hsmmsinglecell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hsmmsinglecell/container.yaml"
updated_at: "2025-10-24 03:25:26.958619"
latest: "1.26.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hsmmsinglecell"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.26.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hsmmsinglecell"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hsmmsinglecell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hsmmsinglecell", "latest": {"1.26.0--r44hdfd78af_0": "sha256:26b932ee91a3502483b82a4459275ffbaa74e54213d0a0739747d8ee74f62086"}, "tags": {"1.9.0--r40_0": "sha256:ed515829a87c14b2cbf9cbdf63b4d07596e1321b92b09bf98625cbb76d733120", "1.18.0--r42hdfd78af_0": "sha256:eadfa18832fe3929440e7ba08e94b610a227ade3c488522fd59ec3c0522dcb85", "1.17.0--r42hdfd78af_0": "sha256:749245706196611fad6c38d0920e88fff0310089a309f5ff725cecfaa6bcbfb5", "1.14.0--r41hdfd78af_1": "sha256:16abc1c80db635e58b9b8194e4a9b72e517db212b713da2bb31f98cd165419d9", "1.12.0--r41hdfd78af_0": "sha256:593f52e974232f022d41ae832dd80a68d6cf785c047baf662fceb4991551cbd4", "1.10.0--r40hdfd78af_1": "sha256:54ae2532b3ab07015e512019ba12ea839d5511f479a52b88f3e9499c03dcef3e", "1.20.0--r43hdfd78af_0": "sha256:332d6a06301172680bdd1fb840acd6f965dc58d05887b76a07758f2f963318cc", "1.22.0--r43hdfd78af_0": "sha256:4e2d7d12726bb2bbc783a33b5b7cd7de81eda9e0a9becb84079c107d0169ec77", "1.26.0--r44hdfd78af_0": "sha256:26b932ee91a3502483b82a4459275ffbaa74e54213d0a0739747d8ee74f62086"}, "docker": "quay.io/biocontainers/bioconductor-hsmmsinglecell", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hsmmsinglecell.
shpc-registry automated BioContainers addition for bioconductor-hsmmsinglecell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hsmmsinglecell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hsmmsinglecell:1.26.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hsmmsinglecell/1.26.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hsmmsinglecell/1.26.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hsmmsinglecell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hsmmsinglecell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hsmmsinglecell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hsmmsinglecell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hsmmsinglecell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hsmmsinglecell-inspect-deffile:

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