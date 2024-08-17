---
layout: container
name:  "quay.io/biocontainers/r-psych"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-psych/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-psych/container.yaml"
updated_at: "2024-08-17 03:12:46.505669"
latest: "crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout"
container_url: "https://biocontainers.pro/tools/r-psych"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.7.8--r3.4.1_0"
 - "crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout"
description: "shpc-registry automated BioContainers addition for r-psych"
config: {"url": "https://biocontainers.pro/tools/r-psych", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-psych", "latest": {"crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout": "crane digest quay.io/biocontainers/r-psych:crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout: parsing reference \"quay.io/biocontainers/r-psych:crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout\": could not parse reference"}, "tags": {"1.7.8--r3.4.1_0": "sha256:7a7a30f3c2bfd32542ed99c51dcd58d636c20b3f303780accc40ad1cb7c6ab92", "crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout": "crane digest quay.io/biocontainers/r-psych:crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout: parsing reference \"quay.io/biocontainers/r-psych:crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout\": could not parse reference"}, "docker": "quay.io/biocontainers/r-psych", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-psych.
shpc-registry automated BioContainers addition for r-psych
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-psych
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-psych:crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-psych/crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout
$ module help quay.io/biocontainers/r-psych/crane ls quay.io/biocontainers/r-psych: unrecognized HTTP status: 504 Gateway Timeout
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-psych-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-psych-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-psych-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-psych-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-psych-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-psych-inspect-deffile:

```bash
$ singularity inspect -d <container>
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