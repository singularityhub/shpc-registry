---
layout: container
name:  "quay.io/biocontainers/telescope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telescope/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/telescope/container.yaml"
updated_at: "2022-10-27 00:36:51.514992"
latest: "1.0.3--py37hc399e3d_5"
container_url: "https://biocontainers.pro/tools/telescope"
aliases:
 - "telescope"
versions:
 - "1.0.3--py37hc399e3d_5"
description: "shpc-registry automated BioContainers addition for telescope"
config: {"url": "https://biocontainers.pro/tools/telescope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for telescope", "latest": {"1.0.3--py37hc399e3d_5": "sha256:b2010ebdf2f5b2382317781653f583c3dc9ff8e487f1416c1d92cd1f1235ef65"}, "tags": {"1.0.3--py37hc399e3d_5": "sha256:b2010ebdf2f5b2382317781653f583c3dc9ff8e487f1416c1d92cd1f1235ef65"}, "docker": "quay.io/biocontainers/telescope", "aliases": {"telescope": "/usr/local/bin/telescope"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telescope.
shpc-registry automated BioContainers addition for telescope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telescope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telescope:1.0.3--py37hc399e3d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telescope/1.0.3--py37hc399e3d_5
$ module help quay.io/biocontainers/telescope/1.0.3--py37hc399e3d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telescope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telescope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telescope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telescope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telescope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telescope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### telescope

```bash
$ singularity exec <container> /usr/local/bin/telescope
$ podman run --it --rm --entrypoint /usr/local/bin/telescope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telescope   -v ${PWD} -w ${PWD} <container> -c " $@"
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