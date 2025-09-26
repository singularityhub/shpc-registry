---
layout: container
name:  "quay.io/biocontainers/maelstrom-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maelstrom-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maelstrom-core/container.yaml"
updated_at: "2025-09-26 03:50:15.348420"
latest: "0.1.1--h9d3141d_2"
container_url: "https://biocontainers.pro/tools/maelstrom-core"
aliases:
 - "maelstrom-core"
versions:
 - "0.1.1--h92d785c_0"
 - "0.1.1--h9d3141d_2"
description: "singularity registry hpc automated addition for maelstrom-core"
config: {"url": "https://biocontainers.pro/tools/maelstrom-core", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for maelstrom-core", "latest": {"0.1.1--h9d3141d_2": "sha256:cf5d3c83d8d12c3336fdd65c5b1ee4b61f0ef3f33a6b5a44ca373fd653038e68"}, "tags": {"0.1.1--h92d785c_0": "sha256:2bc60264f4bf2695d45e880bed4d5ca4c7a7e9a22ce4d1faccb8bf97f6f38dee", "0.1.1--h9d3141d_2": "sha256:cf5d3c83d8d12c3336fdd65c5b1ee4b61f0ef3f33a6b5a44ca373fd653038e68"}, "docker": "quay.io/biocontainers/maelstrom-core", "aliases": {"maelstrom-core": "/usr/local/bin/maelstrom-core"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maelstrom-core.
singularity registry hpc automated addition for maelstrom-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maelstrom-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maelstrom-core:0.1.1--h9d3141d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maelstrom-core/0.1.1--h9d3141d_2
$ module help quay.io/biocontainers/maelstrom-core/0.1.1--h9d3141d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maelstrom-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maelstrom-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maelstrom-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maelstrom-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maelstrom-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maelstrom-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### maelstrom-core

```bash
$ singularity exec <container> /usr/local/bin/maelstrom-core
$ podman run --it --rm --entrypoint /usr/local/bin/maelstrom-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maelstrom-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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