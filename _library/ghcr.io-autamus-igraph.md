---
layout: container
name:  "ghcr.io/autamus/igraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/igraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/igraph/container.yaml"
updated_at: "2024-11-12 02:46:35.845566"
latest: "0.7.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/igraph"

versions:
 - "0.7.1"
 - "latest"
description: "igraph is a library collection for creating and manipulating graphs and analyzing networks. It is written in C and also exists as Python and R packages."
config: {"docker": "ghcr.io/autamus/igraph", "url": "https://github.com/orgs/autamus/packages/container/package/igraph", "maintainer": "@vsoch", "description": "igraph is a library collection for creating and manipulating graphs and analyzing networks. It is written in C and also exists as Python and R packages.", "latest": {"0.7.1": "sha256:2a6771a24bfc82a73388c410e93db25b0060c7100adaaea9097e92becd56850d"}, "tags": {"0.7.1": "sha256:2a6771a24bfc82a73388c410e93db25b0060c7100adaaea9097e92becd56850d", "latest": "sha256:2a6771a24bfc82a73388c410e93db25b0060c7100adaaea9097e92becd56850d"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/igraph.
igraph is a library collection for creating and manipulating graphs and analyzing networks. It is written in C and also exists as Python and R packages.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/igraph
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/igraph:0.7.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/igraph/0.7.1
$ module help ghcr.io/autamus/igraph/0.7.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### igraph

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