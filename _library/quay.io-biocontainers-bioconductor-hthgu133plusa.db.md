---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133plusa.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133plusa.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133plusa.db/container.yaml"
updated_at: "2025-08-01 11:00:34.103925"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133plusa.db"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133plusa.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133plusa.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133plusa.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:a255cc39511fc65404686262807bc9fb8b66c75da961b29194632056b2916be1"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:bf8366087cfa7a0448a0c13c9c64abcb30cb4b90a1d3f18c8e2e3703e2d5cc4a", "3.13.0--r42hdfd78af_2": "sha256:c0269b21ce9bd4088d9948612416d26b72d906334da217fe86f1e9ac658a4334", "3.13.0--r43hdfd78af_3": "sha256:7e22f07b80f7669662cc267b9c343dd212127a9c1054b2a3920f4613d7492f8d", "3.13.0--r43hdfd78af_4": "sha256:b6a2a1ecf96b91bc93a5472f82a854fa3f67ffc640d226b5bc51c9f8ac7deeda", "3.13.0--r44hdfd78af_5": "sha256:a255cc39511fc65404686262807bc9fb8b66c75da961b29194632056b2916be1"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133plusa.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133plusa.db.
shpc-registry automated BioContainers addition for bioconductor-hthgu133plusa.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133plusa.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133plusa.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133plusa.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-hthgu133plusa.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133plusa.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133plusa.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133plusa.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133plusa.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133plusa.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133plusa.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hthgu133plusa.db

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