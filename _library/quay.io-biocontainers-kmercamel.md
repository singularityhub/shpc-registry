---
layout: container
name:  "quay.io/biocontainers/kmercamel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmercamel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmercamel/container.yaml"
updated_at: "2025-12-05 03:47:23.332540"
latest: "2.2.0--ha119d93_0"
container_url: "https://biocontainers.pro/tools/kmercamel"
aliases:
 - "kmercamel"
 - "glpsol"
versions:
 - "1.0.2--hc4f6fa1_1"
 - "1.0.2--ha119d93_2"
 - "2.0.0--ha119d93_0"
 - "2.1.1--ha119d93_0"
 - "2.2.0--ha119d93_0"
description: "singularity registry hpc automated addition for kmercamel"
config: {"url": "https://biocontainers.pro/tools/kmercamel", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmercamel", "latest": {"2.2.0--ha119d93_0": "sha256:9ed6310dca68d6988adaa05baff954a5191c3d6c437be94b03743a7be94b4fdb"}, "tags": {"1.0.2--hc4f6fa1_1": "sha256:c73a9cd0fab7231251c3879d36b99ede97d29d9671fe9295dd93744f0745121e", "1.0.2--ha119d93_2": "sha256:3ec068690aea86436331bd6dfc5829261d69505a8e402a4c79d728e89bbad294", "2.0.0--ha119d93_0": "sha256:b38ae3c1ecc2d72d72192a50ad6c7372eab3bc0051d86c7a096bd0b4c27bad25", "2.1.1--ha119d93_0": "sha256:54ad04901a00533bb725fceebdf6b8e9047a8666acb7d8992e2c7adbd3fb0b72", "2.2.0--ha119d93_0": "sha256:9ed6310dca68d6988adaa05baff954a5191c3d6c437be94b03743a7be94b4fdb"}, "docker": "quay.io/biocontainers/kmercamel", "aliases": {"kmercamel": "/usr/local/bin/kmercamel", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmercamel.
singularity registry hpc automated addition for kmercamel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmercamel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmercamel:2.2.0--ha119d93_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmercamel/2.2.0--ha119d93_0
$ module help quay.io/biocontainers/kmercamel/2.2.0--ha119d93_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmercamel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmercamel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmercamel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmercamel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmercamel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmercamel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmercamel

```bash
$ singularity exec <container> /usr/local/bin/kmercamel
$ podman run --it --rm --entrypoint /usr/local/bin/kmercamel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmercamel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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