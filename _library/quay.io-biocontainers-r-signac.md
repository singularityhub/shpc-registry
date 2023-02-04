---
layout: container
name:  "quay.io/biocontainers/r-signac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-signac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-signac/container.yaml"
updated_at: "2023-02-04 03:09:57.152854"
latest: "1.8.0--r42hecf12ef_1"
container_url: "https://biocontainers.pro/tools/r-signac"
aliases:
 - "geosop"
 - "geos-config"
versions:
 - "1.8.0--r41hecf12ef_0"
 - "1.8.0--r42hecf12ef_1"
description: "shpc-registry automated BioContainers addition for r-signac"
config: {"url": "https://biocontainers.pro/tools/r-signac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-signac", "latest": {"1.8.0--r42hecf12ef_1": "sha256:0e1afe6c0bae43e4b1064710c97d9be7e282f44ea147e1cd1f9e9ebcaa05ff34"}, "tags": {"1.8.0--r41hecf12ef_0": "sha256:f212100013aac7cf43778f9fa5d9fc9e2aea39ed90d58919ea99c43f99405fb8", "1.8.0--r42hecf12ef_1": "sha256:0e1afe6c0bae43e4b1064710c97d9be7e282f44ea147e1cd1f9e9ebcaa05ff34"}, "docker": "quay.io/biocontainers/r-signac", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-signac.
shpc-registry automated BioContainers addition for r-signac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-signac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-signac:1.8.0--r42hecf12ef_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-signac/1.8.0--r42hecf12ef_1
$ module help quay.io/biocontainers/r-signac/1.8.0--r42hecf12ef_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-signac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-signac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-signac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-signac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-signac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-signac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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