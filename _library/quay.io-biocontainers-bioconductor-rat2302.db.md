---
layout: container
name:  "quay.io/biocontainers/bioconductor-rat2302.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rat2302.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rat2302.db/container.yaml"
updated_at: "2025-10-21 03:36:58.778820"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-rat2302.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-rat2302.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rat2302.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rat2302.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:c6ac14cad662e67616971b2a2342137af15e1e84be1fd5651066b000be7230e4"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:8b335980b08ed8328f55e42a4493ebb096666316166385fa0e73d3b47b81f419", "3.13.0--r42hdfd78af_2": "sha256:382c96f449bf5b9c3c2566d381cc53053c995f9366082fcc52f1c541c651e104", "3.13.0--r43hdfd78af_3": "sha256:dca4dc63bb42b8c752f213e74bd2af971f4b4c467babd7469ba1cbb29a85733e", "3.13.0--r43hdfd78af_4": "sha256:d8615a396d7da7ffa64130300c4cf8d8a379155356ecbdb3a09cfa9a364f9142", "3.13.0--r44hdfd78af_5": "sha256:c6ac14cad662e67616971b2a2342137af15e1e84be1fd5651066b000be7230e4"}, "docker": "quay.io/biocontainers/bioconductor-rat2302.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rat2302.db.
shpc-registry automated BioContainers addition for bioconductor-rat2302.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rat2302.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rat2302.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-rat2302.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rat2302.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rat2302.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rat2302.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rat2302.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rat2302.db-inspect-deffile:

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