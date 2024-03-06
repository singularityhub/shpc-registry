---
layout: container
name:  "quay.io/biocontainers/bioconductor-r10kcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-r10kcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-r10kcod.db/container.yaml"
updated_at: "2024-03-06 02:52:21.933223"
latest: "3.4.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-r10kcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-r10kcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-r10kcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-r10kcod.db", "latest": {"3.4.0--r43hdfd78af_12": "sha256:9f7314dc18795d33f9a45e81013f03dbfa7448846fa284b3a7328dbf0ad20e2c"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:55e489bc22e12671775804eac6172ff9f2ca1fdc2ba043be54e1f24a58c04127", "3.4.0--r42hdfd78af_10": "sha256:55f4f709d4fb8e370be6955ede25c1b0b23dec7ad881111ea1a826067784a0d6", "3.4.0--r43hdfd78af_11": "sha256:3e19847a5e7479b3fddb1b59efa7d6c4060477f84c512053e1ef0a0000e80394", "3.4.0--r43hdfd78af_12": "sha256:9f7314dc18795d33f9a45e81013f03dbfa7448846fa284b3a7328dbf0ad20e2c"}, "docker": "quay.io/biocontainers/bioconductor-r10kcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-r10kcod.db.
shpc-registry automated BioContainers addition for bioconductor-r10kcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-r10kcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-r10kcod.db:3.4.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-r10kcod.db/3.4.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-r10kcod.db/3.4.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-r10kcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r10kcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r10kcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-r10kcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-r10kcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-r10kcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-r10kcod.db

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