---
layout: container
name:  "quay.io/biocontainers/restrander"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/restrander/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/restrander/container.yaml"
updated_at: "2026-08-27 13:11:08.880161"
latest: "1.1.3--h3be2455_1"
container_url: "https://biocontainers.pro/tools/restrander"
aliases:
 - "restrander"
versions:
 - "1.1.3--h3be2455_1"
description: "singularity registry hpc automated addition for restrander"
config: {"url": "https://biocontainers.pro/tools/restrander", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for restrander", "latest": {"1.1.3--h3be2455_1": "sha256:5a6a18e5d5be44dc182821ce98e5f3cc0a36fa7e3d0b5c843214a27ae1fef57e"}, "tags": {"1.1.3--h3be2455_1": "sha256:5a6a18e5d5be44dc182821ce98e5f3cc0a36fa7e3d0b5c843214a27ae1fef57e"}, "docker": "quay.io/biocontainers/restrander", "aliases": {"restrander": "/usr/local/bin/restrander"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/restrander.
singularity registry hpc automated addition for restrander
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/restrander
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/restrander:1.1.3--h3be2455_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/restrander/1.1.3--h3be2455_1
$ module help quay.io/biocontainers/restrander/1.1.3--h3be2455_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### restrander-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### restrander-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### restrander-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### restrander-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### restrander-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### restrander-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### restrander

```bash
$ singularity exec <container> /usr/local/bin/restrander
$ podman run --it --rm --entrypoint /usr/local/bin/restrander   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/restrander   -v ${PWD} -w ${PWD} <container> -c " $@"
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