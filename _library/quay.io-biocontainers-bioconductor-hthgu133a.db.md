---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133a.db/container.yaml"
updated_at: "2024-04-04 03:53:06.229092"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133a.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133a.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:edc9e57cbbb788b3e3f46eaf0869d62cfa99e4daa0ff06c1a82c556259ff228e"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:db2ea43944ee98c3f919c6a3f77c6804f5e519dd9c0cd7e0fb5064db2200c74e", "3.13.0--r42hdfd78af_2": "sha256:28d4d52405e1ae435cf3d35246e17749a5f18b59b5de9629efe9840844e0601b", "3.13.0--r43hdfd78af_3": "sha256:fa2cf130afe2792812f5ec8cd33d8eddd1c44ef5d1c03cfaad7950820b9c3823", "3.13.0--r43hdfd78af_4": "sha256:edc9e57cbbb788b3e3f46eaf0869d62cfa99e4daa0ff06c1a82c556259ff228e"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133a.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133a.db.
shpc-registry automated BioContainers addition for bioconductor-hthgu133a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133a.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133a.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hthgu133a.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133a.db-inspect-deffile:

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