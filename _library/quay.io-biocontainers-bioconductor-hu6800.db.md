---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu6800.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu6800.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu6800.db/container.yaml"
updated_at: "2024-01-28 02:37:01.495749"
latest: "3.13.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-hu6800.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-hu6800.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu6800.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu6800.db", "latest": {"3.13.0--r43hdfd78af_3": "sha256:af8a67c83d8d23e1a701fbbf2c262fe52364dad9dba94f75473b9cbb12dd5298"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:9404631d76a36484c3246f3451869449b1a1c2d224e1f1539ff85fa90466dc6c", "3.13.0--r41hdfd78af_1": "sha256:7d6685d82e39e4e3b985d8b17556878b9addfacf2e24327147e56c31fde17137", "3.13.0--r42hdfd78af_2": "sha256:0962c0c15f557b146f62f303c4922ca86a266c7b1ba0d406154c003433c643b6", "3.13.0--r43hdfd78af_3": "sha256:af8a67c83d8d23e1a701fbbf2c262fe52364dad9dba94f75473b9cbb12dd5298"}, "docker": "quay.io/biocontainers/bioconductor-hu6800.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu6800.db.
shpc-registry automated BioContainers addition for bioconductor-hu6800.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800.db:3.13.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu6800.db/3.13.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-hu6800.db/3.13.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu6800.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu6800.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu6800.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu6800.db-inspect-deffile:

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