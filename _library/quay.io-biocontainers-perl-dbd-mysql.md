---
layout: container
name:  "quay.io/biocontainers/perl-dbd-mysql"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-dbd-mysql/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-dbd-mysql/container.yaml"
updated_at: "2022-10-27 00:24:52.181988"
latest: "4.050--pl5321h9f5acd7_0"
container_url: "https://biocontainers.pro/tools/perl-dbd-mysql"
aliases:
 - "use-devel-checklib"
versions:
 - "4.050--pl5321h9f5acd7_0"
description: "shpc-registry automated BioContainers addition for perl-dbd-mysql"
config: {"url": "https://biocontainers.pro/tools/perl-dbd-mysql", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-dbd-mysql", "latest": {"4.050--pl5321h9f5acd7_0": "sha256:799bad957a8610d11b293d4630b0b0c244533ecd86394eb1c3c62c5d7f20db5a"}, "tags": {"4.050--pl5321h9f5acd7_0": "sha256:799bad957a8610d11b293d4630b0b0c244533ecd86394eb1c3c62c5d7f20db5a"}, "docker": "quay.io/biocontainers/perl-dbd-mysql", "aliases": {"use-devel-checklib": "/usr/local/bin/use-devel-checklib"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-dbd-mysql.
shpc-registry automated BioContainers addition for perl-dbd-mysql
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-dbd-mysql
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-dbd-mysql:4.050--pl5321h9f5acd7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-dbd-mysql/4.050--pl5321h9f5acd7_0
$ module help quay.io/biocontainers/perl-dbd-mysql/4.050--pl5321h9f5acd7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-dbd-mysql-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-dbd-mysql-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-dbd-mysql-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-dbd-mysql-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-dbd-mysql-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-dbd-mysql-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### use-devel-checklib

```bash
$ singularity exec <container> /usr/local/bin/use-devel-checklib
$ podman run --it --rm --entrypoint /usr/local/bin/use-devel-checklib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/use-devel-checklib   -v ${PWD} -w ${PWD} <container> -c " $@"
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