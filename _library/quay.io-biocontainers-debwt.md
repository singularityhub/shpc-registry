---
layout: container
name:  "quay.io/biocontainers/debwt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/debwt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/debwt/container.yaml"
updated_at: "2024-02-03 02:42:40.578790"
latest: "1.0.1--he4a0461_7"
container_url: "https://biocontainers.pro/tools/debwt"
aliases:
 - "deBWT"
versions:
 - "1.0.1--h7132678_5"
 - "1.0.1--he4a0461_7"
description: "shpc-registry automated BioContainers addition for debwt"
config: {"url": "https://biocontainers.pro/tools/debwt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for debwt", "latest": {"1.0.1--he4a0461_7": "sha256:4079340c9e726e9f5758634be6985e063bb9442b30879179abf5580b9889d577"}, "tags": {"1.0.1--h7132678_5": "sha256:bae1b7a22194b702a6a9440f245664a5e6073edfc560c9deb81e457d16edfaf8", "1.0.1--he4a0461_7": "sha256:4079340c9e726e9f5758634be6985e063bb9442b30879179abf5580b9889d577"}, "docker": "quay.io/biocontainers/debwt", "aliases": {"deBWT": "/usr/local/bin/deBWT"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/debwt.
shpc-registry automated BioContainers addition for debwt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/debwt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/debwt:1.0.1--he4a0461_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/debwt/1.0.1--he4a0461_7
$ module help quay.io/biocontainers/debwt/1.0.1--he4a0461_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### debwt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### debwt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### debwt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### debwt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### debwt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### debwt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deBWT

```bash
$ singularity exec <container> /usr/local/bin/deBWT
$ podman run --it --rm --entrypoint /usr/local/bin/deBWT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deBWT   -v ${PWD} -w ${PWD} <container> -c " $@"
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