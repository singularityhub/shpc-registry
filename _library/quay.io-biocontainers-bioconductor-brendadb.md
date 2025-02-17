---
layout: container
name:  "quay.io/biocontainers/bioconductor-brendadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-brendadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-brendadb/container.yaml"
updated_at: "2025-02-17 03:31:03.061083"
latest: "1.20.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-brendadb"

versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.11.0--r42hc247a5b_0"
 - "1.11.0--r42hf17093f_1"
 - "1.14.0--r43hf17093f_0"
 - "1.16.0--r43hf17093f_0"
 - "1.20.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-brendadb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-brendadb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-brendadb", "latest": {"1.20.0--r44he5774e6_0": "sha256:ca774c4cf6aa9e97dfc4bf255dc4d5ec8799e384a665228b9f109d23b3f86e31"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:2d0c714edd59e197cb2aba2707ab7338986a5cce50941cf45f3ba674f72318e1", "1.11.0--r42hc247a5b_0": "sha256:ea41a492edd5dc232d89f7541b22835f4f243f6f2fbc62566c1d69bca0a4f83b", "1.11.0--r42hf17093f_1": "sha256:7548e0ad9c2fc5f915026a73c0206b5791ca21744f46fec8fea0f81cb23d041c", "1.14.0--r43hf17093f_0": "sha256:1d53e9220fb46fac16ca61a334487bab2353ffdd98d845532e14a1016407580d", "1.16.0--r43hf17093f_0": "sha256:01405a5ddcfc868d13839f8a0abef7cf9049ad30430298f6edd5eccf88cea0b9", "1.20.0--r44he5774e6_0": "sha256:ca774c4cf6aa9e97dfc4bf255dc4d5ec8799e384a665228b9f109d23b3f86e31"}, "docker": "quay.io/biocontainers/bioconductor-brendadb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-brendadb.
shpc-registry automated BioContainers addition for bioconductor-brendadb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-brendadb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-brendadb:1.20.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-brendadb/1.20.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-brendadb/1.20.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-brendadb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brendadb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brendadb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-brendadb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-brendadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-brendadb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-brendadb

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