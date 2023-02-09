---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbhmdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbhmdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbhmdb/container.yaml"
updated_at: "2023-02-09 18:10:27.525978"
latest: "1.4.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbhmdb"

versions:
 - "1.0.3--r41hc247a5b_1"
 - "1.4.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodbhmdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbhmdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodbhmdb", "latest": {"1.4.0--r42hc247a5b_0": "sha256:8e8d3c806c2a016216883c38f8c65227cc6564061e422eb776354564a2572855"}, "tags": {"1.0.3--r41hc247a5b_1": "sha256:56c955a1249168867b206ef482be91e6206737d6fe5e104b81bc8c7251d6a8cc", "1.4.0--r42hc247a5b_0": "sha256:8e8d3c806c2a016216883c38f8c65227cc6564061e422eb776354564a2572855"}, "docker": "quay.io/biocontainers/bioconductor-biodbhmdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbhmdb.
shpc-registry automated BioContainers addition for bioconductor-biodbhmdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbhmdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbhmdb:1.4.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbhmdb/1.4.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-biodbhmdb/1.4.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbhmdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbhmdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbhmdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbhmdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbhmdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbhmdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbhmdb

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