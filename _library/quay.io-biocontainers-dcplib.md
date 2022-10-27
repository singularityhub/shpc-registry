---
layout: container
name:  "quay.io/biocontainers/dcplib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dcplib/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dcplib/container.yaml"
updated_at: "2022-10-27 01:01:36.154978"
latest: "3.9.0--py_0"
container_url: "https://biocontainers.pro/tools/dcplib"

versions:
 - "3.9.0--py_0"
description: "shpc-registry automated BioContainers addition for dcplib"
config: {"url": "https://biocontainers.pro/tools/dcplib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dcplib", "latest": {"3.9.0--py_0": "sha256:d921504c7b662ed3f485355d6a578357c7832e539363f42ff5ee28108cd398b2"}, "tags": {"3.9.0--py_0": "sha256:d921504c7b662ed3f485355d6a578357c7832e539363f42ff5ee28108cd398b2"}, "docker": "quay.io/biocontainers/dcplib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/dcplib.
shpc-registry automated BioContainers addition for dcplib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dcplib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dcplib:3.9.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dcplib/3.9.0--py_0
$ module help quay.io/biocontainers/dcplib/3.9.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dcplib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dcplib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dcplib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dcplib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dcplib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dcplib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### dcplib

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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