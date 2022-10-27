---
layout: container
name:  "quay.io/biocontainers/tombo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tombo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tombo/container.yaml"
updated_at: "2022-10-27 00:37:47.039972"
latest: "1.0--py27_0"
container_url: "https://biocontainers.pro/tools/tombo"
aliases:
 - "graphmap"
 - "tombo"
versions:
 - "1.0--py27_0"
description: "shpc-registry automated BioContainers addition for tombo"
config: {"url": "https://biocontainers.pro/tools/tombo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tombo", "latest": {"1.0--py27_0": "sha256:6f93d035e4d3bdd641e0b7e3070dcbce909ea115befa72af6f9c0b47d34fabdb"}, "tags": {"1.0--py27_0": "sha256:6f93d035e4d3bdd641e0b7e3070dcbce909ea115befa72af6f9c0b47d34fabdb"}, "docker": "quay.io/biocontainers/tombo", "aliases": {"graphmap": "/usr/local/bin/graphmap", "tombo": "/usr/local/bin/tombo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tombo.
shpc-registry automated BioContainers addition for tombo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tombo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tombo:1.0--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tombo/1.0--py27_0
$ module help quay.io/biocontainers/tombo/1.0--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tombo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tombo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tombo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tombo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tombo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tombo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphmap

```bash
$ singularity exec <container> /usr/local/bin/graphmap
$ podman run --it --rm --entrypoint /usr/local/bin/graphmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tombo

```bash
$ singularity exec <container> /usr/local/bin/tombo
$ podman run --it --rm --entrypoint /usr/local/bin/tombo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tombo   -v ${PWD} -w ${PWD} <container> -c " $@"
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