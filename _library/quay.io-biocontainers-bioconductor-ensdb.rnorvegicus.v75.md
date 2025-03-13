---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75/container.yaml"
updated_at: "2025-03-13 03:21:58.480232"
latest: "2.99.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.rnorvegicus.v75"

versions:
 - "2.99.0--r41hdfd78af_9"
 - "2.99.0--r42hdfd78af_10"
 - "2.99.0--r43hdfd78af_11"
 - "2.99.0--r43hdfd78af_12"
 - "2.99.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v75"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.rnorvegicus.v75", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v75", "latest": {"2.99.0--r44hdfd78af_13": "sha256:06861a4f5c3b2461b86b685dff805cee3ecae7d0859a5d5b6bca79ec0a800306"}, "tags": {"2.99.0--r41hdfd78af_9": "sha256:a6c67b571a999f7171c5b2c1cfa279c3b9c67c5f28a32ea7d601aa94cf675c2c", "2.99.0--r42hdfd78af_10": "sha256:e0941a522ddd44803e56b63164498e05eb35537003df2b006aa4939445d14eca", "2.99.0--r43hdfd78af_11": "sha256:3b54dc7f642c47f0862e83bd002ed5844865f56e232e93949123e95a8998e02a", "2.99.0--r43hdfd78af_12": "sha256:dcda893bdebb0d87a42d7a9a25afa75c59dffdca21455e5a599159405b23221f", "2.99.0--r44hdfd78af_13": "sha256:06861a4f5c3b2461b86b685dff805cee3ecae7d0859a5d5b6bca79ec0a800306"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75.
shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v75
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75:2.99.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75/2.99.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v75/2.99.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.rnorvegicus.v75-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.rnorvegicus.v75-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.rnorvegicus.v75-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.rnorvegicus.v75-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.rnorvegicus.v75-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.rnorvegicus.v75-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensdb.rnorvegicus.v75

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