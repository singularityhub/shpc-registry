---
layout: container
name:  "quay.io/biocontainers/bioconductor-xina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xina/container.yaml"
updated_at: "2024-01-24 02:45:06.316506"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xina"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xina"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xina", "latest": {"1.20.0--r43hdfd78af_0": "sha256:ef24bbf8d5a13e30f483d49b3e09e0bbef6e568f74ef00b5e6f124c1ee1013a5"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:9803f0d47ab8e00723b69666edc245290ab9413dd0d65264b88f02072dbb2ce6", "1.16.0--r42hdfd78af_0": "sha256:e897bee45671cbcdd3a8578db9a51a693b179f97a55df4848579016a67f94e79", "1.12.0--r41hdfd78af_0": "sha256:fc662f1d874e40ddf90bcf9e91e90abfea85a079c3aab4d6d0529d934eec11ec", "1.10.0--r41hdfd78af_0": "sha256:75460d1aa403fdbc398008293322de447bdb08bfb2b25281690ef8a82553ca7e", "1.18.0--r43hdfd78af_0": "sha256:7c774658827b01f0b9f319cdb3fdb658cc974633a8dd56f2edba099a6157c5b5", "1.20.0--r43hdfd78af_0": "sha256:ef24bbf8d5a13e30f483d49b3e09e0bbef6e568f74ef00b5e6f124c1ee1013a5"}, "docker": "quay.io/biocontainers/bioconductor-xina", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xina.
shpc-registry automated BioContainers addition for bioconductor-xina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xina:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xina/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xina/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xina-inspect-deffile:

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