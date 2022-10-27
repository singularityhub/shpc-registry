---
layout: container
name:  "quay.io/biocontainers/nanoraw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoraw/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanoraw/container.yaml"
updated_at: "2022-10-27 00:56:37.170297"
latest: "0.5--py_3"
container_url: "https://biocontainers.pro/tools/nanoraw"
aliases:
 - "graphmap"
 - "nanoraw"
versions:
 - "0.5--py_3"
description: "shpc-registry automated BioContainers addition for nanoraw"
config: {"url": "https://biocontainers.pro/tools/nanoraw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoraw", "latest": {"0.5--py_3": "sha256:db7ed0855361274788e57ba99a506944c622a5c9f286a446ac19a055506b5f49"}, "tags": {"0.5--py_3": "sha256:db7ed0855361274788e57ba99a506944c622a5c9f286a446ac19a055506b5f49"}, "docker": "quay.io/biocontainers/nanoraw", "aliases": {"graphmap": "/usr/local/bin/graphmap", "nanoraw": "/usr/local/bin/nanoraw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoraw.
shpc-registry automated BioContainers addition for nanoraw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoraw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoraw:0.5--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoraw/0.5--py_3
$ module help quay.io/biocontainers/nanoraw/0.5--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoraw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoraw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoraw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoraw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoraw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoraw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphmap

```bash
$ singularity exec <container> /usr/local/bin/graphmap
$ podman run --it --rm --entrypoint /usr/local/bin/graphmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanoraw

```bash
$ singularity exec <container> /usr/local/bin/nanoraw
$ podman run --it --rm --entrypoint /usr/local/bin/nanoraw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanoraw   -v ${PWD} -w ${PWD} <container> -c " $@"
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