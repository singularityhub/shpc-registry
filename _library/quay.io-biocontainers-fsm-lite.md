---
layout: container
name:  "quay.io/biocontainers/fsm-lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fsm-lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fsm-lite/container.yaml"
updated_at: "2023-06-26 03:46:23.083256"
latest: "1.0--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/fsm-lite"
aliases:
 - "fsm-lite"
versions:
 - "1.0--h9f5acd7_3"
 - "1.0--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for fsm-lite"
config: {"url": "https://biocontainers.pro/tools/fsm-lite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fsm-lite", "latest": {"1.0--h4ac6f70_5": "sha256:484e7826547b60115d8512874d487f184be9a777cacc0df06ac596e115b88734"}, "tags": {"1.0--h9f5acd7_3": "sha256:8ed52c99ac8db024429e3ba47761f42f6df752713efc22a1eb45c609b04be72c", "1.0--h4ac6f70_5": "sha256:484e7826547b60115d8512874d487f184be9a777cacc0df06ac596e115b88734"}, "docker": "quay.io/biocontainers/fsm-lite", "aliases": {"fsm-lite": "/usr/local/bin/fsm-lite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fsm-lite.
shpc-registry automated BioContainers addition for fsm-lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fsm-lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fsm-lite:1.0--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fsm-lite/1.0--h4ac6f70_5
$ module help quay.io/biocontainers/fsm-lite/1.0--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fsm-lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fsm-lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fsm-lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fsm-lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fsm-lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fsm-lite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fsm-lite

```bash
$ singularity exec <container> /usr/local/bin/fsm-lite
$ podman run --it --rm --entrypoint /usr/local/bin/fsm-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsm-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
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