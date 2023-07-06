---
layout: container
name:  "quay.io/biocontainers/ncbi-vdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-vdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-vdb/container.yaml"
updated_at: "2023-07-06 03:19:22.533824"
latest: "3.0.5--hdbdd923_2"
container_url: "https://biocontainers.pro/tools/ncbi-vdb"

versions:
 - "3.0.0--pl5321h87f3376_0"
 - "3.0.2--h87f3376_0"
 - "3.0.5--h87f3376_0"
 - "3.0.5--hdbdd923_2"
description: "shpc-registry automated BioContainers addition for ncbi-vdb"
config: {"url": "https://biocontainers.pro/tools/ncbi-vdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-vdb", "latest": {"3.0.5--hdbdd923_2": "sha256:7fbaa66b85908c236f293990058119f1be03a45ac71d7818d4ec2b3015a523d0"}, "tags": {"3.0.0--pl5321h87f3376_0": "sha256:3b6375b7218a284bb56576729f38aa69f5a0ee208535f90fbfbc21022e71057d", "3.0.2--h87f3376_0": "sha256:aba43c21a8b43784d533b628aa938ea862735e780bdefbfbc38874fc747644bb", "3.0.5--h87f3376_0": "sha256:6fdeb8dac5974c888aa8c986af7709da148127d749e1998588b47ddc922f2c8a", "3.0.5--hdbdd923_2": "sha256:7fbaa66b85908c236f293990058119f1be03a45ac71d7818d4ec2b3015a523d0"}, "docker": "quay.io/biocontainers/ncbi-vdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-vdb.
shpc-registry automated BioContainers addition for ncbi-vdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-vdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-vdb:3.0.5--hdbdd923_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-vdb/3.0.5--hdbdd923_2
$ module help quay.io/biocontainers/ncbi-vdb/3.0.5--hdbdd923_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-vdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-vdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-vdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-vdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ncbi-vdb

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