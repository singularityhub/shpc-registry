---
layout: container
name:  "quay.io/biocontainers/hificnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hificnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hificnv/container.yaml"
updated_at: "2023-08-07 03:34:51.737220"
latest: "0.1.6b--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/hificnv"
aliases:
 - "hificnv"
versions:
 - "0.1.6b--h9ee0642_0"
description: "singularity registry hpc automated addition for hificnv"
config: {"url": "https://biocontainers.pro/tools/hificnv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hificnv", "latest": {"0.1.6b--h9ee0642_0": "sha256:760a600f74f1fc2f186fc1bbcc221eee2db14b0c1d46f666a0215da32d1a6afc"}, "tags": {"0.1.6b--h9ee0642_0": "sha256:760a600f74f1fc2f186fc1bbcc221eee2db14b0c1d46f666a0215da32d1a6afc"}, "docker": "quay.io/biocontainers/hificnv", "aliases": {"hificnv": "/usr/local/bin/hificnv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hificnv.
singularity registry hpc automated addition for hificnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hificnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hificnv:0.1.6b--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hificnv/0.1.6b--h9ee0642_0
$ module help quay.io/biocontainers/hificnv/0.1.6b--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hificnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hificnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hificnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hificnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hificnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hificnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hificnv

```bash
$ singularity exec <container> /usr/local/bin/hificnv
$ podman run --it --rm --entrypoint /usr/local/bin/hificnv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hificnv   -v ${PWD} -w ${PWD} <container> -c " $@"
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