---
layout: container
name:  "quay.io/biocontainers/r-phangorn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-phangorn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-phangorn/container.yaml"
updated_at: "2023-10-04 05:09:17.857065"
latest: "2.4.0--r341h9d2a408_0"
container_url: "https://biocontainers.pro/tools/r-phangorn"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.4.0--r341h9d2a408_0"
description: "shpc-registry automated BioContainers addition for r-phangorn"
config: {"url": "https://biocontainers.pro/tools/r-phangorn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-phangorn", "latest": {"2.4.0--r341h9d2a408_0": "sha256:66b9f896c91ab26403d2823a5354cfa9a2fae92d7f31e1d8f972cb91f7303191"}, "tags": {"2.4.0--r341h9d2a408_0": "sha256:66b9f896c91ab26403d2823a5354cfa9a2fae92d7f31e1d8f972cb91f7303191"}, "docker": "quay.io/biocontainers/r-phangorn", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-phangorn.
shpc-registry automated BioContainers addition for r-phangorn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-phangorn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-phangorn:2.4.0--r341h9d2a408_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-phangorn/2.4.0--r341h9d2a408_0
$ module help quay.io/biocontainers/r-phangorn/2.4.0--r341h9d2a408_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-phangorn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-phangorn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-phangorn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-phangorn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-phangorn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-phangorn-inspect-deffile:

```bash
$ singularity inspect -d <container>
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