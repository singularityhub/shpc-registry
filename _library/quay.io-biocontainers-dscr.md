---
layout: container
name:  "quay.io/biocontainers/dscr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dscr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dscr/container.yaml"
updated_at: "2022-10-27 00:51:26.773600"
latest: "2014.12.17--boost1.60_1"
container_url: "https://biocontainers.pro/tools/dscr"
aliases:
 - "dsrc"
versions:
 - "2014.12.17--boost1.60_1"
description: "shpc-registry automated BioContainers addition for dscr"
config: {"url": "https://biocontainers.pro/tools/dscr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dscr", "latest": {"2014.12.17--boost1.60_1": "sha256:988bee0765e17cb85c3ee1cedb922439e47191fdacd64cb51d7a638e05b8befb"}, "tags": {"2014.12.17--boost1.60_1": "sha256:988bee0765e17cb85c3ee1cedb922439e47191fdacd64cb51d7a638e05b8befb"}, "docker": "quay.io/biocontainers/dscr", "aliases": {"dsrc": "/usr/local/bin/dsrc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dscr.
shpc-registry automated BioContainers addition for dscr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dscr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dscr:2014.12.17--boost1.60_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dscr/2014.12.17--boost1.60_1
$ module help quay.io/biocontainers/dscr/2014.12.17--boost1.60_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dscr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dscr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dscr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dscr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dscr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dscr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dsrc

```bash
$ singularity exec <container> /usr/local/bin/dsrc
$ podman run --it --rm --entrypoint /usr/local/bin/dsrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsrc   -v ${PWD} -w ${PWD} <container> -c " $@"
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