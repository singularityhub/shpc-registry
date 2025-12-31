---
layout: container
name:  "quay.io/biocontainers/bwtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwtk/container.yaml"
updated_at: "2025-12-31 04:23:43.797077"
latest: "1.8.1--h9990f68_0"
container_url: "https://biocontainers.pro/tools/bwtk"
aliases:
 - "bwtk"
versions:
 - "1.8.1--h9990f68_0"
description: "singularity registry hpc automated addition for bwtk"
config: {"url": "https://biocontainers.pro/tools/bwtk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bwtk", "latest": {"1.8.1--h9990f68_0": "sha256:0fa18ce25d0b93f877eb02359b616404abaa8319eb900939f87af0d6dc5c3a93"}, "tags": {"1.8.1--h9990f68_0": "sha256:0fa18ce25d0b93f877eb02359b616404abaa8319eb900939f87af0d6dc5c3a93"}, "docker": "quay.io/biocontainers/bwtk", "aliases": {"bwtk": "/usr/local/bin/bwtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwtk.
singularity registry hpc automated addition for bwtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwtk:1.8.1--h9990f68_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwtk/1.8.1--h9990f68_0
$ module help quay.io/biocontainers/bwtk/1.8.1--h9990f68_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwtk

```bash
$ singularity exec <container> /usr/local/bin/bwtk
$ podman run --it --rm --entrypoint /usr/local/bin/bwtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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