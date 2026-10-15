---
layout: container
name:  "quay.io/biocontainers/hapmeth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hapmeth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hapmeth/container.yaml"
updated_at: "2026-10-15 19:00:03.393229"
latest: "0.1.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/hapmeth"
aliases:
 - "hapmeth"
versions:
 - "0.1.0--hfa8f182_0"
description: "singularity registry hpc automated addition for hapmeth"
config: {"url": "https://biocontainers.pro/tools/hapmeth", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hapmeth", "latest": {"0.1.0--hfa8f182_0": "sha256:ab0c113d554c7f32b6ff19606f1106edbf7c2500a1d605cdff92eede0377966a"}, "tags": {"0.1.0--hfa8f182_0": "sha256:ab0c113d554c7f32b6ff19606f1106edbf7c2500a1d605cdff92eede0377966a"}, "docker": "quay.io/biocontainers/hapmeth", "aliases": {"hapmeth": "/usr/local/bin/hapmeth"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hapmeth.
singularity registry hpc automated addition for hapmeth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hapmeth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hapmeth:0.1.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hapmeth/0.1.0--hfa8f182_0
$ module help quay.io/biocontainers/hapmeth/0.1.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hapmeth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hapmeth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hapmeth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hapmeth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hapmeth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hapmeth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hapmeth

```bash
$ singularity exec <container> /usr/local/bin/hapmeth
$ podman run --it --rm --entrypoint /usr/local/bin/hapmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapmeth   -v ${PWD} -w ${PWD} <container> -c " $@"
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