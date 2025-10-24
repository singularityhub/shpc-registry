---
layout: container
name:  "quay.io/biocontainers/datavzrd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/datavzrd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/datavzrd/container.yaml"
updated_at: "2025-10-24 03:28:49.939348"
latest: "2.23.2"
container_url: "https://biocontainers.pro/tools/datavzrd"
aliases:
 - "datavzrd"
versions:
 - "2.23.2"
description: "singularity registry hpc automated addition for datavzrd"
config: {"url": "https://biocontainers.pro/tools/datavzrd", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for datavzrd", "latest": {"2.23.2": "sha256:035fcc3dd8cbe35d3d41d563fe6f542dc89798c06075b656b74b0fc2b7362fe0"}, "tags": {"2.23.2": "sha256:035fcc3dd8cbe35d3d41d563fe6f542dc89798c06075b656b74b0fc2b7362fe0"}, "docker": "quay.io/biocontainers/datavzrd", "aliases": {"datavzrd": "/usr/local/bin/datavzrd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/datavzrd.
singularity registry hpc automated addition for datavzrd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/datavzrd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/datavzrd:2.23.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/datavzrd/2.23.2
$ module help quay.io/biocontainers/datavzrd/2.23.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### datavzrd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### datavzrd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### datavzrd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### datavzrd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### datavzrd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### datavzrd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### datavzrd

```bash
$ singularity exec <container> /usr/local/bin/datavzrd
$ podman run --it --rm --entrypoint /usr/local/bin/datavzrd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datavzrd   -v ${PWD} -w ${PWD} <container> -c " $@"
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