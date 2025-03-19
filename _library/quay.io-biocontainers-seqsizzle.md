---
layout: container
name:  "quay.io/biocontainers/seqsizzle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqsizzle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqsizzle/container.yaml"
updated_at: "2025-03-19 03:38:25.511284"
latest: "0.1.5--h790517f_1"
container_url: "https://biocontainers.pro/tools/seqsizzle"
aliases:
 - "seqsizzle"
versions:
 - "0.1.4--h8bd2d3b_0"
 - "0.1.5--h790517f_1"
description: "singularity registry hpc automated addition for seqsizzle"
config: {"url": "https://biocontainers.pro/tools/seqsizzle", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seqsizzle", "latest": {"0.1.5--h790517f_1": "sha256:e2efaf873809abd976ec09a5dc7e82fc3adcbfebf659be3cd332d8658b5ee868"}, "tags": {"0.1.4--h8bd2d3b_0": "sha256:7e2c45fbcf4d6059307b8e16c78d5a6959da1e40f28cdaae2ab3a650ea49d931", "0.1.5--h790517f_1": "sha256:e2efaf873809abd976ec09a5dc7e82fc3adcbfebf659be3cd332d8658b5ee868"}, "docker": "quay.io/biocontainers/seqsizzle", "aliases": {"seqsizzle": "/usr/local/bin/seqsizzle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqsizzle.
singularity registry hpc automated addition for seqsizzle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqsizzle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqsizzle:0.1.5--h790517f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqsizzle/0.1.5--h790517f_1
$ module help quay.io/biocontainers/seqsizzle/0.1.5--h790517f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqsizzle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqsizzle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqsizzle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqsizzle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqsizzle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqsizzle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqsizzle

```bash
$ singularity exec <container> /usr/local/bin/seqsizzle
$ podman run --it --rm --entrypoint /usr/local/bin/seqsizzle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqsizzle   -v ${PWD} -w ${PWD} <container> -c " $@"
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