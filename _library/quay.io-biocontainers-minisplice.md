---
layout: container
name:  "quay.io/biocontainers/minisplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minisplice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minisplice/container.yaml"
updated_at: "2025-10-04 03:27:34.084318"
latest: "0.4--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/minisplice"
aliases:
 - "minisplice"
versions:
 - "0.4--h577a1d6_0"
description: "singularity registry hpc automated addition for minisplice"
config: {"url": "https://biocontainers.pro/tools/minisplice", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for minisplice", "latest": {"0.4--h577a1d6_0": "sha256:86d994d8f59239685b32362379b0a539c7e7ce78b909ae59b3982acd409b3b37"}, "tags": {"0.4--h577a1d6_0": "sha256:86d994d8f59239685b32362379b0a539c7e7ce78b909ae59b3982acd409b3b37"}, "docker": "quay.io/biocontainers/minisplice", "aliases": {"minisplice": "/usr/local/bin/minisplice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minisplice.
singularity registry hpc automated addition for minisplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minisplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minisplice:0.4--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minisplice/0.4--h577a1d6_0
$ module help quay.io/biocontainers/minisplice/0.4--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minisplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minisplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minisplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minisplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minisplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minisplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minisplice

```bash
$ singularity exec <container> /usr/local/bin/minisplice
$ podman run --it --rm --entrypoint /usr/local/bin/minisplice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minisplice   -v ${PWD} -w ${PWD} <container> -c " $@"
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