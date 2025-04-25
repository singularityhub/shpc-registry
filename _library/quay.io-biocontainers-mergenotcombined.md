---
layout: container
name:  "quay.io/biocontainers/mergenotcombined"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mergenotcombined/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mergenotcombined/container.yaml"
updated_at: "2025-04-25 02:27:04.548494"
latest: "1.0--h503566f_4"
container_url: "https://biocontainers.pro/tools/mergenotcombined"
aliases:
 - "mergeNotCombined"
versions:
 - "1.0--h87f3376_2"
 - "1.0--hdbdd923_3"
 - "1.0--h503566f_4"
description: "shpc-registry automated BioContainers addition for mergenotcombined"
config: {"url": "https://biocontainers.pro/tools/mergenotcombined", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mergenotcombined", "latest": {"1.0--h503566f_4": "sha256:049e85d5f9fe46a67b7e0290b63348bdba428b45d571731143d1b369e1b12b5b"}, "tags": {"1.0--h87f3376_2": "sha256:db3e59a02f099381846ddd92659d9a408fb75e301f1b3c8ee3d6061092915582", "1.0--hdbdd923_3": "sha256:bc0569624281674e2a6a959204a393fe27b732acd853234b57726459f5ed14f6", "1.0--h503566f_4": "sha256:049e85d5f9fe46a67b7e0290b63348bdba428b45d571731143d1b369e1b12b5b"}, "docker": "quay.io/biocontainers/mergenotcombined", "aliases": {"mergeNotCombined": "/usr/local/bin/mergeNotCombined"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mergenotcombined.
shpc-registry automated BioContainers addition for mergenotcombined
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mergenotcombined
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mergenotcombined:1.0--h503566f_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mergenotcombined/1.0--h503566f_4
$ module help quay.io/biocontainers/mergenotcombined/1.0--h503566f_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mergenotcombined-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mergenotcombined-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mergenotcombined-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mergenotcombined-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mergenotcombined-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mergenotcombined-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mergeNotCombined

```bash
$ singularity exec <container> /usr/local/bin/mergeNotCombined
$ podman run --it --rm --entrypoint /usr/local/bin/mergeNotCombined   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeNotCombined   -v ${PWD} -w ${PWD} <container> -c " $@"
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