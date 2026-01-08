---
layout: container
name:  "quay.io/biocontainers/mpboot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mpboot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mpboot/container.yaml"
updated_at: "2026-01-08 04:18:50.317562"
latest: "1.2--h503566f_0"
container_url: "https://biocontainers.pro/tools/mpboot"
aliases:
 - "mpboot"
 - "mpboot-avx"
versions:
 - "1.2--h503566f_0"
description: "singularity registry hpc automated addition for mpboot"
config: {"url": "https://biocontainers.pro/tools/mpboot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mpboot", "latest": {"1.2--h503566f_0": "sha256:642890074e5edc787319c717973b653234b65c5d9d9eedae3a8b32a78b5c8602"}, "tags": {"1.2--h503566f_0": "sha256:642890074e5edc787319c717973b653234b65c5d9d9eedae3a8b32a78b5c8602"}, "docker": "quay.io/biocontainers/mpboot", "aliases": {"mpboot": "/usr/local/bin/mpboot", "mpboot-avx": "/usr/local/bin/mpboot-avx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mpboot.
singularity registry hpc automated addition for mpboot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mpboot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mpboot:1.2--h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mpboot/1.2--h503566f_0
$ module help quay.io/biocontainers/mpboot/1.2--h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mpboot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mpboot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mpboot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mpboot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mpboot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mpboot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpboot

```bash
$ singularity exec <container> /usr/local/bin/mpboot
$ podman run --it --rm --entrypoint /usr/local/bin/mpboot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpboot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpboot-avx

```bash
$ singularity exec <container> /usr/local/bin/mpboot-avx
$ podman run --it --rm --entrypoint /usr/local/bin/mpboot-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpboot-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
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