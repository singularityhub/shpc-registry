---
layout: container
name:  "quay.io/biocontainers/bioconductor-rwgcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rwgcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rwgcod.db/container.yaml"
updated_at: "2025-10-10 03:39:15.462709"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rwgcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rwgcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rwgcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rwgcod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:22a48dbe138cdf01dd84f596e0e0aef0e806a9e78284e6a0e18782d87cfbe302"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:4b78019c20c9532847028d746db4d3b210e40c093256343d7e6b799147a50e79", "3.4.0--r42hdfd78af_10": "sha256:aa6c1e5eb8ebb54d8042461de93b8ac79b03b03851a66e54293e8dba026c3b0c", "3.4.0--r43hdfd78af_11": "sha256:a79af7633c59d146e912ba8f5b8f6f984046e466b38c6fcd51eb27934fa83d97", "3.4.0--r43hdfd78af_12": "sha256:53ac5fa0210225a5fc993306e04ca34b3f7384d9f3b732befa4f2a4278d6b202", "3.4.0--r44hdfd78af_13": "sha256:22a48dbe138cdf01dd84f596e0e0aef0e806a9e78284e6a0e18782d87cfbe302"}, "docker": "quay.io/biocontainers/bioconductor-rwgcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rwgcod.db.
shpc-registry automated BioContainers addition for bioconductor-rwgcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rwgcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rwgcod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rwgcod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rwgcod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rwgcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rwgcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rwgcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rwgcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rwgcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rwgcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rwgcod.db

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