---
layout: container
name:  "quay.io/biocontainers/synthbar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/synthbar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/synthbar/container.yaml"
updated_at: "2026-07-01 07:10:44.279718"
latest: "0.2.0--h118bc1c_0"
container_url: "https://biocontainers.pro/tools/synthbar"
aliases:
 - "synthbar"
versions:
 - "0.2.0--h118bc1c_0"
description: "singularity registry hpc automated addition for synthbar"
config: {"url": "https://biocontainers.pro/tools/synthbar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for synthbar", "latest": {"0.2.0--h118bc1c_0": "sha256:f95e30c94a3baed0616064f184863bcd15ae9c5727205edd830bf468b78a8639"}, "tags": {"0.2.0--h118bc1c_0": "sha256:f95e30c94a3baed0616064f184863bcd15ae9c5727205edd830bf468b78a8639"}, "docker": "quay.io/biocontainers/synthbar", "aliases": {"synthbar": "/usr/local/bin/synthbar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/synthbar.
singularity registry hpc automated addition for synthbar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/synthbar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/synthbar:0.2.0--h118bc1c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/synthbar/0.2.0--h118bc1c_0
$ module help quay.io/biocontainers/synthbar/0.2.0--h118bc1c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### synthbar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### synthbar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### synthbar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### synthbar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### synthbar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### synthbar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### synthbar

```bash
$ singularity exec <container> /usr/local/bin/synthbar
$ podman run --it --rm --entrypoint /usr/local/bin/synthbar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/synthbar   -v ${PWD} -w ${PWD} <container> -c " $@"
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