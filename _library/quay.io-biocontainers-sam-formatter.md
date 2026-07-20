---
layout: container
name:  "quay.io/biocontainers/sam-formatter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sam-formatter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sam-formatter/container.yaml"
updated_at: "2026-07-20 06:27:11.644901"
latest: "1.2.0--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/sam-formatter"
aliases:
 - "sam-formatter"
versions:
 - "1.2.0--hab7d0fd_0"
description: "singularity registry hpc automated addition for sam-formatter"
config: {"url": "https://biocontainers.pro/tools/sam-formatter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sam-formatter", "latest": {"1.2.0--hab7d0fd_0": "sha256:6f76caad71109971ef74d08e8300ffcb0fb607004d4034f5211427ae2ef9fc26"}, "tags": {"1.2.0--hab7d0fd_0": "sha256:6f76caad71109971ef74d08e8300ffcb0fb607004d4034f5211427ae2ef9fc26"}, "docker": "quay.io/biocontainers/sam-formatter", "aliases": {"sam-formatter": "/usr/local/bin/sam-formatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sam-formatter.
singularity registry hpc automated addition for sam-formatter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sam-formatter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sam-formatter:1.2.0--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sam-formatter/1.2.0--hab7d0fd_0
$ module help quay.io/biocontainers/sam-formatter/1.2.0--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sam-formatter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sam-formatter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sam-formatter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sam-formatter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sam-formatter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sam-formatter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sam-formatter

```bash
$ singularity exec <container> /usr/local/bin/sam-formatter
$ podman run --it --rm --entrypoint /usr/local/bin/sam-formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam-formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
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