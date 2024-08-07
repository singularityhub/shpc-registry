---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133b.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133b.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133b.db/container.yaml"
updated_at: "2024-08-07 02:51:24.084482"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133b.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133b.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133b.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133b.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:9fcd553291831a71e2f2e6a5f13a81821ce445d60f3ee684e152bc09df5f17a3"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:90373c1dde3f1175acd921c40129dd439ff474b89f3689fdad88dc73cd3f0df0", "3.13.0--r42hdfd78af_2": "sha256:725db20f7f25882fd1c70a20d2ca7841153e636720d416e5b1fc0dfb30d6e498", "3.13.0--r43hdfd78af_3": "sha256:a22be7fa10b22c7d8db04b7534f632ab0d030e31930881e46a55d6ccf1314572", "3.13.0--r43hdfd78af_4": "sha256:9fcd553291831a71e2f2e6a5f13a81821ce445d60f3ee684e152bc09df5f17a3"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133b.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133b.db.
shpc-registry automated BioContainers addition for bioconductor-hthgu133b.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133b.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133b.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133b.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hthgu133b.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133b.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133b.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133b.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133b.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133b.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133b.db-inspect-deffile:

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