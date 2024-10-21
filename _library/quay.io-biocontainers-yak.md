---
layout: container
name:  "quay.io/biocontainers/yak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yak/container.yaml"
updated_at: "2024-10-21 03:25:51.919539"
latest: "0.1--he4a0461_5"
container_url: "https://biocontainers.pro/tools/yak"
aliases:
 - "yak"
versions:
 - "0.1--h7132678_2"
 - "0.1--he4a0461_4"
 - "0.1--he4a0461_5"
description: "shpc-registry automated BioContainers addition for yak"
config: {"url": "https://biocontainers.pro/tools/yak", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yak", "latest": {"0.1--he4a0461_5": "sha256:6b7f4382392bc20dceb1208e700ce8b384ae6822c6fad66c40eb31b305792c97"}, "tags": {"0.1--h7132678_2": "sha256:a1e9fb7c97e4e402fbd60e77758f03ef471cac46c6b7c9c7aa99fc5d4f802b3f", "0.1--he4a0461_4": "sha256:e0ccc68a12843e0d7f80e3951bca0ed7adbea703f4ea211691fbabde09698755", "0.1--he4a0461_5": "sha256:6b7f4382392bc20dceb1208e700ce8b384ae6822c6fad66c40eb31b305792c97"}, "docker": "quay.io/biocontainers/yak", "aliases": {"yak": "/usr/local/bin/yak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yak.
shpc-registry automated BioContainers addition for yak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yak:0.1--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yak/0.1--he4a0461_5
$ module help quay.io/biocontainers/yak/0.1--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yak

```bash
$ singularity exec <container> /usr/local/bin/yak
$ podman run --it --rm --entrypoint /usr/local/bin/yak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yak   -v ${PWD} -w ${PWD} <container> -c " $@"
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