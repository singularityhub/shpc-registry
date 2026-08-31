---
layout: container
name:  "quay.io/biocontainers/constrain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/constrain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/constrain/container.yaml"
updated_at: "2026-08-31 08:44:20.719629"
latest: "1.1.0--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/constrain"
aliases:
 - "ConSTRain"
versions:
 - "1.1.0--hab7d0fd_0"
description: "singularity registry hpc automated addition for constrain"
config: {"url": "https://biocontainers.pro/tools/constrain", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for constrain", "latest": {"1.1.0--hab7d0fd_0": "sha256:52c47faced743836754499cb9654e2888d20ff574b344138ecada25336b4e828"}, "tags": {"1.1.0--hab7d0fd_0": "sha256:52c47faced743836754499cb9654e2888d20ff574b344138ecada25336b4e828"}, "docker": "quay.io/biocontainers/constrain", "aliases": {"ConSTRain": "/usr/local/bin/ConSTRain"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/constrain.
singularity registry hpc automated addition for constrain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/constrain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/constrain:1.1.0--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/constrain/1.1.0--hab7d0fd_0
$ module help quay.io/biocontainers/constrain/1.1.0--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### constrain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### constrain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### constrain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### constrain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### constrain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### constrain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ConSTRain

```bash
$ singularity exec <container> /usr/local/bin/ConSTRain
$ podman run --it --rm --entrypoint /usr/local/bin/ConSTRain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ConSTRain   -v ${PWD} -w ${PWD} <container> -c " $@"
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