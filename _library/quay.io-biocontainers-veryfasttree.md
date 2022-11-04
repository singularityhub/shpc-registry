---
layout: container
name:  "quay.io/biocontainers/veryfasttree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/veryfasttree/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/veryfasttree/container.yaml"
updated_at: "2022-11-04 00:24:56.172965"
latest: "3.1.1--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/veryfasttree"
aliases:
 - "VeryFastTree"
versions:
 - "3.1.1--h9f5acd7_1"
description: "shpc-registry automated BioContainers addition for veryfasttree"
config: {"url": "https://biocontainers.pro/tools/veryfasttree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for veryfasttree", "latest": {"3.1.1--h9f5acd7_1": "sha256:f61eb7aa8aa0a69a1791d3c702c78d32a5ed85af370c8da20dec66b837eed066"}, "tags": {"3.1.1--h9f5acd7_1": "sha256:f61eb7aa8aa0a69a1791d3c702c78d32a5ed85af370c8da20dec66b837eed066"}, "docker": "quay.io/biocontainers/veryfasttree", "aliases": {"VeryFastTree": "/usr/local/bin/VeryFastTree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/veryfasttree.
shpc-registry automated BioContainers addition for veryfasttree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/veryfasttree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/veryfasttree:3.1.1--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/veryfasttree/3.1.1--h9f5acd7_1
$ module help quay.io/biocontainers/veryfasttree/3.1.1--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### veryfasttree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### veryfasttree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### veryfasttree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### veryfasttree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### veryfasttree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### veryfasttree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### VeryFastTree

```bash
$ singularity exec <container> /usr/local/bin/VeryFastTree
$ podman run --it --rm --entrypoint /usr/local/bin/VeryFastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VeryFastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
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