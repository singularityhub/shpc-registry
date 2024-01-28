---
layout: container
name:  "quay.io/biocontainers/bioconductor-lrbase.bta.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lrbase.bta.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lrbase.bta.eg.db/container.yaml"
updated_at: "2024-01-28 03:39:24.825011"
latest: "2.0.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lrbase.bta.eg.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.0.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lrbase.bta.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lrbase.bta.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lrbase.bta.eg.db", "latest": {"2.0.0--r41hdfd78af_0": "sha256:1d386cf3d0ecc812699dde83bafb600aee4b43668696a1e358336593d1db769d"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:1d386cf3d0ecc812699dde83bafb600aee4b43668696a1e358336593d1db769d"}, "docker": "quay.io/biocontainers/bioconductor-lrbase.bta.eg.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lrbase.bta.eg.db.
shpc-registry automated BioContainers addition for bioconductor-lrbase.bta.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbase.bta.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lrbase.bta.eg.db:2.0.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lrbase.bta.eg.db/2.0.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lrbase.bta.eg.db/2.0.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lrbase.bta.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbase.bta.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrbase.bta.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lrbase.bta.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lrbase.bta.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lrbase.bta.eg.db-inspect-deffile:

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