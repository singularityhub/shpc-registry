---
layout: container
name:  "quay.io/biocontainers/kmtricks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmtricks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmtricks/container.yaml"
updated_at: "2023-12-16 02:48:36.244216"
latest: "1.4.0--h8b7377a_0"
container_url: "https://biocontainers.pro/tools/kmtricks"
aliases:
 - "kmtricks"
 - "kmtricks-socks"
 - "kmtricksp"
versions:
 - "1.4.0--h8b7377a_0"
description: "singularity registry hpc automated addition for kmtricks"
config: {"url": "https://biocontainers.pro/tools/kmtricks", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmtricks", "latest": {"1.4.0--h8b7377a_0": "sha256:89138f7ae98572df7c3cbef49a8eb31c160d17d167cd203608e6385d199f1084"}, "tags": {"1.4.0--h8b7377a_0": "sha256:89138f7ae98572df7c3cbef49a8eb31c160d17d167cd203608e6385d199f1084"}, "docker": "quay.io/biocontainers/kmtricks", "aliases": {"kmtricks": "/usr/local/bin/kmtricks", "kmtricks-socks": "/usr/local/bin/kmtricks-socks", "kmtricksp": "/usr/local/bin/kmtricksp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmtricks.
singularity registry hpc automated addition for kmtricks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmtricks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmtricks:1.4.0--h8b7377a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmtricks/1.4.0--h8b7377a_0
$ module help quay.io/biocontainers/kmtricks/1.4.0--h8b7377a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmtricks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmtricks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmtricks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmtricks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmtricks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmtricks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmtricks

```bash
$ singularity exec <container> /usr/local/bin/kmtricks
$ podman run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmtricks-socks

```bash
$ singularity exec <container> /usr/local/bin/kmtricks-socks
$ podman run --it --rm --entrypoint /usr/local/bin/kmtricks-socks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmtricks-socks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmtricksp

```bash
$ singularity exec <container> /usr/local/bin/kmtricksp
$ podman run --it --rm --entrypoint /usr/local/bin/kmtricksp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmtricksp   -v ${PWD} -w ${PWD} <container> -c " $@"
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