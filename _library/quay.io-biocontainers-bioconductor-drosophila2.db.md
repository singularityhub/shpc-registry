---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosophila2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosophila2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosophila2.db/container.yaml"
updated_at: "2025-04-17 04:38:23.285208"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-drosophila2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-drosophila2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosophila2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosophila2.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:fa99c9cfaeeb11560b3abdf2524f5c8cf97d8e65d32bbd917c55c61de4dfaf3a"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:ee2b03083bfe42279c61e0d6ab55e699f16a8e25fb79289a011084425c96df1b", "3.13.0--r42hdfd78af_2": "sha256:790148654f1f79b44ddd46bdd5fe97dbf8b624c529d186a23678b791ecabedda", "3.13.0--r43hdfd78af_4": "sha256:bcc4588dea30f88ff5731481e695005394c767283ea3d779122dbcdb5a533818", "3.13.0--r44hdfd78af_5": "sha256:fa99c9cfaeeb11560b3abdf2524f5c8cf97d8e65d32bbd917c55c61de4dfaf3a"}, "docker": "quay.io/biocontainers/bioconductor-drosophila2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosophila2.db.
shpc-registry automated BioContainers addition for bioconductor-drosophila2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosophila2.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-drosophila2.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosophila2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosophila2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosophila2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosophila2.db-inspect-deffile:

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