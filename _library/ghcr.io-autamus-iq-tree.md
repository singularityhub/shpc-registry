---
layout: container
name:  "ghcr.io/autamus/iq-tree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/iq-tree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/iq-tree/container.yaml"
updated_at: "2024-11-20 02:57:25.731015"
latest: "2.1.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/iq-tree"
aliases:
 - "iq-tree2"
versions:
 - "2.0.6"
 - "2.1.3"
 - "latest"
description: "IQ-TREE (http://www.iqtree.org, last accessed February 6, 2020) is a user-friendly and widely used software package for phylogenetic inference using maximum likelihood."
config: {"docker": "ghcr.io/autamus/iq-tree", "url": "https://github.com/orgs/autamus/packages/container/package/iq-tree", "maintainer": "@vsoch", "description": "IQ-TREE (http://www.iqtree.org, last accessed February 6, 2020) is a user-friendly and widely used software package for phylogenetic inference using maximum likelihood.", "latest": {"2.1.3": "sha256:935757d6b8520265ee12ccc5cd941fc38d6b2466dba73ab556425e19bea76ad4"}, "tags": {"2.0.6": "sha256:3b3fa503ae69d5fbddbd6adb92462ad5bc09bdf814140001bd04baacc4feae9e", "2.1.3": "sha256:935757d6b8520265ee12ccc5cd941fc38d6b2466dba73ab556425e19bea76ad4", "latest": "sha256:935757d6b8520265ee12ccc5cd941fc38d6b2466dba73ab556425e19bea76ad4"}, "aliases": {"iq-tree2": "/opt/view/bin/iq-tree2"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/iq-tree.
IQ-TREE (http://www.iqtree.org, last accessed February 6, 2020) is a user-friendly and widely used software package for phylogenetic inference using maximum likelihood.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/iq-tree
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/iq-tree:2.1.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/iq-tree/2.1.3
$ module help ghcr.io/autamus/iq-tree/2.1.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iq-tree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iq-tree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iq-tree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iq-tree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iq-tree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iq-tree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iq-tree2

```bash
$ singularity exec <container> /opt/view/bin/iq-tree2
$ podman run --it --rm --entrypoint /opt/view/bin/iq-tree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/iq-tree2   -v ${PWD} -w ${PWD} <container> -c " $@"
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