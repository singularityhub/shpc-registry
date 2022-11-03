---
layout: container
name:  "quay.io/biocontainers/bioconductor-chicken.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chicken.db/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chicken.db/container.yaml"
updated_at: "2022-11-03 00:45:20.728541"
latest: "3.2.3--r41hdfd78af_7"
container_url: "https://biocontainers.pro/tools/bioconductor-chicken.db"
aliases:
 - ".bioconductor-chicken.db-post-link.sh"
 - ".bioconductor-chicken.db-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
description: "shpc-registry automated BioContainers addition for bioconductor-chicken.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chicken.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chicken.db", "latest": {"3.2.3--r41hdfd78af_7": "sha256:c840d58d94e0fbef77f5473beba5b0bd8221402d4b0f32526d5c754d5af6611c"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:c840d58d94e0fbef77f5473beba5b0bd8221402d4b0f32526d5c754d5af6611c"}, "docker": "quay.io/biocontainers/bioconductor-chicken.db", "aliases": {".bioconductor-chicken.db-post-link.sh": "/usr/local/bin/.bioconductor-chicken.db-post-link.sh", ".bioconductor-chicken.db-pre-unlink.sh": "/usr/local/bin/.bioconductor-chicken.db-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chicken.db.
shpc-registry automated BioContainers addition for bioconductor-chicken.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chicken.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chicken.db:3.2.3--r41hdfd78af_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chicken.db/3.2.3--r41hdfd78af_7
$ module help quay.io/biocontainers/bioconductor-chicken.db/3.2.3--r41hdfd78af_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chicken.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicken.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chicken.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chicken.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chicken.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chicken.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-chicken.db-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-chicken.db-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-chicken.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-chicken.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-chicken.db-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-chicken.db-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-chicken.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-chicken.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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