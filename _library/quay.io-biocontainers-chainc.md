---
layout: container
name:  "quay.io/biocontainers/chainc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chainc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chainc/container.yaml"
updated_at: "2026-08-28 14:15:17.000031"
latest: "0.0.1--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/chainc"
aliases:
 - "chainc"
versions:
 - "0.0.1--hab7d0fd_0"
description: "singularity registry hpc automated addition for chainc"
config: {"url": "https://biocontainers.pro/tools/chainc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chainc", "latest": {"0.0.1--hab7d0fd_0": "sha256:0ea5f06be1cf1fa24256c8b8b39cc2d7224a876e58268391e0901886f0e8c9c7"}, "tags": {"0.0.1--hab7d0fd_0": "sha256:0ea5f06be1cf1fa24256c8b8b39cc2d7224a876e58268391e0901886f0e8c9c7"}, "docker": "quay.io/biocontainers/chainc", "aliases": {"chainc": "/usr/local/bin/chainc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chainc.
singularity registry hpc automated addition for chainc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chainc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chainc:0.0.1--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chainc/0.0.1--hab7d0fd_0
$ module help quay.io/biocontainers/chainc/0.0.1--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chainc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chainc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chainc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chainc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chainc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chainc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chainc

```bash
$ singularity exec <container> /usr/local/bin/chainc
$ podman run --it --rm --entrypoint /usr/local/bin/chainc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chainc   -v ${PWD} -w ${PWD} <container> -c " $@"
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