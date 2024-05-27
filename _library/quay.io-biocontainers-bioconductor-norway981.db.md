---
layout: container
name:  "quay.io/biocontainers/bioconductor-norway981.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-norway981.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-norway981.db/container.yaml"
updated_at: "2024-05-27 03:24:27.460512"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-norway981.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-norway981.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-norway981.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-norway981.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:e7611f43a2b60db1546f4ad2f017142a9fb83da70478ad7bfa9defc67f431c57"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:a8d92880313dce7de1a6b77a17ba5b5f3ee4cbbe03a2a466d59686dd428d9f42", "3.2.3--r42hdfd78af_10": "sha256:02f613d59a80a43edc3cf003476f1a94e2257eda41607b6392be327648278645", "3.2.3--r43hdfd78af_11": "sha256:18f0c3827199d4593f6eb12850c14714d0e3a9d60177034b515ecd0f97882823", "3.2.3--r43hdfd78af_12": "sha256:e7611f43a2b60db1546f4ad2f017142a9fb83da70478ad7bfa9defc67f431c57"}, "docker": "quay.io/biocontainers/bioconductor-norway981.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-norway981.db.
shpc-registry automated BioContainers addition for bioconductor-norway981.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-norway981.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-norway981.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-norway981.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-norway981.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-norway981.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-norway981.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-norway981.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-norway981.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-norway981.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-norway981.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-norway981.db

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