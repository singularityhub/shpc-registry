---
layout: container
name:  "quay.io/biocontainers/assembly-stats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/assembly-stats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/assembly-stats/container.yaml"
updated_at: "2024-11-06 03:29:34.633867"
latest: "1.0.1--h4ac6f70_8"
container_url: "https://biocontainers.pro/tools/assembly-stats"
aliases:
 - "assembly-stats"
versions:
 - "1.0.1--h9f5acd7_5"
 - "1.0.1--h4ac6f70_7"
 - "1.0.1--h4ac6f70_8"
description: "shpc-registry automated BioContainers addition for assembly-stats"
config: {"url": "https://biocontainers.pro/tools/assembly-stats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for assembly-stats", "latest": {"1.0.1--h4ac6f70_8": "sha256:eb83677fcf8d32105e191dc234c761e4fd8926ff9f51e0ac1954b758e7cd4e4b"}, "tags": {"1.0.1--h9f5acd7_5": "sha256:13419ab79fc4f9e10acd8c34c8e7ca1ed37dcffdaa6b6b8950ae5e2228209229", "1.0.1--h4ac6f70_7": "sha256:f25db878659d69d5ff3bd38691b595fd05723baddda76f0b63ffaa5ab1a3ea97", "1.0.1--h4ac6f70_8": "sha256:eb83677fcf8d32105e191dc234c761e4fd8926ff9f51e0ac1954b758e7cd4e4b"}, "docker": "quay.io/biocontainers/assembly-stats", "aliases": {"assembly-stats": "/usr/local/bin/assembly-stats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/assembly-stats.
shpc-registry automated BioContainers addition for assembly-stats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/assembly-stats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/assembly-stats:1.0.1--h4ac6f70_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/assembly-stats/1.0.1--h4ac6f70_8
$ module help quay.io/biocontainers/assembly-stats/1.0.1--h4ac6f70_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### assembly-stats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### assembly-stats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### assembly-stats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### assembly-stats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### assembly-stats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### assembly-stats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assembly-stats

```bash
$ singularity exec <container> /usr/local/bin/assembly-stats
$ podman run --it --rm --entrypoint /usr/local/bin/assembly-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assembly-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
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