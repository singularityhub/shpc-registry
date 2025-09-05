---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu19ksubc.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu19ksubc.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu19ksubc.db/container.yaml"
updated_at: "2025-09-05 03:13:41.943995"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mu19ksubc.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mu19ksubc.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu19ksubc.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu19ksubc.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:c434900d68d8256688578cb89c153849fe15ecc3fee44a6eaa7acf4c6bc930ff"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:b7bbe5d0b8c83578947fff283c9335c5a1ffd2d37c422f8a6b087441a7cede00", "3.13.0--r42hdfd78af_2": "sha256:95cf69a2cadea5e957464d066da4deb8d63a059b3f00722940d9268b7e1b691c", "3.13.0--r43hdfd78af_3": "sha256:6762367f937e6a6d8d6981dce1d48bc0dd8345e837c2a8ac18c34d97a2fc6c71", "3.13.0--r43hdfd78af_4": "sha256:8dfc09774244aac7c5c287a5f6fdbd69a533327b6a0fd8f24effb669a67050c4", "3.13.0--r44hdfd78af_5": "sha256:c434900d68d8256688578cb89c153849fe15ecc3fee44a6eaa7acf4c6bc930ff"}, "docker": "quay.io/biocontainers/bioconductor-mu19ksubc.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu19ksubc.db.
shpc-registry automated BioContainers addition for bioconductor-mu19ksubc.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubc.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubc.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu19ksubc.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mu19ksubc.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu19ksubc.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubc.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubc.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu19ksubc.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu19ksubc.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu19ksubc.db-inspect-deffile:

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