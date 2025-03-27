---
layout: container
name:  "quay.io/biocontainers/bioconductor-lrbase.gga.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lrbase.gga.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lrbase.gga.eg.db/container.yaml"
updated_at: "2025-03-27 03:30:50.083008"
latest: "2.0.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lrbase.gga.eg.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.0.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lrbase.gga.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lrbase.gga.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lrbase.gga.eg.db", "latest": {"2.0.0--r41hdfd78af_0": "sha256:a209f4bf68937660b628f9af3427e17cb8194b3d7725cee8b2c7c8e94cbfacf0"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:a209f4bf68937660b628f9af3427e17cb8194b3d7725cee8b2c7c8e94cbfacf0"}, "docker": "quay.io/biocontainers/bioconductor-lrbase.gga.eg.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lrbase.gga.eg.db.
shpc-registry automated BioContainers addition for bioconductor-lrbase.gga.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbase.gga.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbase.gga.eg.db:2.0.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lrbase.gga.eg.db/2.0.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lrbase.gga.eg.db/2.0.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lrbase.gga.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbase.gga.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbase.gga.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lrbase.gga.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lrbase.gga.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lrbase.gga.eg.db-inspect-deffile:

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