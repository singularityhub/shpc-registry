---
layout: container
name:  "quay.io/biocontainers/bioconductor-rmir.hs.mirna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rmir.hs.mirna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rmir.hs.mirna/container.yaml"
updated_at: "2023-11-19 02:53:06.825922"
latest: "1.0.7--r43hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-rmir.hs.mirna"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.7--r40hdfd78af_9"
 - "1.0.7--r42hdfd78af_13"
 - "1.0.7--r43hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-rmir.hs.mirna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rmir.hs.mirna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rmir.hs.mirna", "latest": {"1.0.7--r43hdfd78af_14": "sha256:98231d3b3568a30a8a9fd7938904798c0581c14f601aa2418e97e13bc67140fa"}, "tags": {"1.0.7--r40hdfd78af_9": "sha256:2bbe6ed82988ba723d5510c092a7e729223c3cb844d28b7b3436f8bd7911e3f9", "1.0.7--r42hdfd78af_13": "sha256:508f1c65684f92cc128306a9b877186a57aa02d152bc4bb05b5fbc91b6bdf0d0", "1.0.7--r43hdfd78af_14": "sha256:98231d3b3568a30a8a9fd7938904798c0581c14f601aa2418e97e13bc67140fa"}, "docker": "quay.io/biocontainers/bioconductor-rmir.hs.mirna", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rmir.hs.mirna.
shpc-registry automated BioContainers addition for bioconductor-rmir.hs.mirna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rmir.hs.mirna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rmir.hs.mirna:1.0.7--r43hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rmir.hs.mirna/1.0.7--r43hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-rmir.hs.mirna/1.0.7--r43hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rmir.hs.mirna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmir.hs.mirna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmir.hs.mirna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rmir.hs.mirna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rmir.hs.mirna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rmir.hs.mirna-inspect-deffile:

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