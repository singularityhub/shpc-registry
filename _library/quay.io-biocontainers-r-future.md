---
layout: container
name:  "quay.io/biocontainers/r-future"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-future/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-future/container.yaml"
updated_at: "2024-08-08 03:49:42.715689"
latest: "1.2.0--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-future"
aliases:
 - "uconv"
 - "tclsh8.5"
 - "wish8.5"
 - "ncursesw5-config"
versions:
 - "1.2.0--r3.3.2_0"
 - "1.2.0--r3.3.1_0"
description: "shpc-registry automated BioContainers addition for r-future"
config: {"url": "https://biocontainers.pro/tools/r-future", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-future", "latest": {"1.2.0--r3.3.2_0": "sha256:aac453f51e35f8f4f7427ce0ab8d991bfe321065b91f7fb7d4c34eae54344a7f"}, "tags": {"1.2.0--r3.3.2_0": "sha256:aac453f51e35f8f4f7427ce0ab8d991bfe321065b91f7fb7d4c34eae54344a7f", "1.2.0--r3.3.1_0": "sha256:6412abcde4dae0113e7dfb191dcda46152a74ee84a7810280ec9277302b5a6b9"}, "docker": "quay.io/biocontainers/r-future", "aliases": {"uconv": "/usr/local/bin/uconv", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-future.
shpc-registry automated BioContainers addition for r-future
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-future
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-future:1.2.0--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-future/1.2.0--r3.3.2_0
$ module help quay.io/biocontainers/r-future/1.2.0--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-future-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-future-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-future-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-future-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-future-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-future-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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