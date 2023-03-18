---
layout: container
name:  "quay.io/biocontainers/bioconductor-do.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-do.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-do.db/container.yaml"
updated_at: "2023-03-18 03:02:05.360717"
latest: "2.9--r42hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-do.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.9--r40_9"
 - "2.9--r41hdfd78af_13"
 - "2.9--r42hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-do.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-do.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-do.db", "latest": {"2.9--r42hdfd78af_14": "sha256:9e4cc60ca7c0f47c84ff2490d1bfd5dc7eaa2d90a01bc2808f51f71a68b8e6bc"}, "tags": {"2.9--r40_9": "sha256:b014006c35272c7680c1ca330c68c63b3efab10650047aaa4bba5ce8f841bfe5", "2.9--r41hdfd78af_13": "sha256:74c497703db0123cf4248a511004ff5a0973ec66539a2988e457c92492b51aad", "2.9--r42hdfd78af_14": "sha256:9e4cc60ca7c0f47c84ff2490d1bfd5dc7eaa2d90a01bc2808f51f71a68b8e6bc"}, "docker": "quay.io/biocontainers/bioconductor-do.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-do.db.
shpc-registry automated BioContainers addition for bioconductor-do.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-do.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-do.db:2.9--r42hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-do.db/2.9--r42hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-do.db/2.9--r42hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-do.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-do.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-do.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-do.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-do.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-do.db-inspect-deffile:

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