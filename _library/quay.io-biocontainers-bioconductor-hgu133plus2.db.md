---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133plus2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133plus2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133plus2.db/container.yaml"
updated_at: "2024-02-15 03:53:59.363431"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133plus2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r40_9"
 - "3.13.0--r42hdfd78af_2"
 - "3.2.3--r41hdfd78af_11"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133plus2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:222353bb8e1b6d6a8a7b220f311deca8ca98b3a72733987769b7c1a9ffb3bbe7"}, "tags": {"3.2.3--r40_9": "sha256:c1894e61572e364e5c1ceceff6736f1c329d1018c58dca2906d9b8da4a538006", "3.13.0--r42hdfd78af_2": "sha256:8c9fe46f9fc7bbd76ba550844a233991ad78282a188049a76f8486304a438ce5", "3.2.3--r41hdfd78af_11": "sha256:56f2529acb2eb1a47fe644f0cc775b148362c2b7532ba9b10e922389a40279e1", "3.13.0--r43hdfd78af_3": "sha256:fea81f45b697264f8ce8e605999ffc2e8899e48693c7d04b3b7c02d7b648bb1e", "3.13.0--r43hdfd78af_4": "sha256:222353bb8e1b6d6a8a7b220f311deca8ca98b3a72733987769b7c1a9ffb3bbe7"}, "docker": "quay.io/biocontainers/bioconductor-hgu133plus2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133plus2.db.
shpc-registry automated BioContainers addition for bioconductor-hgu133plus2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133plus2.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hgu133plus2.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133plus2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133plus2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133plus2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133plus2.db-inspect-deffile:

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