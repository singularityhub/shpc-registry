---
layout: container
name:  "quay.io/biocontainers/tagbam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tagbam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tagbam/container.yaml"
updated_at: "2025-04-03 03:11:33.445515"
latest: "0.1.0--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/tagbam"
aliases:
 - "tagbam"
versions:
 - "0.1.0--h3ab6199_0"
description: "singularity registry hpc automated addition for tagbam"
config: {"url": "https://biocontainers.pro/tools/tagbam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tagbam", "latest": {"0.1.0--h3ab6199_0": "sha256:fc10ccbff69b190131a0be466fd586e652e4bc2a23f167e089bcebf8268a2d0a"}, "tags": {"0.1.0--h3ab6199_0": "sha256:fc10ccbff69b190131a0be466fd586e652e4bc2a23f167e089bcebf8268a2d0a"}, "docker": "quay.io/biocontainers/tagbam", "aliases": {"tagbam": "/usr/local/bin/tagbam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tagbam.
singularity registry hpc automated addition for tagbam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tagbam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tagbam:0.1.0--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tagbam/0.1.0--h3ab6199_0
$ module help quay.io/biocontainers/tagbam/0.1.0--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tagbam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tagbam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tagbam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tagbam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tagbam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tagbam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tagbam

```bash
$ singularity exec <container> /usr/local/bin/tagbam
$ podman run --it --rm --entrypoint /usr/local/bin/tagbam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tagbam   -v ${PWD} -w ${PWD} <container> -c " $@"
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