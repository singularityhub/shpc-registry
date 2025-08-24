---
layout: container
name:  "quay.io/biocontainers/bioconductor-htrat230pm.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htrat230pm.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htrat230pm.db/container.yaml"
updated_at: "2025-08-24 04:11:20.708633"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-htrat230pm.db"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-htrat230pm.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htrat230pm.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htrat230pm.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:f20cfc1d9c5bafdd69777ae6d0a560fda48b5b37eb42b7d152fa917b31fd677e"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:18ee6b2a5a8d7a2c630aabdf1041e0984f28c65a6ddfdd6dc236992cdd14767f", "3.13.0--r42hdfd78af_2": "sha256:14a3c6b6113bc0ba48c3b06bfea1ccede46faca68d5497c3c4bfc639a14ee1d6", "3.13.0--r43hdfd78af_3": "sha256:8ba81b6df7b44861f478cd3bdce95f06c603ec19448f838fe4d61a7d3094c411", "3.13.0--r43hdfd78af_4": "sha256:04389eab6b8287c1942b841c320858585485341910c248274e4d9d120ac53fa7", "3.13.0--r44hdfd78af_5": "sha256:f20cfc1d9c5bafdd69777ae6d0a560fda48b5b37eb42b7d152fa917b31fd677e"}, "docker": "quay.io/biocontainers/bioconductor-htrat230pm.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htrat230pm.db.
shpc-registry automated BioContainers addition for bioconductor-htrat230pm.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htrat230pm.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htrat230pm.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htrat230pm.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-htrat230pm.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htrat230pm.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htrat230pm.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htrat230pm.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htrat230pm.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htrat230pm.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htrat230pm.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htrat230pm.db

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