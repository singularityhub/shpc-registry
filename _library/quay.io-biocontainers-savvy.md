---
layout: container
name:  "quay.io/biocontainers/savvy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/savvy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/savvy/container.yaml"
updated_at: "2023-09-12 03:08:52.143404"
latest: "2.1.0--h40c17d1_2"
container_url: "https://biocontainers.pro/tools/savvy"
aliases:
 - "sav"
versions:
 - "2.1.0--hfb1f815_0"
 - "2.1.0--h40c17d1_2"
description: "shpc-registry automated BioContainers addition for savvy"
config: {"url": "https://biocontainers.pro/tools/savvy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for savvy", "latest": {"2.1.0--h40c17d1_2": "sha256:112dd22d4f335d43251e3b2a9da3426c4528b39fafe2e459028c6e4d9e74953f"}, "tags": {"2.1.0--hfb1f815_0": "sha256:afdc978ed9c748ad990268a507b0140d99246e5c3d918a99e90d9b576213429b", "2.1.0--h40c17d1_2": "sha256:112dd22d4f335d43251e3b2a9da3426c4528b39fafe2e459028c6e4d9e74953f"}, "docker": "quay.io/biocontainers/savvy", "aliases": {"sav": "/usr/local/bin/sav"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/savvy.
shpc-registry automated BioContainers addition for savvy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/savvy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/savvy:2.1.0--h40c17d1_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/savvy/2.1.0--h40c17d1_2
$ module help quay.io/biocontainers/savvy/2.1.0--h40c17d1_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### savvy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### savvy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### savvy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### savvy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### savvy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### savvy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sav

```bash
$ singularity exec <container> /usr/local/bin/sav
$ podman run --it --rm --entrypoint /usr/local/bin/sav   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sav   -v ${PWD} -w ${PWD} <container> -c " $@"
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