---
layout: container
name:  "quay.io/biocontainers/gfatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfatk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfatk/container.yaml"
updated_at: "2026-10-11 08:58:56.642099"
latest: "0.6.1--hab7d0fd_1"
container_url: "https://biocontainers.pro/tools/gfatk"
aliases:
 - "gfatk"
versions:
 - "0.6.1--hab7d0fd_1"
description: "singularity registry hpc automated addition for gfatk"
config: {"url": "https://biocontainers.pro/tools/gfatk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfatk", "latest": {"0.6.1--hab7d0fd_1": "sha256:8f04a775b90f53410af7405e4e5229d989536c51f48a8a7d2bc4b9dd4e03ead8"}, "tags": {"0.6.1--hab7d0fd_1": "sha256:8f04a775b90f53410af7405e4e5229d989536c51f48a8a7d2bc4b9dd4e03ead8"}, "docker": "quay.io/biocontainers/gfatk", "aliases": {"gfatk": "/usr/local/bin/gfatk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfatk.
singularity registry hpc automated addition for gfatk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfatk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfatk:0.6.1--hab7d0fd_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfatk/0.6.1--hab7d0fd_1
$ module help quay.io/biocontainers/gfatk/0.6.1--hab7d0fd_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfatk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfatk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfatk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfatk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfatk

```bash
$ singularity exec <container> /usr/local/bin/gfatk
$ podman run --it --rm --entrypoint /usr/local/bin/gfatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfatk   -v ${PWD} -w ${PWD} <container> -c " $@"
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