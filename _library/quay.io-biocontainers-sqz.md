---
layout: container
name:  "quay.io/biocontainers/sqz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sqz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sqz/container.yaml"
updated_at: "2026-04-03 04:51:32.881305"
latest: "0.2.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/sqz"
aliases:
 - "sqz"
versions:
 - "0.2.0--h4349ce8_0"
description: "singularity registry hpc automated addition for sqz"
config: {"url": "https://biocontainers.pro/tools/sqz", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sqz", "latest": {"0.2.0--h4349ce8_0": "sha256:9e89a1eae2b1cfe90788d2156bc59d13dd5cee747e3bc1b8de98bafb81427b73"}, "tags": {"0.2.0--h4349ce8_0": "sha256:9e89a1eae2b1cfe90788d2156bc59d13dd5cee747e3bc1b8de98bafb81427b73"}, "docker": "quay.io/biocontainers/sqz", "aliases": {"sqz": "/usr/local/bin/sqz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sqz.
singularity registry hpc automated addition for sqz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sqz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sqz:0.2.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sqz/0.2.0--h4349ce8_0
$ module help quay.io/biocontainers/sqz/0.2.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sqz

```bash
$ singularity exec <container> /usr/local/bin/sqz
$ podman run --it --rm --entrypoint /usr/local/bin/sqz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqz   -v ${PWD} -w ${PWD} <container> -c " $@"
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