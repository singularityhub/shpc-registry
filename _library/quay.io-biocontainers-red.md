---
layout: container
name:  "quay.io/biocontainers/red"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/red/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/red/container.yaml"
updated_at: "2023-11-10 02:40:18.021306"
latest: "2018.09.10--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/red"
aliases:
 - "Red"
versions:
 - "2018.09.10--h9f5acd7_0"
 - "2018.09.10--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for red"
config: {"url": "https://biocontainers.pro/tools/red", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for red", "latest": {"2018.09.10--h4ac6f70_2": "sha256:d2dd7804a9f8b94479e8b9c29341429cbb2dda4dc4ba99cd10d88ece9a72e4be"}, "tags": {"2018.09.10--h9f5acd7_0": "sha256:a4674781d8393ec8cacfd050f94ea8300a4d37b5e44123abd629f9e5316d8035", "2018.09.10--h4ac6f70_2": "sha256:d2dd7804a9f8b94479e8b9c29341429cbb2dda4dc4ba99cd10d88ece9a72e4be"}, "docker": "quay.io/biocontainers/red", "aliases": {"Red": "/usr/local/bin/Red"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/red.
shpc-registry automated BioContainers addition for red
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/red
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/red:2018.09.10--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/red/2018.09.10--h4ac6f70_2
$ module help quay.io/biocontainers/red/2018.09.10--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### red-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### red-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### red-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### red-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### red-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### red-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Red

```bash
$ singularity exec <container> /usr/local/bin/Red
$ podman run --it --rm --entrypoint /usr/local/bin/Red   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Red   -v ${PWD} -w ${PWD} <container> -c " $@"
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