---
layout: container
name:  "quay.io/biocontainers/namfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/namfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/namfinder/container.yaml"
updated_at: "2023-12-02 02:27:41.493597"
latest: "0.1.3--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/namfinder"
aliases:
 - "namfinder"
versions:
 - "0.1.3--h4ac6f70_0"
description: "singularity registry hpc automated addition for namfinder"
config: {"url": "https://biocontainers.pro/tools/namfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for namfinder", "latest": {"0.1.3--h4ac6f70_0": "sha256:722923cbd6b5d4e78c547058f3260693c0d81bca32ac4034acacd2d9a05ee386"}, "tags": {"0.1.3--h4ac6f70_0": "sha256:722923cbd6b5d4e78c547058f3260693c0d81bca32ac4034acacd2d9a05ee386"}, "docker": "quay.io/biocontainers/namfinder", "aliases": {"namfinder": "/usr/local/bin/namfinder"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/namfinder.
singularity registry hpc automated addition for namfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/namfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/namfinder:0.1.3--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/namfinder/0.1.3--h4ac6f70_0
$ module help quay.io/biocontainers/namfinder/0.1.3--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### namfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### namfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### namfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### namfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### namfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### namfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### namfinder

```bash
$ singularity exec <container> /usr/local/bin/namfinder
$ podman run --it --rm --entrypoint /usr/local/bin/namfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/namfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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