---
layout: container
name:  "quay.io/biocontainers/gocr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gocr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gocr/container.yaml"
updated_at: "2022-11-17 03:25:54.340075"
latest: "0.50--hec16e2b_4"
container_url: "https://biocontainers.pro/tools/gocr"
aliases:
 - "gocr"
 - "gocr.tcl"
versions:
 - "0.50--hec16e2b_4"
description: "shpc-registry automated BioContainers addition for gocr"
config: {"url": "https://biocontainers.pro/tools/gocr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gocr", "latest": {"0.50--hec16e2b_4": "sha256:af5d9ac323d151e22e20d3cee1124fbeefa75e9709f99a9ae9b8d8a2d28ff55b"}, "tags": {"0.50--hec16e2b_4": "sha256:af5d9ac323d151e22e20d3cee1124fbeefa75e9709f99a9ae9b8d8a2d28ff55b"}, "docker": "quay.io/biocontainers/gocr", "aliases": {"gocr": "/usr/local/bin/gocr", "gocr.tcl": "/usr/local/bin/gocr.tcl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gocr.
shpc-registry automated BioContainers addition for gocr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gocr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gocr:0.50--hec16e2b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gocr/0.50--hec16e2b_4
$ module help quay.io/biocontainers/gocr/0.50--hec16e2b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gocr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gocr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gocr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gocr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gocr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gocr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gocr

```bash
$ singularity exec <container> /usr/local/bin/gocr
$ podman run --it --rm --entrypoint /usr/local/bin/gocr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gocr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gocr.tcl

```bash
$ singularity exec <container> /usr/local/bin/gocr.tcl
$ podman run --it --rm --entrypoint /usr/local/bin/gocr.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gocr.tcl   -v ${PWD} -w ${PWD} <container> -c " $@"
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