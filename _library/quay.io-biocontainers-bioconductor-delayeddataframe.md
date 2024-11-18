---
layout: container
name:  "quay.io/biocontainers/bioconductor-delayeddataframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-delayeddataframe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-delayeddataframe/container.yaml"
updated_at: "2024-11-18 16:37:08.494111"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-delayeddataframe"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-delayeddataframe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-delayeddataframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-delayeddataframe", "latest": {"1.18.0--r43hdfd78af_0": "sha256:bb2e0ed4c061bfa446501b7005e73d6d5fe9c83f71138ea0c82dd7396ec66fc2"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:1feb6dfb953239ade388b0787cd000360f795df81bd72e7f31a009de90a07a9a", "1.14.0--r42hdfd78af_0": "sha256:96ca2e59b130fbb114cce2cabdb37ffc8d2a176874175607b981ca0d7289956a", "1.10.0--r41hdfd78af_0": "sha256:e186bf0fd0ce81ad77568c88234c315805b43bc076940bad15ace3dd3950479f", "1.16.0--r43hdfd78af_0": "sha256:61da891bc80dc3feec667b31f99e2ad1bc13fc7227cce1021cf1daa724c05679", "1.18.0--r43hdfd78af_0": "sha256:bb2e0ed4c061bfa446501b7005e73d6d5fe9c83f71138ea0c82dd7396ec66fc2"}, "docker": "quay.io/biocontainers/bioconductor-delayeddataframe", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-delayeddataframe.
shpc-registry automated BioContainers addition for bioconductor-delayeddataframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-delayeddataframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-delayeddataframe:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-delayeddataframe/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-delayeddataframe/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-delayeddataframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayeddataframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayeddataframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-delayeddataframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-delayeddataframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-delayeddataframe-inspect-deffile:

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