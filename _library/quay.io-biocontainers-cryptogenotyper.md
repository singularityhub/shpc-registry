---
layout: container
name:  "quay.io/biocontainers/cryptogenotyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cryptogenotyper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cryptogenotyper/container.yaml"
updated_at: "2022-10-27 00:18:40.975453"
latest: "1.0--py_3"
container_url: "https://biocontainers.pro/tools/cryptogenotyper"
aliases:
 - "cryptogenotyper"
versions:
 - "1.0--py_3"
description: "shpc-registry automated BioContainers addition for cryptogenotyper"
config: {"url": "https://biocontainers.pro/tools/cryptogenotyper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cryptogenotyper", "latest": {"1.0--py_3": "sha256:3aab47f844f2cc9b5772c5e3abde0200d4acb6a7a6f284a499361b31e45848eb"}, "tags": {"1.0--py_3": "sha256:3aab47f844f2cc9b5772c5e3abde0200d4acb6a7a6f284a499361b31e45848eb"}, "docker": "quay.io/biocontainers/cryptogenotyper", "aliases": {"cryptogenotyper": "/usr/local/bin/cryptogenotyper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cryptogenotyper.
shpc-registry automated BioContainers addition for cryptogenotyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cryptogenotyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cryptogenotyper:1.0--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cryptogenotyper/1.0--py_3
$ module help quay.io/biocontainers/cryptogenotyper/1.0--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cryptogenotyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cryptogenotyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cryptogenotyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cryptogenotyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cryptogenotyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cryptogenotyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cryptogenotyper

```bash
$ singularity exec <container> /usr/local/bin/cryptogenotyper
$ podman run --it --rm --entrypoint /usr/local/bin/cryptogenotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cryptogenotyper   -v ${PWD} -w ${PWD} <container> -c " $@"
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