---
layout: container
name:  "quay.io/biocontainers/scvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scvis/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scvis/container.yaml"
updated_at: "2022-10-27 00:38:29.063798"
latest: "0.1.0--scvis_0"
container_url: "https://biocontainers.pro/tools/scvis"
aliases:
 - "scvis"
versions:
 - "0.1.0--scvis_0"
description: "shpc-registry automated BioContainers addition for scvis"
config: {"url": "https://biocontainers.pro/tools/scvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scvis", "latest": {"0.1.0--scvis_0": "sha256:8480ed863db56e475879e139e667422bfd029eb906d15cf1bf33a8c4ae9a7ea6"}, "tags": {"0.1.0--scvis_0": "sha256:8480ed863db56e475879e139e667422bfd029eb906d15cf1bf33a8c4ae9a7ea6"}, "docker": "quay.io/biocontainers/scvis", "aliases": {"scvis": "/usr/local/bin/scvis"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scvis.
shpc-registry automated BioContainers addition for scvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scvis:0.1.0--scvis_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scvis/0.1.0--scvis_0
$ module help quay.io/biocontainers/scvis/0.1.0--scvis_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scvis

```bash
$ singularity exec <container> /usr/local/bin/scvis
$ podman run --it --rm --entrypoint /usr/local/bin/scvis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scvis   -v ${PWD} -w ${PWD} <container> -c " $@"
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