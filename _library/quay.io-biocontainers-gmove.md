---
layout: container
name:  "quay.io/biocontainers/gmove"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmove/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmove/container.yaml"
updated_at: "2025-12-19 04:14:02.921664"
latest: "1.3--h9948957_0"
container_url: "https://biocontainers.pro/tools/gmove"
aliases:
 - "gmove"
versions:
 - "1.3--h9948957_0"
description: "singularity registry hpc automated addition for gmove"
config: {"url": "https://biocontainers.pro/tools/gmove", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gmove", "latest": {"1.3--h9948957_0": "sha256:2b00cfc135aaa36fb4e7c1a713d74b5e714e257053b2da97e35c4541cc99c3a4"}, "tags": {"1.3--h9948957_0": "sha256:2b00cfc135aaa36fb4e7c1a713d74b5e714e257053b2da97e35c4541cc99c3a4"}, "docker": "quay.io/biocontainers/gmove", "aliases": {"gmove": "/usr/local/bin/gmove"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmove.
singularity registry hpc automated addition for gmove
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmove
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmove:1.3--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmove/1.3--h9948957_0
$ module help quay.io/biocontainers/gmove/1.3--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmove-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmove-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmove-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmove-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmove-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmove-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gmove

```bash
$ singularity exec <container> /usr/local/bin/gmove
$ podman run --it --rm --entrypoint /usr/local/bin/gmove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmove   -v ${PWD} -w ${PWD} <container> -c " $@"
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