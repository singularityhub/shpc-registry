---
layout: container
name:  "quay.io/biocontainers/bioconductor-msigdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msigdb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msigdb/container.yaml"
updated_at: "2022-11-04 00:04:39.568467"
latest: "1.2.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-msigdb"
aliases:
 - ".bioconductor-msigdb-post-link.sh"
 - ".bioconductor-msigdb-pre-unlink.sh"
versions:
 - "1.2.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-msigdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msigdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msigdb", "latest": {"1.2.0--r41hdfd78af_1": "sha256:105b75f44eb682c377b06dcf11879d1f0e8df04b3e0eb6f722130e81981b35d4"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:105b75f44eb682c377b06dcf11879d1f0e8df04b3e0eb6f722130e81981b35d4"}, "docker": "quay.io/biocontainers/bioconductor-msigdb", "aliases": {".bioconductor-msigdb-post-link.sh": "/usr/local/bin/.bioconductor-msigdb-post-link.sh", ".bioconductor-msigdb-pre-unlink.sh": "/usr/local/bin/.bioconductor-msigdb-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msigdb.
shpc-registry automated BioContainers addition for bioconductor-msigdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msigdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msigdb:1.2.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msigdb/1.2.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-msigdb/1.2.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msigdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msigdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msigdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msigdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msigdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msigdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-msigdb-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-msigdb-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-msigdb-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-msigdb-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-msigdb-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-msigdb-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-msigdb-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-msigdb-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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