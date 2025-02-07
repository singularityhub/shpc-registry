---
layout: container
name:  "quay.io/biocontainers/bioconductor-feast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-feast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-feast/container.yaml"
updated_at: "2025-02-07 03:20:03.919518"
latest: "1.14.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-feast"
aliases:
 - "glpsol"
versions:
 - "1.2.0--r41hc0cfd56_2"
 - "1.6.0--r42hc0cfd56_0"
 - "1.6.0--r42ha9d7317_1"
 - "1.8.0--r43ha9d7317_0"
 - "1.10.0--r43ha9d7317_0"
 - "1.14.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-feast"
config: {"url": "https://biocontainers.pro/tools/bioconductor-feast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-feast", "latest": {"1.14.0--r44h3df3fcb_0": "sha256:e903f8d24c3c62cb7fe7cbe138a8454382fc7df06a2e616c619b8e73acf93969"}, "tags": {"1.2.0--r41hc0cfd56_2": "sha256:ed479d91c618d72a9cf5c3452c8f02625da90cabb56f92c0db6e7769a307d89f", "1.6.0--r42hc0cfd56_0": "sha256:88a6c06b070905d8a5a4abf0e73efaf71bcfd9d47c62634bc81734ec813aaa73", "1.6.0--r42ha9d7317_1": "sha256:194fe925aa9af8995e53c36e20e8d07fc078e185613b5f404df1299962f407ac", "1.8.0--r43ha9d7317_0": "sha256:3e339f5849f5aa6bacedff783b0e606f9198f7c5ca9da76f9856e3d72e0ad5e1", "1.10.0--r43ha9d7317_0": "sha256:1c1c50fa6fa5aa9a05ac4a9537c72995bffc4b9b86b93d2a2f6dbb7b7f52eb38", "1.14.0--r44h3df3fcb_0": "sha256:e903f8d24c3c62cb7fe7cbe138a8454382fc7df06a2e616c619b8e73acf93969"}, "docker": "quay.io/biocontainers/bioconductor-feast", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-feast.
shpc-registry automated BioContainers addition for bioconductor-feast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-feast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-feast:1.14.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-feast/1.14.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-feast/1.14.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-feast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-feast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-feast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-feast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-feast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-feast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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