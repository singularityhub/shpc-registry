---
layout: container
name:  "quay.io/biocontainers/slang"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slang/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slang/container.yaml"
updated_at: "2025-04-22 03:09:49.716871"
latest: "2.3.0--hd3527cb_3"
container_url: "https://biocontainers.pro/tools/slang"
aliases:
 - "slsh"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.3.0--hd3527cb_3"
description: "shpc-registry automated BioContainers addition for slang"
config: {"url": "https://biocontainers.pro/tools/slang", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slang", "latest": {"2.3.0--hd3527cb_3": "sha256:fbe70303bc629250d75f5a887abb39458565bfb18ec2412331361c454bae0bf0"}, "tags": {"2.3.0--hd3527cb_3": "sha256:fbe70303bc629250d75f5a887abb39458565bfb18ec2412331361c454bae0bf0"}, "docker": "quay.io/biocontainers/slang", "aliases": {"slsh": "/usr/local/bin/slsh", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slang.
shpc-registry automated BioContainers addition for slang
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slang
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slang:2.3.0--hd3527cb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slang/2.3.0--hd3527cb_3
$ module help quay.io/biocontainers/slang/2.3.0--hd3527cb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slang-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slang-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slang-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slang-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slang-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slang-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slsh

```bash
$ singularity exec <container> /usr/local/bin/slsh
$ podman run --it --rm --entrypoint /usr/local/bin/slsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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