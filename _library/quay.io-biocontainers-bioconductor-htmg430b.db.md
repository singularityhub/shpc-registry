---
layout: container
name:  "quay.io/biocontainers/bioconductor-htmg430b.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htmg430b.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htmg430b.db/container.yaml"
updated_at: "2024-10-17 03:37:40.088220"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-htmg430b.db"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-htmg430b.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htmg430b.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htmg430b.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:a76fd1299c3119f5e024a1b1acb7eb85bbd1f9af1cf9c5a6cba651b315440c95"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:5b50bbc702015ab8f06ef5cf04d905a99e8c61ea069927c67516c92c9f6eaba5", "3.13.0--r42hdfd78af_2": "sha256:bba362302384a6fc89610627156aff2555184f5609d4e5b596a6f76f6d375392", "3.13.0--r43hdfd78af_3": "sha256:9f515168ed17787477644c63d608633ad211275708a9193026d83b57422603ba", "3.13.0--r43hdfd78af_4": "sha256:a76fd1299c3119f5e024a1b1acb7eb85bbd1f9af1cf9c5a6cba651b315440c95"}, "docker": "quay.io/biocontainers/bioconductor-htmg430b.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htmg430b.db.
shpc-registry automated BioContainers addition for bioconductor-htmg430b.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430b.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430b.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htmg430b.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-htmg430b.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htmg430b.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430b.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430b.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htmg430b.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htmg430b.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htmg430b.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htmg430b.db

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