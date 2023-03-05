---
layout: container
name:  "quay.io/biocontainers/dxua"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dxua/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dxua/container.yaml"
updated_at: "2023-03-05 03:24:19.872924"
latest: "1.5.31--0"
container_url: "https://biocontainers.pro/tools/dxua"
aliases:
 - "dxua"
versions:
 - "1.5.31--0"
description: "shpc-registry automated BioContainers addition for dxua"
config: {"url": "https://biocontainers.pro/tools/dxua", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dxua", "latest": {"1.5.31--0": "sha256:b8ca030a113e14b8710905c3fb49507d7f901b8e5d70b7545f796ac23158f522"}, "tags": {"1.5.31--0": "sha256:b8ca030a113e14b8710905c3fb49507d7f901b8e5d70b7545f796ac23158f522"}, "docker": "quay.io/biocontainers/dxua", "aliases": {"dxua": "/usr/local/bin/dxua"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dxua.
shpc-registry automated BioContainers addition for dxua
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dxua
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dxua:1.5.31--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dxua/1.5.31--0
$ module help quay.io/biocontainers/dxua/1.5.31--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dxua-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dxua-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dxua-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dxua-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dxua-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dxua-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dxua

```bash
$ singularity exec <container> /usr/local/bin/dxua
$ podman run --it --rm --entrypoint /usr/local/bin/dxua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dxua   -v ${PWD} -w ${PWD} <container> -c " $@"
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