---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcseq/container.yaml"
updated_at: "2022-10-27 00:43:44.126199"
latest: "1.8.0--r36_1"
container_url: "https://biocontainers.pro/tools/bioconductor-tcseq"

versions:
 - "1.8.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-tcseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcseq", "latest": {"1.8.0--r36_1": "sha256:3bd45f5828dba9b9310463d6facf07c5ece7c483c25642364f82f86028fdb742"}, "tags": {"1.8.0--r36_1": "sha256:3bd45f5828dba9b9310463d6facf07c5ece7c483c25642364f82f86028fdb742"}, "docker": "quay.io/biocontainers/bioconductor-tcseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcseq.
shpc-registry automated BioContainers addition for bioconductor-tcseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcseq:1.8.0--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcseq/1.8.0--r36_1
$ module help quay.io/biocontainers/bioconductor-tcseq/1.8.0--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tcseq

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