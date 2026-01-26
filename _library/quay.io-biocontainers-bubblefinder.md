---
layout: container
name:  "quay.io/biocontainers/bubblefinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bubblefinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bubblefinder/container.yaml"
updated_at: "2026-01-26 04:25:24.314512"
latest: "1.0.3--h503566f_0"
container_url: "https://biocontainers.pro/tools/bubblefinder"
aliases:
 - "BubbleFinder"
 - "snarls_bf"
versions:
 - "1.0.3--h503566f_0"
description: "singularity registry hpc automated addition for bubblefinder"
config: {"url": "https://biocontainers.pro/tools/bubblefinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bubblefinder", "latest": {"1.0.3--h503566f_0": "sha256:3bafccf2c2c3b7b667bf56105b6323058fbd5da9969fa31e33e8c7ec934c9487"}, "tags": {"1.0.3--h503566f_0": "sha256:3bafccf2c2c3b7b667bf56105b6323058fbd5da9969fa31e33e8c7ec934c9487"}, "docker": "quay.io/biocontainers/bubblefinder", "aliases": {"BubbleFinder": "/usr/local/bin/BubbleFinder", "snarls_bf": "/usr/local/bin/snarls_bf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bubblefinder.
singularity registry hpc automated addition for bubblefinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bubblefinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bubblefinder:1.0.3--h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bubblefinder/1.0.3--h503566f_0
$ module help quay.io/biocontainers/bubblefinder/1.0.3--h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bubblefinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bubblefinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bubblefinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bubblefinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bubblefinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bubblefinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BubbleFinder

```bash
$ singularity exec <container> /usr/local/bin/BubbleFinder
$ podman run --it --rm --entrypoint /usr/local/bin/BubbleFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BubbleFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snarls_bf

```bash
$ singularity exec <container> /usr/local/bin/snarls_bf
$ podman run --it --rm --entrypoint /usr/local/bin/snarls_bf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snarls_bf   -v ${PWD} -w ${PWD} <container> -c " $@"
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