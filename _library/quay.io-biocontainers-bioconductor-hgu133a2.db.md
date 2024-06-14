---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133a2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133a2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133a2.db/container.yaml"
updated_at: "2024-06-14 02:43:51.801842"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133a2.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r40hdfd78af_9"
 - "3.13.0--r42hdfd78af_2"
 - "3.2.3--r41hdfd78af_10"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133a2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133a2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133a2.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:929de35785781cf83e6da15e27746807b23d04b62732235212ce6c7bc95ff842"}, "tags": {"3.2.3--r40hdfd78af_9": "sha256:695a1566fa2c1c1b691d4b707b1b694a7fee10b59e0b90108f4d81807a6af820", "3.13.0--r42hdfd78af_2": "sha256:16f4d44514051a29fdf612b9651ae5b3fcd25ec7cfa5b60a7fb8b67343370aee", "3.2.3--r41hdfd78af_10": "sha256:b019d876a1a9f6bb77551937610997c6919d3da78b35a94ac4031ef87ba240a3", "3.13.0--r43hdfd78af_3": "sha256:7ad6145932abcdfacb103baa6ffe24ec4aa3a4e4ec200d1505bcc11d446242d9", "3.13.0--r43hdfd78af_4": "sha256:929de35785781cf83e6da15e27746807b23d04b62732235212ce6c7bc95ff842"}, "docker": "quay.io/biocontainers/bioconductor-hgu133a2.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133a2.db.
shpc-registry automated BioContainers addition for bioconductor-hgu133a2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133a2.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hgu133a2.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133a2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133a2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133a2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133a2.db-inspect-deffile:

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