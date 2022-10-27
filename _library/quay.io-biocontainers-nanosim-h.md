---
layout: container
name:  "quay.io/biocontainers/nanosim-h"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanosim-h/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanosim-h/container.yaml"
updated_at: "2022-10-27 00:39:36.254965"
latest: "1.1.0.4--pyr40h145b6a8_2"
container_url: "https://biocontainers.pro/tools/nanosim-h"
aliases:
 - "last-split8"
 - "lastal8"
 - "lastdb8"
 - "maf-cut"
 - "nanosim-h"
 - "nanosim-h-train"
versions:
 - "1.1.0.4--pyr40h145b6a8_2"
description: "shpc-registry automated BioContainers addition for nanosim-h"
config: {"url": "https://biocontainers.pro/tools/nanosim-h", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanosim-h", "latest": {"1.1.0.4--pyr40h145b6a8_2": "sha256:76e3d6ab85a917623886d04b49504f1c0865dcfb6fa27cf9d8bd1a7145a26150"}, "tags": {"1.1.0.4--pyr40h145b6a8_2": "sha256:76e3d6ab85a917623886d04b49504f1c0865dcfb6fa27cf9d8bd1a7145a26150"}, "docker": "quay.io/biocontainers/nanosim-h", "aliases": {"last-split8": "/usr/local/bin/last-split8", "lastal8": "/usr/local/bin/lastal8", "lastdb8": "/usr/local/bin/lastdb8", "maf-cut": "/usr/local/bin/maf-cut", "nanosim-h": "/usr/local/bin/nanosim-h", "nanosim-h-train": "/usr/local/bin/nanosim-h-train"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanosim-h.
shpc-registry automated BioContainers addition for nanosim-h
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanosim-h
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanosim-h:1.1.0.4--pyr40h145b6a8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanosim-h/1.1.0.4--pyr40h145b6a8_2
$ module help quay.io/biocontainers/nanosim-h/1.1.0.4--pyr40h145b6a8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanosim-h-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-h-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-h-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanosim-h-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanosim-h-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanosim-h-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### last-split8

```bash
$ singularity exec <container> /usr/local/bin/last-split8
$ podman run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastal8

```bash
$ singularity exec <container> /usr/local/bin/lastal8
$ podman run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb8

```bash
$ singularity exec <container> /usr/local/bin/lastdb8
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-cut

```bash
$ singularity exec <container> /usr/local/bin/maf-cut
$ podman run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanosim-h

```bash
$ singularity exec <container> /usr/local/bin/nanosim-h
$ podman run --it --rm --entrypoint /usr/local/bin/nanosim-h   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosim-h   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanosim-h-train

```bash
$ singularity exec <container> /usr/local/bin/nanosim-h-train
$ podman run --it --rm --entrypoint /usr/local/bin/nanosim-h-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosim-h-train   -v ${PWD} -w ${PWD} <container> -c " $@"
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