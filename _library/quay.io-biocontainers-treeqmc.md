---
layout: container
name:  "quay.io/biocontainers/treeqmc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treeqmc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treeqmc/container.yaml"
updated_at: "2025-05-17 03:57:05.110394"
latest: "3.0.1--hee07fbb_0"
container_url: "https://biocontainers.pro/tools/treeqmc"
aliases:
 - "tree-qmc"
versions:
 - "3.0.1--hee07fbb_0"
description: "singularity registry hpc automated addition for treeqmc"
config: {"url": "https://biocontainers.pro/tools/treeqmc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for treeqmc", "latest": {"3.0.1--hee07fbb_0": "sha256:42aaabd17c6d9b358914a9b2c50cd6ddd175a3774e2b8a41d657a1f1b9428d36"}, "tags": {"3.0.1--hee07fbb_0": "sha256:42aaabd17c6d9b358914a9b2c50cd6ddd175a3774e2b8a41d657a1f1b9428d36"}, "docker": "quay.io/biocontainers/treeqmc", "aliases": {"tree-qmc": "/usr/local/bin/tree-qmc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treeqmc.
singularity registry hpc automated addition for treeqmc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treeqmc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treeqmc:3.0.1--hee07fbb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treeqmc/3.0.1--hee07fbb_0
$ module help quay.io/biocontainers/treeqmc/3.0.1--hee07fbb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treeqmc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treeqmc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treeqmc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treeqmc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treeqmc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treeqmc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tree-qmc

```bash
$ singularity exec <container> /usr/local/bin/tree-qmc
$ podman run --it --rm --entrypoint /usr/local/bin/tree-qmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree-qmc   -v ${PWD} -w ${PWD} <container> -c " $@"
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