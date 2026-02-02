---
layout: container
name:  "quay.io/biocontainers/portello"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/portello/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/portello/container.yaml"
updated_at: "2026-02-02 12:53:13.785818"
latest: "0.7.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/portello"
aliases:
 - "portello"
versions:
 - "0.6.1--h9ee0642_0"
 - "0.7.0--h9ee0642_0"
description: "singularity registry hpc automated addition for portello"
config: {"url": "https://biocontainers.pro/tools/portello", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for portello", "latest": {"0.7.0--h9ee0642_0": "sha256:c3ef615a6debbc4a7cdc2cb2e694dbf9d845971407c4876e2407970c0a94c3bb"}, "tags": {"0.6.1--h9ee0642_0": "sha256:def24ca1ee5438abf60cd1918e373231730242dc54cb5f509e52c6030a81e656", "0.7.0--h9ee0642_0": "sha256:c3ef615a6debbc4a7cdc2cb2e694dbf9d845971407c4876e2407970c0a94c3bb"}, "docker": "quay.io/biocontainers/portello", "aliases": {"portello": "/usr/local/bin/portello"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/portello.
singularity registry hpc automated addition for portello
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/portello
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/portello:0.7.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/portello/0.7.0--h9ee0642_0
$ module help quay.io/biocontainers/portello/0.7.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### portello-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### portello-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### portello-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### portello-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### portello-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### portello-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### portello

```bash
$ singularity exec <container> /usr/local/bin/portello
$ podman run --it --rm --entrypoint /usr/local/bin/portello   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/portello   -v ${PWD} -w ${PWD} <container> -c " $@"
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