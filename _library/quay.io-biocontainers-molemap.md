---
layout: container
name:  "quay.io/biocontainers/molemap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/molemap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/molemap/container.yaml"
updated_at: "2026-06-17 07:23:29.648629"
latest: "1.4.3.1--h5814d7d_0"
container_url: "https://biocontainers.pro/tools/molemap"
aliases:
 - "molemap"
versions:
 - "1.4.3.1--h5814d7d_0"
description: "singularity registry hpc automated addition for molemap"
config: {"url": "https://biocontainers.pro/tools/molemap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for molemap", "latest": {"1.4.3.1--h5814d7d_0": "sha256:468acceeeb9f65b2ef627724bb41efaeeaf0a593e8d0449ce1592b6f162c4867"}, "tags": {"1.4.3.1--h5814d7d_0": "sha256:468acceeeb9f65b2ef627724bb41efaeeaf0a593e8d0449ce1592b6f162c4867"}, "docker": "quay.io/biocontainers/molemap", "aliases": {"molemap": "/usr/local/bin/molemap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/molemap.
singularity registry hpc automated addition for molemap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/molemap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/molemap:1.4.3.1--h5814d7d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/molemap/1.4.3.1--h5814d7d_0
$ module help quay.io/biocontainers/molemap/1.4.3.1--h5814d7d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### molemap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### molemap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### molemap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### molemap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### molemap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### molemap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### molemap

```bash
$ singularity exec <container> /usr/local/bin/molemap
$ podman run --it --rm --entrypoint /usr/local/bin/molemap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/molemap   -v ${PWD} -w ${PWD} <container> -c " $@"
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