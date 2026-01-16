---
layout: container
name:  "quay.io/biocontainers/bioconductor-h20kcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-h20kcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-h20kcod.db/container.yaml"
updated_at: "2026-01-16 03:59:59.796690"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-h20kcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-h20kcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-h20kcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-h20kcod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:28fe53fecc5d83c9d1a89b42b89cb9d4e4fdf4e306cb8ae5dbb8dc7c10d396bc"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:db399268ff0835557057f94639859b37fd1a327e519e8a00178c2de25e945e37", "3.4.0--r42hdfd78af_10": "sha256:5da6e4131b6ddd215220de2337545c3dc0af9b63821b0a5bf14119c793a120fd", "3.4.0--r43hdfd78af_11": "sha256:f776bbe0bdfff7d66d35dc90c135aeba9b4aefd3b56f64afa4b5586be0032814", "3.4.0--r43hdfd78af_12": "sha256:a35b28671416ea5ef47a4c119ce86ca889809f81057e733b3dea417f2b3be6b7", "3.4.0--r44hdfd78af_13": "sha256:28fe53fecc5d83c9d1a89b42b89cb9d4e4fdf4e306cb8ae5dbb8dc7c10d396bc"}, "docker": "quay.io/biocontainers/bioconductor-h20kcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-h20kcod.db.
shpc-registry automated BioContainers addition for bioconductor-h20kcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-h20kcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-h20kcod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-h20kcod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-h20kcod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-h20kcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h20kcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h20kcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-h20kcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-h20kcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-h20kcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-h20kcod.db

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