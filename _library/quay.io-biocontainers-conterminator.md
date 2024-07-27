---
layout: container
name:  "quay.io/biocontainers/conterminator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/conterminator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/conterminator/container.yaml"
updated_at: "2024-07-27 03:06:16.079683"
latest: "1.c74b5--h95f258a_1"
container_url: "https://biocontainers.pro/tools/conterminator"
aliases:
 - "conterminator"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
versions:
 - "1.c74b5--h95f258a_1"
description: "shpc-registry automated BioContainers addition for conterminator"
config: {"url": "https://biocontainers.pro/tools/conterminator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for conterminator", "latest": {"1.c74b5--h95f258a_1": "sha256:acd54557b7875528ea413fd69dd70715aa87e59f0d8f93ad0798c27927bba44a"}, "tags": {"1.c74b5--h95f258a_1": "sha256:acd54557b7875528ea413fd69dd70715aa87e59f0d8f93ad0798c27927bba44a"}, "docker": "quay.io/biocontainers/conterminator", "aliases": {"conterminator": "/usr/local/bin/conterminator", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/conterminator.
shpc-registry automated BioContainers addition for conterminator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/conterminator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/conterminator:1.c74b5--h95f258a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/conterminator/1.c74b5--h95f258a_1
$ module help quay.io/biocontainers/conterminator/1.c74b5--h95f258a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### conterminator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### conterminator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### conterminator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### conterminator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### conterminator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### conterminator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### conterminator

```bash
$ singularity exec <container> /usr/local/bin/conterminator
$ podman run --it --rm --entrypoint /usr/local/bin/conterminator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conterminator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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