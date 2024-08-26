---
layout: container
name:  "quay.io/biocontainers/tree-qmc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tree-qmc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tree-qmc/container.yaml"
updated_at: "2024-08-26 03:06:33.561190"
latest: "3.0.0--hee07fbb_0"
container_url: "https://biocontainers.pro/tools/tree-qmc"
aliases:
 - "TREE-QMC"
versions:
 - "3.0.0--hee07fbb_0"
description: "singularity registry hpc automated addition for tree-qmc"
config: {"url": "https://biocontainers.pro/tools/tree-qmc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tree-qmc", "latest": {"3.0.0--hee07fbb_0": "sha256:07ed7e79a6cd454ae91629962384ba242f7f2fc36d62b7fc99e294d82a69ec04"}, "tags": {"3.0.0--hee07fbb_0": "sha256:07ed7e79a6cd454ae91629962384ba242f7f2fc36d62b7fc99e294d82a69ec04"}, "docker": "quay.io/biocontainers/tree-qmc", "aliases": {"TREE-QMC": "/usr/local/bin/TREE-QMC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tree-qmc.
singularity registry hpc automated addition for tree-qmc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tree-qmc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tree-qmc:3.0.0--hee07fbb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tree-qmc/3.0.0--hee07fbb_0
$ module help quay.io/biocontainers/tree-qmc/3.0.0--hee07fbb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tree-qmc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tree-qmc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tree-qmc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tree-qmc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tree-qmc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tree-qmc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TREE-QMC

```bash
$ singularity exec <container> /usr/local/bin/TREE-QMC
$ podman run --it --rm --entrypoint /usr/local/bin/TREE-QMC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TREE-QMC   -v ${PWD} -w ${PWD} <container> -c " $@"
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