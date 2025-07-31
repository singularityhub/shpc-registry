---
layout: container
name:  "quay.io/biocontainers/ghost-tree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghost-tree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ghost-tree/container.yaml"
updated_at: "2025-07-31 04:08:34.877387"
latest: "0.2.2--py_1"
container_url: "https://biocontainers.pro/tools/ghost-tree"

versions:
 - "0.2.2--py_1"
description: "shpc-registry automated BioContainers addition for ghost-tree"
config: {"url": "https://biocontainers.pro/tools/ghost-tree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghost-tree", "latest": {"0.2.2--py_1": "sha256:c490af82b43c3090e908134bd9cc9cabc18a4f055f9e575b3f06364652356bf8"}, "tags": {"0.2.2--py_1": "sha256:c490af82b43c3090e908134bd9cc9cabc18a4f055f9e575b3f06364652356bf8"}, "docker": "quay.io/biocontainers/ghost-tree"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghost-tree.
shpc-registry automated BioContainers addition for ghost-tree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghost-tree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghost-tree:0.2.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghost-tree/0.2.2--py_1
$ module help quay.io/biocontainers/ghost-tree/0.2.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghost-tree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghost-tree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghost-tree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghost-tree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghost-tree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghost-tree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghost-tree

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