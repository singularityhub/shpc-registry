---
layout: container
name:  "ghcr.io/autamus/alan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/alan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/alan/container.yaml"
updated_at: "2024-05-02 03:39:38.927479"
latest: "2.1.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/alan"
aliases:
 - "alan"
versions:
 - "2.1.1"
 - "latest"
description: "A simple in-terminal alignment viewer."
config: {"docker": "ghcr.io/autamus/alan", "url": "https://github.com/orgs/autamus/packages/container/package/alan", "maintainer": "@vsoch", "description": "A simple in-terminal alignment viewer.", "latest": {"2.1.1": "sha256:fc247776706f7537b8abaa11cf13404ebdb94cb33c8d9ac111febd09c10debd1"}, "tags": {"2.1.1": "sha256:fc247776706f7537b8abaa11cf13404ebdb94cb33c8d9ac111febd09c10debd1", "latest": "sha256:fc247776706f7537b8abaa11cf13404ebdb94cb33c8d9ac111febd09c10debd1"}, "aliases": {"alan": "/opt/view/bin/alan"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/alan.
A simple in-terminal alignment viewer.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/alan
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/alan:2.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/alan/2.1.1
$ module help ghcr.io/autamus/alan/2.1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alan

```bash
$ singularity exec <container> /opt/view/bin/alan
$ podman run --it --rm --entrypoint /opt/view/bin/alan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/alan   -v ${PWD} -w ${PWD} <container> -c " $@"
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