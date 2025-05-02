---
layout: container
name:  "ghcr.io/autamus/libquo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/libquo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/libquo/container.yaml"
updated_at: "2025-05-02 03:09:34.477824"
latest: "1.3.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/libquo"
aliases:
 - "quo-info"
versions:
 - "1.3.1"
 - "latest"
description: "QUO (as in status quo) is a runtime library that aids in accommodating thread-level heterogeneity in dynamic, phased MPI+X applications comprising single- and multi-threaded libraries."
config: {"docker": "ghcr.io/autamus/libquo", "url": "https://github.com/orgs/autamus/packages/container/package/libquo", "maintainer": "@vsoch", "description": "QUO (as in status quo) is a runtime library that aids in accommodating thread-level heterogeneity in dynamic, phased MPI+X applications comprising single- and multi-threaded libraries.", "latest": {"1.3.1": "sha256:b1271a2bc7ba00ed611ae722c97aeff4f7af4399f8d5f04a5d0da4745e04a0b2"}, "tags": {"1.3.1": "sha256:b1271a2bc7ba00ed611ae722c97aeff4f7af4399f8d5f04a5d0da4745e04a0b2", "latest": "sha256:b1271a2bc7ba00ed611ae722c97aeff4f7af4399f8d5f04a5d0da4745e04a0b2"}, "aliases": {"quo-info": "/opt/view/bin/quo-info"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/libquo.
QUO (as in status quo) is a runtime library that aids in accommodating thread-level heterogeneity in dynamic, phased MPI+X applications comprising single- and multi-threaded libraries.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/libquo
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libquo:1.3.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libquo/1.3.1
$ module help ghcr.io/autamus/libquo/1.3.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libquo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libquo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libquo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libquo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libquo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libquo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### quo-info

```bash
$ singularity exec <container> /opt/view/bin/quo-info
$ podman run --it --rm --entrypoint /opt/view/bin/quo-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/quo-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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