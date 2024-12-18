---
layout: container
name:  "quay.io/biocontainers/bioconductor-mwgcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mwgcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mwgcod.db/container.yaml"
updated_at: "2024-12-18 03:32:41.989151"
latest: "3.4.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mwgcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mwgcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mwgcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mwgcod.db", "latest": {"3.4.0--r43hdfd78af_12": "sha256:bb5ca7d4a1e6e04f1cd86a759aa6cef5c999119898302aa1570999b25e721c17"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:31815f219e5ecbb6154e2e8100547281d8da9043d97a39d96ecf0e4236b5309c", "3.4.0--r42hdfd78af_10": "sha256:8d8913337b184a7dcd2f522d78912770a80d683aab2ef74a0b45b9233470d9d7", "3.4.0--r43hdfd78af_11": "sha256:5907c42c2b44cb9dd232a8fde18e8a55e5d4fe128a2f7861d0be2de4a2725f93", "3.4.0--r43hdfd78af_12": "sha256:bb5ca7d4a1e6e04f1cd86a759aa6cef5c999119898302aa1570999b25e721c17"}, "docker": "quay.io/biocontainers/bioconductor-mwgcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mwgcod.db.
shpc-registry automated BioContainers addition for bioconductor-mwgcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mwgcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mwgcod.db:3.4.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mwgcod.db/3.4.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mwgcod.db/3.4.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mwgcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mwgcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mwgcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mwgcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mwgcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mwgcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mwgcod.db

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