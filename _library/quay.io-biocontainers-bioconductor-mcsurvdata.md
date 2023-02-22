---
layout: container
name:  "quay.io/biocontainers/bioconductor-mcsurvdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mcsurvdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mcsurvdata/container.yaml"
updated_at: "2023-02-22 02:56:48.197114"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mcsurvdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mcsurvdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mcsurvdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mcsurvdata", "latest": {"1.16.0--r42hdfd78af_0": "sha256:9fbcd220ac784c3cfe984c332c848c439b14a8f0753ffeb5a44d66adab4d7b5f"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:b7d29cae7158e28fc11956e4b1fc3e6bf778c6d4b2015726f3ca40937b25fd9c", "1.16.0--r42hdfd78af_0": "sha256:9fbcd220ac784c3cfe984c332c848c439b14a8f0753ffeb5a44d66adab4d7b5f", "1.12.0--r41hdfd78af_1": "sha256:2c3ac0097216d2cce03efee51b0e9dd82d74846941c6b22296a64592cf443580", "1.10.0--r41hdfd78af_0": "sha256:ebf67a579c7ba9665c6c0d1e68326db522eb90ec635ebbf37b70425b5204a106"}, "docker": "quay.io/biocontainers/bioconductor-mcsurvdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mcsurvdata.
shpc-registry automated BioContainers addition for bioconductor-mcsurvdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mcsurvdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mcsurvdata:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mcsurvdata/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mcsurvdata/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mcsurvdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcsurvdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcsurvdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mcsurvdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mcsurvdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mcsurvdata-inspect-deffile:

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