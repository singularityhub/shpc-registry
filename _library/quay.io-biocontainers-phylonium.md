---
layout: container
name:  "quay.io/biocontainers/phylonium"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylonium/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylonium/container.yaml"
updated_at: "2026-03-05 04:18:09.324630"
latest: "1.7--hde5307d_0"
container_url: "https://biocontainers.pro/tools/phylonium"
aliases:
 - "phylonium"
versions:
 - "1.7--hde5307d_0"
description: "singularity registry hpc automated addition for phylonium"
config: {"url": "https://biocontainers.pro/tools/phylonium", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phylonium", "latest": {"1.7--hde5307d_0": "sha256:6757b05d48fc58fee90f553f5cf69e86d98e46287a781e37e0b6c3472161d1f4"}, "tags": {"1.7--hde5307d_0": "sha256:6757b05d48fc58fee90f553f5cf69e86d98e46287a781e37e0b6c3472161d1f4"}, "docker": "quay.io/biocontainers/phylonium", "aliases": {"phylonium": "/usr/local/bin/phylonium"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylonium.
singularity registry hpc automated addition for phylonium
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylonium
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylonium:1.7--hde5307d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylonium/1.7--hde5307d_0
$ module help quay.io/biocontainers/phylonium/1.7--hde5307d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylonium-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylonium-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylonium-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylonium-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylonium-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylonium-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phylonium

```bash
$ singularity exec <container> /usr/local/bin/phylonium
$ podman run --it --rm --entrypoint /usr/local/bin/phylonium   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylonium   -v ${PWD} -w ${PWD} <container> -c " $@"
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