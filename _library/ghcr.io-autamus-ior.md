---
layout: container
name:  "ghcr.io/autamus/ior"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ior/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/ior/container.yaml"
updated_at: "2024-10-24 10:32:43.813814"
latest: "3.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/ior"
aliases:
 - "ior"
versions:
 - "3.3.0"
 - "latest"
description: "IOR is a parallel IO benchmark that can be used to test the performance of parallel storage systems using various interfaces and access patterns. "
config: {"docker": "ghcr.io/autamus/ior", "url": "https://github.com/orgs/autamus/packages/container/package/ior", "maintainer": "@vsoch", "description": "IOR is a parallel IO benchmark that can be used to test the performance of parallel storage systems using various interfaces and access patterns. ", "latest": {"3.3.0": "sha256:fce17f6d8fad6ee7266d371967da40f03ef9e0907980d4ecce7d6a12dc8db877"}, "tags": {"3.3.0": "sha256:fce17f6d8fad6ee7266d371967da40f03ef9e0907980d4ecce7d6a12dc8db877", "latest": "sha256:fce17f6d8fad6ee7266d371967da40f03ef9e0907980d4ecce7d6a12dc8db877"}, "aliases": {"ior": "/opt/view/bin/ior"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ior.
IOR is a parallel IO benchmark that can be used to test the performance of parallel storage systems using various interfaces and access patterns. 
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ior
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ior:3.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ior/3.3.0
$ module help ghcr.io/autamus/ior/3.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ior-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ior-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ior-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ior-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ior-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ior-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ior

```bash
$ singularity exec <container> /opt/view/bin/ior
$ podman run --it --rm --entrypoint /opt/view/bin/ior   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ior   -v ${PWD} -w ${PWD} <container> -c " $@"
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