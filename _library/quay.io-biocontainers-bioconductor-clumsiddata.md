---
layout: container
name:  "quay.io/biocontainers/bioconductor-clumsiddata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clumsiddata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clumsiddata/container.yaml"
updated_at: "2023-05-06 03:26:54.141648"
latest: "1.13.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clumsiddata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-clumsiddata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clumsiddata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clumsiddata", "latest": {"1.13.0--r42hdfd78af_0": "sha256:5d3869983f9b7575dfb8f23b2c596e8a0f25acb3677240676ac620814d6bb73a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:ac369c324b15ddc4226c3357422e34cd74c2a89cbf54f4f2a07586b3ae072de6", "1.13.0--r42hdfd78af_0": "sha256:5d3869983f9b7575dfb8f23b2c596e8a0f25acb3677240676ac620814d6bb73a", "1.10.0--r41hdfd78af_1": "sha256:17e44862d504158383aa63c414edf3a36e97e2235503825271cac1200633dfd3"}, "docker": "quay.io/biocontainers/bioconductor-clumsiddata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clumsiddata.
shpc-registry automated BioContainers addition for bioconductor-clumsiddata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clumsiddata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clumsiddata:1.13.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clumsiddata/1.13.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clumsiddata/1.13.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clumsiddata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clumsiddata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clumsiddata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clumsiddata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clumsiddata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clumsiddata-inspect-deffile:

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