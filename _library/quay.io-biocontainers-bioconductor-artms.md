---
layout: container
name:  "quay.io/biocontainers/bioconductor-artms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-artms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-artms/container.yaml"
updated_at: "2023-10-06 03:04:21.141034"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-artms"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.2--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-artms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-artms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-artms", "latest": {"1.18.0--r43hdfd78af_0": "sha256:4f0b398190f474a8086294ca96d149ac80339348cc2e560709ed755ded3cb737"}, "tags": {"1.8.2--r40hdfd78af_0": "sha256:d6cff4fbd7188d879402d6a2f7f73c15c4a6ee5accc37679cd56e499978db60a", "1.16.0--r42hdfd78af_0": "sha256:6da8f5e3d865d6607265844fb1826f1d52d2bcd57ba78591433851241c795b71", "1.12.0--r41hdfd78af_0": "sha256:775fe2bc48e253807c1db3d782573cc3a09a862646d0200f6673280944ded1b3", "1.10.0--r41hdfd78af_0": "sha256:beabbce71137b457245cac9799f3d6ea1b22dc46670ab9c8bf9054a7b3122771", "1.18.0--r43hdfd78af_0": "sha256:4f0b398190f474a8086294ca96d149ac80339348cc2e560709ed755ded3cb737"}, "docker": "quay.io/biocontainers/bioconductor-artms", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-artms.
shpc-registry automated BioContainers addition for bioconductor-artms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-artms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-artms:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-artms/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-artms/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-artms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-artms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-artms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-artms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-artms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-artms-inspect-deffile:

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