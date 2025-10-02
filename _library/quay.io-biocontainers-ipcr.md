---
layout: container
name:  "quay.io/biocontainers/ipcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ipcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ipcr/container.yaml"
updated_at: "2025-10-02 04:14:36.762595"
latest: "1.1.0--h467016e_0"
container_url: "https://biocontainers.pro/tools/ipcr"
aliases:
 - "ipcr"
versions:
 - "1.1.0--h467016e_0"
description: "singularity registry hpc automated addition for ipcr"
config: {"url": "https://biocontainers.pro/tools/ipcr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ipcr", "latest": {"1.1.0--h467016e_0": "sha256:c4554628a461ad1d70f53b95af3fcb40e550352391a868d6382fc61f7194c5c1"}, "tags": {"1.1.0--h467016e_0": "sha256:c4554628a461ad1d70f53b95af3fcb40e550352391a868d6382fc61f7194c5c1"}, "docker": "quay.io/biocontainers/ipcr", "aliases": {"ipcr": "/usr/local/bin/ipcr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ipcr.
singularity registry hpc automated addition for ipcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ipcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ipcr:1.1.0--h467016e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ipcr/1.1.0--h467016e_0
$ module help quay.io/biocontainers/ipcr/1.1.0--h467016e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ipcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ipcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ipcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ipcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ipcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ipcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ipcr

```bash
$ singularity exec <container> /usr/local/bin/ipcr
$ podman run --it --rm --entrypoint /usr/local/bin/ipcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcr   -v ${PWD} -w ${PWD} <container> -c " $@"
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