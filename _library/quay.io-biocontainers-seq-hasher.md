---
layout: container
name:  "quay.io/biocontainers/seq-hasher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seq-hasher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seq-hasher/container.yaml"
updated_at: "2024-10-24 10:34:14.717439"
latest: "0.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/seq-hasher"
aliases:
 - "seq-hasher"
versions:
 - "0.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for seq-hasher"
config: {"url": "https://biocontainers.pro/tools/seq-hasher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seq-hasher", "latest": {"0.1.0--h4349ce8_0": "sha256:63909f041a8fa09a996c98b5ab16e0ba31082c657cbd228d85813e68e9f4fcc4"}, "tags": {"0.1.0--h4349ce8_0": "sha256:63909f041a8fa09a996c98b5ab16e0ba31082c657cbd228d85813e68e9f4fcc4"}, "docker": "quay.io/biocontainers/seq-hasher", "aliases": {"seq-hasher": "/usr/local/bin/seq-hasher"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seq-hasher.
singularity registry hpc automated addition for seq-hasher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seq-hasher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seq-hasher:0.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seq-hasher/0.1.0--h4349ce8_0
$ module help quay.io/biocontainers/seq-hasher/0.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seq-hasher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seq-hasher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seq-hasher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seq-hasher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seq-hasher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seq-hasher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seq-hasher

```bash
$ singularity exec <container> /usr/local/bin/seq-hasher
$ podman run --it --rm --entrypoint /usr/local/bin/seq-hasher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-hasher   -v ${PWD} -w ${PWD} <container> -c " $@"
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