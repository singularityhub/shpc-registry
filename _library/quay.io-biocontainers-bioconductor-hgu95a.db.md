---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95a.db/container.yaml"
updated_at: "2026-01-26 05:03:40.354271"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95a.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95a.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:8755efcf1de093941850ab7b76cac182db2872b75586740f0417636cab8f3161"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:0f412eae423e8e32584f90d581ae45e9d8e6a717730f92e351a3c2bce254be69", "3.13.0--r42hdfd78af_2": "sha256:adc5ccb9fb8131e9169cf38365e26a00644acfa16f1d0d0cb51969cc89a42a98", "3.13.0--r43hdfd78af_3": "sha256:fbb64b406daa88b6b7efc14ffc13a12a83de6ba033d209357c52f78915b6e0d5", "3.13.0--r43hdfd78af_4": "sha256:1ca0a72fa3ab34a8cb09cdb304e9ec8179cfd2b65a256887790fc416dbde1a33", "3.13.0--r44hdfd78af_5": "sha256:8755efcf1de093941850ab7b76cac182db2872b75586740f0417636cab8f3161"}, "docker": "quay.io/biocontainers/bioconductor-hgu95a.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95a.db.
shpc-registry automated BioContainers addition for bioconductor-hgu95a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95a.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95a.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-hgu95a.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95a.db-inspect-deffile:

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