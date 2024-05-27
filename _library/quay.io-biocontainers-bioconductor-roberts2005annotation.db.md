---
layout: container
name:  "quay.io/biocontainers/bioconductor-roberts2005annotation.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-roberts2005annotation.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-roberts2005annotation.db/container.yaml"
updated_at: "2024-05-27 03:16:37.912292"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-roberts2005annotation.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-roberts2005annotation.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-roberts2005annotation.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-roberts2005annotation.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:7aa99e7b88c1aeb98614ca84e2fb89983aed5eb22640fa9dd30f90a244a129a7"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:a09f042c60f941931a10bc6b822cff1250d5395cdc50d1d6e87163c20a25d18a", "3.2.3--r42hdfd78af_10": "sha256:be7a26a173c12057b93c1874518efe9f31f4ca6d971b253aed916703824326f7", "3.2.3--r43hdfd78af_11": "sha256:f08ddff05975d3681a686c1584469f9f6183332df292f4304789a83a132d927b", "3.2.3--r43hdfd78af_12": "sha256:7aa99e7b88c1aeb98614ca84e2fb89983aed5eb22640fa9dd30f90a244a129a7"}, "docker": "quay.io/biocontainers/bioconductor-roberts2005annotation.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-roberts2005annotation.db.
shpc-registry automated BioContainers addition for bioconductor-roberts2005annotation.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-roberts2005annotation.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-roberts2005annotation.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-roberts2005annotation.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-roberts2005annotation.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-roberts2005annotation.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roberts2005annotation.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roberts2005annotation.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-roberts2005annotation.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-roberts2005annotation.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-roberts2005annotation.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-roberts2005annotation.db

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