---
layout: container
name:  "quay.io/biocontainers/libgenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libgenome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libgenome/container.yaml"
updated_at: "2024-02-22 03:04:23.316587"
latest: "1.3.1--h4ac6f70_7"
container_url: "https://biocontainers.pro/tools/libgenome"

versions:
 - "1.3.1--h9f5acd7_5"
 - "1.3.1--h4ac6f70_7"
description: "shpc-registry automated BioContainers addition for libgenome"
config: {"url": "https://biocontainers.pro/tools/libgenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libgenome", "latest": {"1.3.1--h4ac6f70_7": "sha256:6550787b273bebe18f74aa10f7bc34e5b0133e6e6b2a11c63fc13d7618451979"}, "tags": {"1.3.1--h9f5acd7_5": "sha256:aaa664a489c0b3461ffbe63941ba94c16976237f1904b12a019dac0b837f6d1a", "1.3.1--h4ac6f70_7": "sha256:6550787b273bebe18f74aa10f7bc34e5b0133e6e6b2a11c63fc13d7618451979"}, "docker": "quay.io/biocontainers/libgenome"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libgenome.
shpc-registry automated BioContainers addition for libgenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libgenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libgenome:1.3.1--h4ac6f70_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libgenome/1.3.1--h4ac6f70_7
$ module help quay.io/biocontainers/libgenome/1.3.1--h4ac6f70_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libgenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libgenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libgenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libgenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libgenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libgenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libgenome

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