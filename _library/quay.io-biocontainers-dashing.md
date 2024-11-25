---
layout: container
name:  "quay.io/biocontainers/dashing"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dashing/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dashing/container.yaml"
updated_at: "2024-11-25 03:54:15.002608"
latest: "1.0--h40c17d1_2"
container_url: "https://biocontainers.pro/tools/dashing"
aliases:
 - "dashing"
versions:
 - "1.0--hfb1f815_0"
 - "1.0--h40c17d1_2"
description: "shpc-registry automated BioContainers addition for dashing"
config: {"url": "https://biocontainers.pro/tools/dashing", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dashing", "latest": {"1.0--h40c17d1_2": "sha256:45bd9d1a9be72f433438416c5deea42ccdfe018abeb205c73b1a0407cd58d28c"}, "tags": {"1.0--hfb1f815_0": "sha256:c9d7eacebbd93f4cd248c921d16f592d5674d022abfc6d09810748f22494084d", "1.0--h40c17d1_2": "sha256:45bd9d1a9be72f433438416c5deea42ccdfe018abeb205c73b1a0407cd58d28c"}, "docker": "quay.io/biocontainers/dashing", "aliases": {"dashing": "/usr/local/bin/dashing"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dashing.
shpc-registry automated BioContainers addition for dashing
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dashing
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dashing:1.0--h40c17d1_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dashing/1.0--h40c17d1_2
$ module help quay.io/biocontainers/dashing/1.0--h40c17d1_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dashing-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dashing-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dashing-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dashing-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dashing-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dashing-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dashing

```bash
$ singularity exec <container> /usr/local/bin/dashing
$ podman run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
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