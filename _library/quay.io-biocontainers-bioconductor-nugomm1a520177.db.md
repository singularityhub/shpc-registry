---
layout: container
name:  "quay.io/biocontainers/bioconductor-nugomm1a520177.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nugomm1a520177.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nugomm1a520177.db/container.yaml"
updated_at: "2023-04-17 02:50:56.083663"
latest: "3.4.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-nugomm1a520177.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nugomm1a520177.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177.db", "latest": {"3.4.0--r42hdfd78af_10": "sha256:7244f080d9c9b3bb685f1a0b2a355116314b83ad36ec9d13ba7c8653ae8bb292"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:6d9d09d0c388e8c905495722da6c023aef0a499a4df4aa8741ec9f28cc36b387", "3.4.0--r42hdfd78af_10": "sha256:7244f080d9c9b3bb685f1a0b2a355116314b83ad36ec9d13ba7c8653ae8bb292"}, "docker": "quay.io/biocontainers/bioconductor-nugomm1a520177.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nugomm1a520177.db.
shpc-registry automated BioContainers addition for bioconductor-nugomm1a520177.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nugomm1a520177.db:3.4.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nugomm1a520177.db/3.4.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-nugomm1a520177.db/3.4.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nugomm1a520177.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugomm1a520177.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nugomm1a520177.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nugomm1a520177.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nugomm1a520177.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nugomm1a520177.db

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