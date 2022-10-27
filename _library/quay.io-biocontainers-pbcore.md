---
layout: container
name:  "quay.io/biocontainers/pbcore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbcore/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pbcore/container.yaml"
updated_at: "2022-10-27 01:12:28.593550"
latest: "2.1.2--py_2"
container_url: "https://biocontainers.pro/tools/pbcore"
aliases:
 - ".open"
 - ".pbcore-post-link.sh"
versions:
 - "2.1.2--py_2"
description: "shpc-registry automated BioContainers addition for pbcore"
config: {"url": "https://biocontainers.pro/tools/pbcore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbcore", "latest": {"2.1.2--py_2": "sha256:5661257583c7ba3a3661f443eed2680b0e4a90605fc8f3e4c18ab10de4983187"}, "tags": {"2.1.2--py_2": "sha256:5661257583c7ba3a3661f443eed2680b0e4a90605fc8f3e4c18ab10de4983187"}, "docker": "quay.io/biocontainers/pbcore", "aliases": {".open": "/usr/local/bin/.open", ".pbcore-post-link.sh": "/usr/local/bin/.pbcore-post-link.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbcore.
shpc-registry automated BioContainers addition for pbcore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbcore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbcore:2.1.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbcore/2.1.2--py_2
$ module help quay.io/biocontainers/pbcore/2.1.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbcore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbcore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbcore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbcore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbcore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbcore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .open

```bash
$ singularity exec <container> /usr/local/bin/.open
$ podman run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcore-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcore-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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