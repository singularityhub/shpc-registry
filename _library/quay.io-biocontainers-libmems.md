---
layout: container
name:  "quay.io/biocontainers/libmems"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libmems/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libmems/container.yaml"
updated_at: "2025-08-31 03:22:15.390485"
latest: "1.6.0--h9948957_8"
container_url: "https://biocontainers.pro/tools/libmems"

versions:
 - "1.6.0--h2df963e_5"
 - "1.6.0--h376f1d3_6"
 - "1.6.0--h9948957_8"
description: "shpc-registry automated BioContainers addition for libmems"
config: {"url": "https://biocontainers.pro/tools/libmems", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libmems", "latest": {"1.6.0--h9948957_8": "sha256:3b9e6757ec2636790397ff81ae1ed3ba1b40aa486a114a7c439c2a80bb8602e6"}, "tags": {"1.6.0--h2df963e_5": "sha256:786d03bdadf29715ee462ee37bd95472e8e20f3c082d4f6724622bfe9db086e0", "1.6.0--h376f1d3_6": "sha256:98e3fdf02207775549ef6188e5a48e06482fcde2f56077787b539609bb18d15f", "1.6.0--h9948957_8": "sha256:3b9e6757ec2636790397ff81ae1ed3ba1b40aa486a114a7c439c2a80bb8602e6"}, "docker": "quay.io/biocontainers/libmems"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libmems.
shpc-registry automated BioContainers addition for libmems
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libmems
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libmems:1.6.0--h9948957_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libmems/1.6.0--h9948957_8
$ module help quay.io/biocontainers/libmems/1.6.0--h9948957_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libmems-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libmems-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libmems-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libmems-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libmems-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libmems-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libmems

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