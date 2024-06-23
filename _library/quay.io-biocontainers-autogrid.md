---
layout: container
name:  "quay.io/biocontainers/autogrid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autogrid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autogrid/container.yaml"
updated_at: "2024-06-23 02:48:49.911503"
latest: "4.2.6--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/autogrid"
aliases:
 - "autogrid4"
versions:
 - "4.2.6--h9f5acd7_1"
 - "4.2.6--h4ac6f70_3"
description: "singularity registry hpc automated addition for autogrid"
config: {"url": "https://biocontainers.pro/tools/autogrid", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for autogrid", "latest": {"4.2.6--h4ac6f70_3": "sha256:b579ddcf2bd976846802770fca3d6f6e454f97fbdbd0a442b5e4c3e6f44f3abf"}, "tags": {"4.2.6--h9f5acd7_1": "sha256:d596f8bbcd037ca092e5df0ab4c2b1cddf58d680a0d58704221175a7aaff56c4", "4.2.6--h4ac6f70_3": "sha256:b579ddcf2bd976846802770fca3d6f6e454f97fbdbd0a442b5e4c3e6f44f3abf"}, "docker": "quay.io/biocontainers/autogrid", "aliases": {"autogrid4": "/usr/local/bin/autogrid4"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autogrid.
singularity registry hpc automated addition for autogrid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autogrid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autogrid:4.2.6--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autogrid/4.2.6--h4ac6f70_3
$ module help quay.io/biocontainers/autogrid/4.2.6--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autogrid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autogrid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autogrid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autogrid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autogrid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autogrid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autogrid4

```bash
$ singularity exec <container> /usr/local/bin/autogrid4
$ podman run --it --rm --entrypoint /usr/local/bin/autogrid4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autogrid4   -v ${PWD} -w ${PWD} <container> -c " $@"
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