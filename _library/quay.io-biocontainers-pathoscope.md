---
layout: container
name:  "quay.io/biocontainers/pathoscope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pathoscope/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pathoscope/container.yaml"
updated_at: "2022-10-27 00:41:58.807829"
latest: "2.0.7--py_1"
container_url: "https://biocontainers.pro/tools/pathoscope"
aliases:
 - "pathoscope"
versions:
 - "2.0.7--py_1"
description: "shpc-registry automated BioContainers addition for pathoscope"
config: {"url": "https://biocontainers.pro/tools/pathoscope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pathoscope", "latest": {"2.0.7--py_1": "sha256:2768a98e8714e8ac5d5b8c6566b6d0c121e9ce35794dd8eebe9607dd636f8f31"}, "tags": {"2.0.7--py_1": "sha256:2768a98e8714e8ac5d5b8c6566b6d0c121e9ce35794dd8eebe9607dd636f8f31"}, "docker": "quay.io/biocontainers/pathoscope", "aliases": {"pathoscope": "/usr/local/bin/pathoscope"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pathoscope.
shpc-registry automated BioContainers addition for pathoscope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pathoscope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pathoscope:2.0.7--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pathoscope/2.0.7--py_1
$ module help quay.io/biocontainers/pathoscope/2.0.7--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pathoscope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pathoscope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pathoscope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pathoscope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pathoscope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pathoscope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pathoscope

```bash
$ singularity exec <container> /usr/local/bin/pathoscope
$ podman run --it --rm --entrypoint /usr/local/bin/pathoscope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathoscope   -v ${PWD} -w ${PWD} <container> -c " $@"
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