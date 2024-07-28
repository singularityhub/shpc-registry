---
layout: container
name:  "quay.io/biocontainers/r-spieceasi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-spieceasi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-spieceasi/container.yaml"
updated_at: "2024-07-28 03:05:23.083489"
latest: "1.1.1--r43hdbdd923_5"
container_url: "https://biocontainers.pro/tools/r-spieceasi"

versions:
 - "1.1.1--r41h87f3376_1"
 - "1.1.1--r42h87f3376_2"
 - "1.1.1--r42hdbdd923_4"
 - "1.1.1--r43hdbdd923_5"
description: "shpc-registry automated BioContainers addition for r-spieceasi"
config: {"url": "https://biocontainers.pro/tools/r-spieceasi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-spieceasi", "latest": {"1.1.1--r43hdbdd923_5": "sha256:6b830f4e88519513fa13432d3791aef43f128bfb8e8dc64a42969af424277cc0"}, "tags": {"1.1.1--r41h87f3376_1": "sha256:daae54f3a91d74b9444a97b0772ba11ca12dc2b477e6fa299b8f2d08b8ef7861", "1.1.1--r42h87f3376_2": "sha256:739dba8b0f9a8ff6fa1d27c29cf92d50bd2890ebba26515cf3fcb65de1aea346", "1.1.1--r42hdbdd923_4": "sha256:7cb6b401ae1f0d3085b525474ecab33caf8c1890d1cc1d04fc369a33b195d23f", "1.1.1--r43hdbdd923_5": "sha256:6b830f4e88519513fa13432d3791aef43f128bfb8e8dc64a42969af424277cc0"}, "docker": "quay.io/biocontainers/r-spieceasi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-spieceasi.
shpc-registry automated BioContainers addition for r-spieceasi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-spieceasi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-spieceasi:1.1.1--r43hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-spieceasi/1.1.1--r43hdbdd923_5
$ module help quay.io/biocontainers/r-spieceasi/1.1.1--r43hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-spieceasi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-spieceasi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-spieceasi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-spieceasi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-spieceasi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-spieceasi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-spieceasi

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