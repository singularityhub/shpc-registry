---
layout: container
name:  "quay.io/biocontainers/je-suite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/je-suite/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/je-suite/container.yaml"
updated_at: "2022-10-27 00:26:24.892010"
latest: "2.0.RC--0"
container_url: "https://biocontainers.pro/tools/je-suite"
aliases:
 - "je"
versions:
 - "2.0.RC--0"
description: "shpc-registry automated BioContainers addition for je-suite"
config: {"url": "https://biocontainers.pro/tools/je-suite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for je-suite", "latest": {"2.0.RC--0": "sha256:85b39d0c82192d39396d8ae1626c3a03a3de3c77522aa00f0b4b3d9a57ad9b8d"}, "tags": {"2.0.RC--0": "sha256:85b39d0c82192d39396d8ae1626c3a03a3de3c77522aa00f0b4b3d9a57ad9b8d"}, "docker": "quay.io/biocontainers/je-suite", "aliases": {"je": "/usr/local/bin/je"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/je-suite.
shpc-registry automated BioContainers addition for je-suite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/je-suite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/je-suite:2.0.RC--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/je-suite/2.0.RC--0
$ module help quay.io/biocontainers/je-suite/2.0.RC--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### je-suite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### je-suite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### je-suite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### je-suite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### je-suite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### je-suite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### je

```bash
$ singularity exec <container> /usr/local/bin/je
$ podman run --it --rm --entrypoint /usr/local/bin/je   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/je   -v ${PWD} -w ${PWD} <container> -c " $@"
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