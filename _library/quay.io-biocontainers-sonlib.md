---
layout: container
name:  "quay.io/biocontainers/sonlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sonlib/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sonlib/container.yaml"
updated_at: "2022-10-27 00:52:02.654802"
latest: "1.1.0--py_2"
container_url: "https://biocontainers.pro/tools/sonlib"

versions:
 - "1.1.0--py_2"
description: "shpc-registry automated BioContainers addition for sonlib"
config: {"url": "https://biocontainers.pro/tools/sonlib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sonlib", "latest": {"1.1.0--py_2": "sha256:0edb4b58190e1a330acf9693e029add6ba497ffc0a562302ce2796ff5d5444cf"}, "tags": {"1.1.0--py_2": "sha256:0edb4b58190e1a330acf9693e029add6ba497ffc0a562302ce2796ff5d5444cf"}, "docker": "quay.io/biocontainers/sonlib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sonlib.
shpc-registry automated BioContainers addition for sonlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sonlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sonlib:1.1.0--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sonlib/1.1.0--py_2
$ module help quay.io/biocontainers/sonlib/1.1.0--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sonlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sonlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sonlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sonlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sonlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sonlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sonlib

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