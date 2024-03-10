---
layout: container
name:  "quay.io/biocontainers/mgems"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgems/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgems/container.yaml"
updated_at: "2024-03-10 03:00:13.832075"
latest: "1.3.1--h468198e_0"
container_url: "https://biocontainers.pro/tools/mgems"
aliases:
 - "mGEMS"
versions:
 - "1.3.1--h468198e_0"
description: "singularity registry hpc automated addition for mgems"
config: {"url": "https://biocontainers.pro/tools/mgems", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mgems", "latest": {"1.3.1--h468198e_0": "sha256:eaa440b4eb637ac9f97beda227291fb6272ae36d56b75a8b1b77211889d6b296"}, "tags": {"1.3.1--h468198e_0": "sha256:eaa440b4eb637ac9f97beda227291fb6272ae36d56b75a8b1b77211889d6b296"}, "docker": "quay.io/biocontainers/mgems", "aliases": {"mGEMS": "/usr/local/bin/mGEMS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgems.
singularity registry hpc automated addition for mgems
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgems
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgems:1.3.1--h468198e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgems/1.3.1--h468198e_0
$ module help quay.io/biocontainers/mgems/1.3.1--h468198e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgems-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgems-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgems-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgems-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgems-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgems-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mGEMS

```bash
$ singularity exec <container> /usr/local/bin/mGEMS
$ podman run --it --rm --entrypoint /usr/local/bin/mGEMS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mGEMS   -v ${PWD} -w ${PWD} <container> -c " $@"
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