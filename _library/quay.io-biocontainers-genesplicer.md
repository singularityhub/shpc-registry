---
layout: container
name:  "quay.io/biocontainers/genesplicer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genesplicer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genesplicer/container.yaml"
updated_at: "2025-10-21 03:11:12.004763"
latest: "1.0--1"
container_url: "https://biocontainers.pro/tools/genesplicer"
aliases:
 - "genesplicer"
versions:
 - "1.0--1"
description: "shpc-registry automated BioContainers addition for genesplicer"
config: {"url": "https://biocontainers.pro/tools/genesplicer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genesplicer", "latest": {"1.0--1": "sha256:bcccde967f89034cbf9d6cbe906fa7bc54c0ebe3f035212c14c0fa538b0974f6"}, "tags": {"1.0--1": "sha256:bcccde967f89034cbf9d6cbe906fa7bc54c0ebe3f035212c14c0fa538b0974f6"}, "docker": "quay.io/biocontainers/genesplicer", "aliases": {"genesplicer": "/usr/local/bin/genesplicer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genesplicer.
shpc-registry automated BioContainers addition for genesplicer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genesplicer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genesplicer:1.0--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genesplicer/1.0--1
$ module help quay.io/biocontainers/genesplicer/1.0--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genesplicer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genesplicer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genesplicer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genesplicer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genesplicer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genesplicer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genesplicer

```bash
$ singularity exec <container> /usr/local/bin/genesplicer
$ podman run --it --rm --entrypoint /usr/local/bin/genesplicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genesplicer   -v ${PWD} -w ${PWD} <container> -c " $@"
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