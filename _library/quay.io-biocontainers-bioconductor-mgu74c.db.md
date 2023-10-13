---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74c.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74c.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74c.db/container.yaml"
updated_at: "2023-10-13 03:05:35.848353"
latest: "3.13.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74c.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74c.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74c.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74c.db", "latest": {"3.13.0--r43hdfd78af_3": "sha256:b57c03a9b5cc5c9dd59017d3b7ea992198ea27706b43aedf7d15952ea4861351"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:44cc5a6996889dc5b8f7fc11f937adb6092a808a8d6b7613eaa5017560e2d037", "3.13.0--r42hdfd78af_2": "sha256:89c27e4c51f4815599ccb7cd6612806e95a6dd28141d326cc7b7bee7141900c1", "3.13.0--r43hdfd78af_3": "sha256:b57c03a9b5cc5c9dd59017d3b7ea992198ea27706b43aedf7d15952ea4861351"}, "docker": "quay.io/biocontainers/bioconductor-mgu74c.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74c.db.
shpc-registry automated BioContainers addition for bioconductor-mgu74c.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74c.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74c.db:3.13.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74c.db/3.13.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-mgu74c.db/3.13.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74c.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74c.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74c.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74c.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74c.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74c.db-inspect-deffile:

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