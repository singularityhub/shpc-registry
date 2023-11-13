---
layout: container
name:  "quay.io/biocontainers/google-sparsehash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/google-sparsehash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/google-sparsehash/container.yaml"
updated_at: "2023-11-13 03:20:22.423820"
latest: "2.0.3--1"
container_url: "https://biocontainers.pro/tools/google-sparsehash"
aliases:
 - "sparsetable_unittest"
versions:
 - "2.0.3--1"
description: "shpc-registry automated BioContainers addition for google-sparsehash"
config: {"url": "https://biocontainers.pro/tools/google-sparsehash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for google-sparsehash", "latest": {"2.0.3--1": "sha256:b5eabd7ede74ceaebe0395d65a9794f4b95ce2db835f75b199bb1d6b37e3b363"}, "tags": {"2.0.3--1": "sha256:b5eabd7ede74ceaebe0395d65a9794f4b95ce2db835f75b199bb1d6b37e3b363"}, "docker": "quay.io/biocontainers/google-sparsehash", "aliases": {"sparsetable_unittest": "/usr/local/bin/sparsetable_unittest"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/google-sparsehash.
shpc-registry automated BioContainers addition for google-sparsehash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/google-sparsehash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/google-sparsehash:2.0.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/google-sparsehash/2.0.3--1
$ module help quay.io/biocontainers/google-sparsehash/2.0.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### google-sparsehash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### google-sparsehash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### google-sparsehash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### google-sparsehash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### google-sparsehash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### google-sparsehash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sparsetable_unittest

```bash
$ singularity exec <container> /usr/local/bin/sparsetable_unittest
$ podman run --it --rm --entrypoint /usr/local/bin/sparsetable_unittest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparsetable_unittest   -v ${PWD} -w ${PWD} <container> -c " $@"
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