---
layout: container
name:  "quay.io/biocontainers/bioconductor-lapointe.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lapointe.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lapointe.db/container.yaml"
updated_at: "2023-06-03 03:30:21.933133"
latest: "3.2.3--r42hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-lapointe.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-lapointe.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lapointe.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lapointe.db", "latest": {"3.2.3--r42hdfd78af_11": "sha256:a6061038d0ef706495d91f1439bbbd0c7e58c84d8f354b17757806c3937c6fa6"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:a5ac2999123a29b02343dba714efe84a52ec1166e2e1d17d6c5a8bc84ba33f70", "3.2.3--r42hdfd78af_11": "sha256:a6061038d0ef706495d91f1439bbbd0c7e58c84d8f354b17757806c3937c6fa6"}, "docker": "quay.io/biocontainers/bioconductor-lapointe.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lapointe.db.
shpc-registry automated BioContainers addition for bioconductor-lapointe.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lapointe.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lapointe.db:3.2.3--r42hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lapointe.db/3.2.3--r42hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-lapointe.db/3.2.3--r42hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lapointe.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lapointe.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lapointe.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lapointe.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lapointe.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lapointe.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lapointe.db

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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