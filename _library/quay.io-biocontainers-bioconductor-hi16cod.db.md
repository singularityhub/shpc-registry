---
layout: container
name:  "quay.io/biocontainers/bioconductor-hi16cod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hi16cod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hi16cod.db/container.yaml"
updated_at: "2025-08-28 12:01:17.660538"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hi16cod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hi16cod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hi16cod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hi16cod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:1daa2d1c9cf015beb15d8aac88849a5f1ed8e306ed24a2f719c97884c5c01ace"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:ee3059d5b9d3c6c247ca72dee29860133613f6c858b5dc5c2dace97cbcf2c72f", "3.4.0--r42hdfd78af_10": "sha256:c27a3977cf2387f40f372f0747ced94f2a2bc5f34ab5aeca80c3101c8e1a986c", "3.4.0--r43hdfd78af_11": "sha256:9b0390dd215adcc790d202e9ec5bb327ad12bda067e8a6e588941d5e712df64a", "3.4.0--r43hdfd78af_12": "sha256:e3c58fdfc3f2dca7a2e23fe92eb1c584738dcba27b6536498b75ae18ccec0099", "3.4.0--r44hdfd78af_13": "sha256:1daa2d1c9cf015beb15d8aac88849a5f1ed8e306ed24a2f719c97884c5c01ace"}, "docker": "quay.io/biocontainers/bioconductor-hi16cod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hi16cod.db.
shpc-registry automated BioContainers addition for bioconductor-hi16cod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hi16cod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hi16cod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hi16cod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hi16cod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hi16cod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hi16cod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hi16cod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hi16cod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hi16cod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hi16cod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hi16cod.db

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