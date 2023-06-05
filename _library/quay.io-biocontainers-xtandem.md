---
layout: container
name:  "quay.io/biocontainers/xtandem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtandem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xtandem/container.yaml"
updated_at: "2023-06-05 02:58:05.842540"
latest: "15.12.15.2--h7e02a51_8"
container_url: "https://biocontainers.pro/tools/xtandem"
aliases:
 - "xtandem"
versions:
 - "15.12.15.2--h072c6ed_6"
 - "15.12.15.2--h7e02a51_8"
description: "shpc-registry automated BioContainers addition for xtandem"
config: {"url": "https://biocontainers.pro/tools/xtandem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xtandem", "latest": {"15.12.15.2--h7e02a51_8": "sha256:2f0afe420396eb3289afabcc5ab7d5c90c14c784ff8e81f880f503092b5967d3"}, "tags": {"15.12.15.2--h072c6ed_6": "sha256:881ed790dc6ea4dcc09c0a30d57645624e5a67b737d2e025e9a3e3cab99ee431", "15.12.15.2--h7e02a51_8": "sha256:2f0afe420396eb3289afabcc5ab7d5c90c14c784ff8e81f880f503092b5967d3"}, "docker": "quay.io/biocontainers/xtandem", "aliases": {"xtandem": "/usr/local/bin/xtandem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtandem.
shpc-registry automated BioContainers addition for xtandem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtandem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtandem:15.12.15.2--h7e02a51_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtandem/15.12.15.2--h7e02a51_8
$ module help quay.io/biocontainers/xtandem/15.12.15.2--h7e02a51_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtandem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtandem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtandem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtandem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtandem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtandem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xtandem

```bash
$ singularity exec <container> /usr/local/bin/xtandem
$ podman run --it --rm --entrypoint /usr/local/bin/xtandem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtandem   -v ${PWD} -w ${PWD} <container> -c " $@"
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