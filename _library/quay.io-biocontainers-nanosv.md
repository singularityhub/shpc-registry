---
layout: container
name:  "quay.io/biocontainers/nanosv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanosv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanosv/container.yaml"
updated_at: "2022-10-27 01:03:03.115146"
latest: "1.2.4--py_0"
container_url: "https://biocontainers.pro/tools/nanosv"
aliases:
 - "NanoSV"
versions:
 - "1.2.4--py_0"
description: "shpc-registry automated BioContainers addition for nanosv"
config: {"url": "https://biocontainers.pro/tools/nanosv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanosv", "latest": {"1.2.4--py_0": "sha256:f1ebe015816151c89fc302a5719075f7703e466eb789d1961944b14198f47c2e"}, "tags": {"1.2.4--py_0": "sha256:f1ebe015816151c89fc302a5719075f7703e466eb789d1961944b14198f47c2e"}, "docker": "quay.io/biocontainers/nanosv", "aliases": {"NanoSV": "/usr/local/bin/NanoSV"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanosv.
shpc-registry automated BioContainers addition for nanosv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanosv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanosv:1.2.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanosv/1.2.4--py_0
$ module help quay.io/biocontainers/nanosv/1.2.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanosv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanosv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanosv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanosv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanosv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanosv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoSV

```bash
$ singularity exec <container> /usr/local/bin/NanoSV
$ podman run --it --rm --entrypoint /usr/local/bin/NanoSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoSV   -v ${PWD} -w ${PWD} <container> -c " $@"
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