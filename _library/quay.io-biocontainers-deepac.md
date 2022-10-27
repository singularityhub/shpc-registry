---
layout: container
name:  "quay.io/biocontainers/deepac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepac/container.yaml"
updated_at: "2022-10-27 00:38:12.699359"
latest: "0.9.3--py_1"
container_url: "https://biocontainers.pro/tools/deepac"
aliases:
 - "deepac"
versions:
 - "0.9.3--py_1"
description: "shpc-registry automated BioContainers addition for deepac"
config: {"url": "https://biocontainers.pro/tools/deepac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepac", "latest": {"0.9.3--py_1": "sha256:8c1672e6ba919988ba7d9bbd909e1a3298dd226f13c4af3778d0a87529d7c8f8"}, "tags": {"0.9.3--py_1": "sha256:8c1672e6ba919988ba7d9bbd909e1a3298dd226f13c4af3778d0a87529d7c8f8"}, "docker": "quay.io/biocontainers/deepac", "aliases": {"deepac": "/usr/local/bin/deepac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepac.
shpc-registry automated BioContainers addition for deepac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepac:0.9.3--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepac/0.9.3--py_1
$ module help quay.io/biocontainers/deepac/0.9.3--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepac

```bash
$ singularity exec <container> /usr/local/bin/deepac
$ podman run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
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