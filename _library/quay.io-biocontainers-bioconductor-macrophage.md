---
layout: container
name:  "quay.io/biocontainers/bioconductor-macrophage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-macrophage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-macrophage/container.yaml"
updated_at: "2025-09-11 03:18:19.123512"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-macrophage"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-macrophage"
config: {"url": "https://biocontainers.pro/tools/bioconductor-macrophage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-macrophage", "latest": {"1.22.0--r44hdfd78af_0": "sha256:67c6611863aab694446bb1b553c202a3940916995f525e30dff03ddba958a524"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a65aecdc5484813a54475e62750831432c13aba622d608333d95798319befa0f", "1.13.0--r42hdfd78af_0": "sha256:f991763e25f246959946fd1812d60812eeb838bdf2d66d14fc6b1a6a85140556", "1.10.0--r41hdfd78af_1": "sha256:3c512f0d69491bd4ffc78af5ed8f27e4f900e993c5f4c3454e8f112a236d02af", "1.16.0--r43hdfd78af_0": "sha256:ab0288160e22fe565850e311416add7e2079f27f30674339a6b3a11e2350cf19", "1.18.0--r43hdfd78af_0": "sha256:4234a6e571c1226b54c7b3eea7f7d8eeaf713d614454099237e9baef052950f3", "1.22.0--r44hdfd78af_0": "sha256:67c6611863aab694446bb1b553c202a3940916995f525e30dff03ddba958a524"}, "docker": "quay.io/biocontainers/bioconductor-macrophage", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-macrophage.
shpc-registry automated BioContainers addition for bioconductor-macrophage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-macrophage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-macrophage:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-macrophage/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-macrophage/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-macrophage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macrophage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macrophage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-macrophage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-macrophage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-macrophage-inspect-deffile:

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