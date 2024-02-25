---
layout: container
name:  "quay.io/biocontainers/hr2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hr2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hr2/container.yaml"
updated_at: "2024-02-25 02:43:39.120666"
latest: "1.04--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/hr2"
aliases:
 - "HR2.exe"
versions:
 - "1.04--h9f5acd7_3"
 - "1.04--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for hr2"
config: {"url": "https://biocontainers.pro/tools/hr2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hr2", "latest": {"1.04--h4ac6f70_5": "sha256:1195925d26c904a386d24db41b70531098c3b422ad63c6a6b6dc6da5e73c75de"}, "tags": {"1.04--h9f5acd7_3": "sha256:2fb668ba0461272839caae7016c83a25e2a69b2d3388f3c00b5b952d59aa8a7b", "1.04--h4ac6f70_5": "sha256:1195925d26c904a386d24db41b70531098c3b422ad63c6a6b6dc6da5e73c75de"}, "docker": "quay.io/biocontainers/hr2", "aliases": {"HR2.exe": "/usr/local/bin/HR2.exe"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hr2.
shpc-registry automated BioContainers addition for hr2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hr2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hr2:1.04--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hr2/1.04--h4ac6f70_5
$ module help quay.io/biocontainers/hr2/1.04--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hr2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hr2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hr2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hr2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hr2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hr2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HR2.exe

```bash
$ singularity exec <container> /usr/local/bin/HR2.exe
$ podman run --it --rm --entrypoint /usr/local/bin/HR2.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HR2.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
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