---
layout: container
name:  "quay.io/biocontainers/r-geoaxe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-geoaxe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-geoaxe/container.yaml"
updated_at: "2024-08-19 03:38:54.761683"
latest: "0.1.0--r351h6115d3f_4"
container_url: "https://biocontainers.pro/tools/r-geoaxe"
aliases:
 - "geos-config"
 - "c89"
 - "c99"
versions:
 - "0.1.0--r351h6115d3f_4"
description: "shpc-registry automated BioContainers addition for r-geoaxe"
config: {"url": "https://biocontainers.pro/tools/r-geoaxe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-geoaxe", "latest": {"0.1.0--r351h6115d3f_4": "sha256:c277b766437dd8490c8d879e635d23569a27533d0fbd41763e1561124026ca40"}, "tags": {"0.1.0--r351h6115d3f_4": "sha256:c277b766437dd8490c8d879e635d23569a27533d0fbd41763e1561124026ca40"}, "docker": "quay.io/biocontainers/r-geoaxe", "aliases": {"geos-config": "/usr/local/bin/geos-config", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-geoaxe.
shpc-registry automated BioContainers addition for r-geoaxe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-geoaxe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-geoaxe:0.1.0--r351h6115d3f_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-geoaxe/0.1.0--r351h6115d3f_4
$ module help quay.io/biocontainers/r-geoaxe/0.1.0--r351h6115d3f_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-geoaxe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-geoaxe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-geoaxe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-geoaxe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-geoaxe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-geoaxe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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