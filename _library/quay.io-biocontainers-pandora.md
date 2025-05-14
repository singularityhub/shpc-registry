---
layout: container
name:  "quay.io/biocontainers/pandora"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pandora/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pandora/container.yaml"
updated_at: "2025-05-14 03:32:40.720014"
latest: "0.9.2--h9948957_1"
container_url: "https://biocontainers.pro/tools/pandora"
aliases:
 - "pandora"
versions:
 - "0.9.1--h9f5acd7_1"
 - "0.9.1--h4ac6f70_2"
 - "0.9.2--h4ac6f70_0"
 - "0.9.2--h9948957_1"
description: "shpc-registry automated BioContainers addition for pandora"
config: {"url": "https://biocontainers.pro/tools/pandora", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pandora", "latest": {"0.9.2--h9948957_1": "sha256:55c636c46188a25353fd3a1fd3d406acb72a2f0d86032736ca476ba218affab8"}, "tags": {"0.9.1--h9f5acd7_1": "sha256:8af0e266701249c65ceb9607684c61b7595c1ad2d5e848eebe1437fc39e5e2f6", "0.9.1--h4ac6f70_2": "sha256:d714ce7f52e78aaa0cce3af62f64c4b0c8fbd8bfea1b5d6bbc68e20350f8e2e8", "0.9.2--h4ac6f70_0": "sha256:5bf5a89ec0b4be4fa4f43cf8632b6245c1b8ded6563e72764e5de300f931ddf0", "0.9.2--h9948957_1": "sha256:55c636c46188a25353fd3a1fd3d406acb72a2f0d86032736ca476ba218affab8"}, "docker": "quay.io/biocontainers/pandora", "aliases": {"pandora": "/usr/local/bin/pandora"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pandora.
shpc-registry automated BioContainers addition for pandora
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pandora
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pandora:0.9.2--h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pandora/0.9.2--h9948957_1
$ module help quay.io/biocontainers/pandora/0.9.2--h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pandora-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pandora-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pandora-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pandora-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pandora-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pandora-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandora

```bash
$ singularity exec <container> /usr/local/bin/pandora
$ podman run --it --rm --entrypoint /usr/local/bin/pandora   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandora   -v ${PWD} -w ${PWD} <container> -c " $@"
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