---
layout: container
name:  "quay.io/biocontainers/aptardi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aptardi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/aptardi/container.yaml"
updated_at: "2022-10-27 00:21:47.799567"
latest: "1.4--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/aptardi"
aliases:
 - "aptardi"
versions:
 - "1.4--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for aptardi"
config: {"url": "https://biocontainers.pro/tools/aptardi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aptardi", "latest": {"1.4--pyh5e36f6f_0": "sha256:15679bc27b0c007c06045d1a422940555449995641741c3b0f7ec8ea8d3abcf8"}, "tags": {"1.4--pyh5e36f6f_0": "sha256:15679bc27b0c007c06045d1a422940555449995641741c3b0f7ec8ea8d3abcf8"}, "docker": "quay.io/biocontainers/aptardi", "aliases": {"aptardi": "/usr/local/bin/aptardi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aptardi.
shpc-registry automated BioContainers addition for aptardi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aptardi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aptardi:1.4--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aptardi/1.4--pyh5e36f6f_0
$ module help quay.io/biocontainers/aptardi/1.4--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aptardi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aptardi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aptardi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aptardi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aptardi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aptardi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aptardi

```bash
$ singularity exec <container> /usr/local/bin/aptardi
$ podman run --it --rm --entrypoint /usr/local/bin/aptardi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aptardi   -v ${PWD} -w ${PWD} <container> -c " $@"
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