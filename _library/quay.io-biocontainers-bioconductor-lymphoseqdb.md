---
layout: container
name:  "quay.io/biocontainers/bioconductor-lymphoseqdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lymphoseqdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lymphoseqdb/container.yaml"
updated_at: "2024-02-13 02:32:25.648479"
latest: "0.99.2--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-lymphoseqdb"

versions:
 - "0.99.2--r41hdfd78af_9"
 - "0.99.2--r42hdfd78af_10"
 - "0.99.2--r43hdfd78af_11"
 - "0.99.2--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-lymphoseqdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lymphoseqdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lymphoseqdb", "latest": {"0.99.2--r43hdfd78af_12": "sha256:3ff489129ec8ebd41dd3056f4f8b46a644b7e718a43f9b06a5ff3b1cf33d5c83"}, "tags": {"0.99.2--r41hdfd78af_9": "sha256:103f70f01cb108bd40de2f8b00ecd2b56ffc27c6f73438234b7ecad2ce4b3dc6", "0.99.2--r42hdfd78af_10": "sha256:efd2a5b57b593dbcc64d28bfaa8cb9f6db130fc30336cbf03eac3afd5d21c58c", "0.99.2--r43hdfd78af_11": "sha256:95d1f5b1616652ff65efab8ab3978ea1b648136da242fae15c6fbbb30c5914f8", "0.99.2--r43hdfd78af_12": "sha256:3ff489129ec8ebd41dd3056f4f8b46a644b7e718a43f9b06a5ff3b1cf33d5c83"}, "docker": "quay.io/biocontainers/bioconductor-lymphoseqdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lymphoseqdb.
shpc-registry automated BioContainers addition for bioconductor-lymphoseqdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lymphoseqdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lymphoseqdb:0.99.2--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lymphoseqdb/0.99.2--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-lymphoseqdb/0.99.2--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lymphoseqdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lymphoseqdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lymphoseqdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lymphoseqdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lymphoseqdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lymphoseqdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lymphoseqdb

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