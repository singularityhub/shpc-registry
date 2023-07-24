---
layout: container
name:  "quay.io/biocontainers/bioconductor-ragene20stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ragene20stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ragene20stprobeset.db/container.yaml"
updated_at: "2023-07-24 03:25:20.422035"
latest: "8.8.0--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-ragene20stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-ragene20stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ragene20stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ragene20stprobeset.db", "latest": {"8.8.0--r42hdfd78af_2": "sha256:3d2a6f1edf1a86d42d5ab12cd0fd32b67127b4672653dd08fb5ed737576696f0"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:54d8261156a6faa17523df1ebba3ea876b260406439e31ad8de3b9abf841d160", "8.8.0--r42hdfd78af_2": "sha256:3d2a6f1edf1a86d42d5ab12cd0fd32b67127b4672653dd08fb5ed737576696f0"}, "docker": "quay.io/biocontainers/bioconductor-ragene20stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ragene20stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-ragene20stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene20stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene20stprobeset.db:8.8.0--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ragene20stprobeset.db/8.8.0--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-ragene20stprobeset.db/8.8.0--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ragene20stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene20stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene20stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ragene20stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ragene20stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ragene20stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ragene20stprobeset.db

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