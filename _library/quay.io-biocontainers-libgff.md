---
layout: container
name:  "quay.io/biocontainers/libgff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libgff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libgff/container.yaml"
updated_at: "2025-05-19 03:50:12.134235"
latest: "2.0.0--h077b44d_2"
container_url: "https://biocontainers.pro/tools/libgff"

versions:
 - "2.0.0--hdcf5f25_1"
 - "2.0.0--h077b44d_2"
description: "singularity registry hpc automated addition for libgff"
config: {"url": "https://biocontainers.pro/tools/libgff", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for libgff", "latest": {"2.0.0--h077b44d_2": "sha256:5b237df68d049a16820808b2f7fcb69c4c069cae7123a478805958970403f818"}, "tags": {"2.0.0--hdcf5f25_1": "sha256:b0c5240ace1f1803bbf5deb787d946f51734a04ba162ff51cc993a943bfadd6d", "2.0.0--h077b44d_2": "sha256:5b237df68d049a16820808b2f7fcb69c4c069cae7123a478805958970403f818"}, "docker": "quay.io/biocontainers/libgff"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libgff.
singularity registry hpc automated addition for libgff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libgff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libgff:2.0.0--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libgff/2.0.0--h077b44d_2
$ module help quay.io/biocontainers/libgff/2.0.0--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libgff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libgff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libgff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libgff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libgff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libgff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libgff

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