---
layout: container
name:  "quay.io/biocontainers/groopm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/groopm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/groopm/container.yaml"
updated_at: "2022-10-27 00:18:28.640076"
latest: "0.3.4--py27_0"
container_url: "https://biocontainers.pro/tools/groopm"
aliases:
 - "bamFlags"
 - "bamm"
 - "groopm"
versions:
 - "0.3.4--py27_0"
description: "shpc-registry automated BioContainers addition for groopm"
config: {"url": "https://biocontainers.pro/tools/groopm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for groopm", "latest": {"0.3.4--py27_0": "sha256:4515ada6ab1fbf183ddd847e7549c2b5960fe5d7a8a7907fb60e713cd6d1102e"}, "tags": {"0.3.4--py27_0": "sha256:4515ada6ab1fbf183ddd847e7549c2b5960fe5d7a8a7907fb60e713cd6d1102e"}, "docker": "quay.io/biocontainers/groopm", "aliases": {"bamFlags": "/usr/local/bin/bamFlags", "bamm": "/usr/local/bin/bamm", "groopm": "/usr/local/bin/groopm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/groopm.
shpc-registry automated BioContainers addition for groopm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/groopm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/groopm:0.3.4--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/groopm/0.3.4--py27_0
$ module help quay.io/biocontainers/groopm/0.3.4--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### groopm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### groopm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### groopm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### groopm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### groopm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### groopm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamFlags

```bash
$ singularity exec <container> /usr/local/bin/bamFlags
$ podman run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamm

```bash
$ singularity exec <container> /usr/local/bin/bamm
$ podman run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groopm

```bash
$ singularity exec <container> /usr/local/bin/groopm
$ podman run --it --rm --entrypoint /usr/local/bin/groopm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groopm   -v ${PWD} -w ${PWD} <container> -c " $@"
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