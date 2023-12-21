---
layout: container
name:  "quay.io/biocontainers/ghm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ghm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ghm/container.yaml"
updated_at: "2023-12-21 03:13:08.824953"
latest: "3.1--h7132678_5"
container_url: "https://biocontainers.pro/tools/ghm"
aliases:
 - "ghm"
versions:
 - "3.1--h7132678_5"
description: "shpc-registry automated BioContainers addition for ghm"
config: {"url": "https://biocontainers.pro/tools/ghm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ghm", "latest": {"3.1--h7132678_5": "sha256:dd8b5633b0aee3fbd474b3b9833446424faefbd5048898d76b467ee47c5f1239"}, "tags": {"3.1--h7132678_5": "sha256:dd8b5633b0aee3fbd474b3b9833446424faefbd5048898d76b467ee47c5f1239"}, "docker": "quay.io/biocontainers/ghm", "aliases": {"ghm": "/usr/local/bin/ghm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ghm.
shpc-registry automated BioContainers addition for ghm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ghm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ghm:3.1--h7132678_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ghm/3.1--h7132678_5
$ module help quay.io/biocontainers/ghm/3.1--h7132678_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ghm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ghm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ghm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ghm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ghm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ghm

```bash
$ singularity exec <container> /usr/local/bin/ghm
$ podman run --it --rm --entrypoint /usr/local/bin/ghm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghm   -v ${PWD} -w ${PWD} <container> -c " $@"
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