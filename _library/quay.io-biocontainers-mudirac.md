---
layout: container
name:  "quay.io/biocontainers/mudirac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mudirac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mudirac/container.yaml"
updated_at: "2025-10-29 03:31:28.845199"
latest: "1.0.1"
container_url: "https://biocontainers.pro/tools/mudirac"
aliases:
 - "mudirac"
versions:
 - "1.0.1"
description: "singularity registry hpc automated addition for mudirac"
config: {"url": "https://biocontainers.pro/tools/mudirac", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mudirac", "latest": {"1.0.1": "sha256:e0d133ffa552647c6eacc8ecce8251d1540d256af3af8914de5a1011a4f9cd03"}, "tags": {"1.0.1": "sha256:e0d133ffa552647c6eacc8ecce8251d1540d256af3af8914de5a1011a4f9cd03"}, "docker": "quay.io/biocontainers/mudirac", "aliases": {"mudirac": "/usr/local/bin/mudirac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mudirac.
singularity registry hpc automated addition for mudirac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mudirac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mudirac:1.0.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mudirac/1.0.1
$ module help quay.io/biocontainers/mudirac/1.0.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mudirac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mudirac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mudirac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mudirac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mudirac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mudirac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mudirac

```bash
$ singularity exec <container> /usr/local/bin/mudirac
$ podman run --it --rm --entrypoint /usr/local/bin/mudirac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mudirac   -v ${PWD} -w ${PWD} <container> -c " $@"
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