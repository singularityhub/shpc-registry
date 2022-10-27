---
layout: container
name:  "quay.io/biocontainers/savage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/savage/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/savage/container.yaml"
updated_at: "2022-10-27 00:24:08.711022"
latest: "0.4.2--py27h16ec135_2"
container_url: "https://biocontainers.pro/tools/savage"
aliases:
 - "rust-overlaps"
 - "savage"
versions:
 - "0.4.2--py27h16ec135_2"
description: "shpc-registry automated BioContainers addition for savage"
config: {"url": "https://biocontainers.pro/tools/savage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for savage", "latest": {"0.4.2--py27h16ec135_2": "sha256:49c7fda8572f906a5bfe94e9972e670b61f780f6c4965d980036d3ff0d6ad4a4"}, "tags": {"0.4.2--py27h16ec135_2": "sha256:49c7fda8572f906a5bfe94e9972e670b61f780f6c4965d980036d3ff0d6ad4a4"}, "docker": "quay.io/biocontainers/savage", "aliases": {"rust-overlaps": "/usr/local/bin/rust-overlaps", "savage": "/usr/local/bin/savage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/savage.
shpc-registry automated BioContainers addition for savage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/savage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/savage:0.4.2--py27h16ec135_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/savage/0.4.2--py27h16ec135_2
$ module help quay.io/biocontainers/savage/0.4.2--py27h16ec135_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### savage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### savage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### savage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### savage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### savage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### savage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rust-overlaps

```bash
$ singularity exec <container> /usr/local/bin/rust-overlaps
$ podman run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rust-overlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### savage

```bash
$ singularity exec <container> /usr/local/bin/savage
$ podman run --it --rm --entrypoint /usr/local/bin/savage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/savage   -v ${PWD} -w ${PWD} <container> -c " $@"
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