---
layout: container
name:  "ghcr.io/autamus/libxpm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/libxpm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/libxpm/container.yaml"
updated_at: "2025-07-19 23:59:47.747539"
latest: "3.5.12"
container_url: "https://github.com/orgs/autamus/packages/container/package/libxpm"

versions:
 - "3.5.12"
 - "latest"
description: "The X PixMap image format is an extension of the monochrome X BitMap format specified in the X protocol, and is commonly used in traditional X applications."
config: {"docker": "ghcr.io/autamus/libxpm", "url": "https://github.com/orgs/autamus/packages/container/package/libxpm", "maintainer": "@vsoch", "description": "The X PixMap image format is an extension of the monochrome X BitMap format specified in the X protocol, and is commonly used in traditional X applications.", "latest": {"3.5.12": "sha256:02a93850ecc72f1c467616653bbd3ca77e78590ca42e366e91378231d918d680"}, "tags": {"3.5.12": "sha256:02a93850ecc72f1c467616653bbd3ca77e78590ca42e366e91378231d918d680", "latest": "sha256:02a93850ecc72f1c467616653bbd3ca77e78590ca42e366e91378231d918d680"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/libxpm.
The X PixMap image format is an extension of the monochrome X BitMap format specified in the X protocol, and is commonly used in traditional X applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/libxpm
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libxpm:3.5.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libxpm/3.5.12
$ module help ghcr.io/autamus/libxpm/3.5.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libxpm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libxpm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libxpm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libxpm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libxpm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libxpm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libxpm

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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