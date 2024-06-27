---
layout: container
name:  "quay.io/biocontainers/bioconductor-geometadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geometadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geometadb/container.yaml"
updated_at: "2024-06-27 03:49:20.788492"
latest: "1.64.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geometadb"

versions:
 - "1.56.0--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geometadb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geometadb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geometadb", "latest": {"1.64.0--r43hdfd78af_0": "sha256:e3845bd217a5e7658972bbaeac53ebb294ab91c17f153ff141a22736b3aa7769"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:bd0b8aad6570684116d2355d794e3396a46779638aa6351247ca4c4285fc56fd", "1.60.0--r42hdfd78af_0": "sha256:d06993b580587f7f03a0fc344c6db957cac91a069c65e7da49c5fc28a5e4bca0", "1.62.0--r43hdfd78af_0": "sha256:ea3051d161514c49ae196b44482850e74d53ef09c5c24ede888e82c075508ecb", "1.64.0--r43hdfd78af_0": "sha256:e3845bd217a5e7658972bbaeac53ebb294ab91c17f153ff141a22736b3aa7769"}, "docker": "quay.io/biocontainers/bioconductor-geometadb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geometadb.
shpc-registry automated BioContainers addition for bioconductor-geometadb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geometadb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geometadb:1.64.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geometadb/1.64.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geometadb/1.64.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geometadb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geometadb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geometadb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geometadb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geometadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geometadb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geometadb

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