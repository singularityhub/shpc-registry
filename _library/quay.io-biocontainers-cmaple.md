---
layout: container
name:  "quay.io/biocontainers/cmaple"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmaple/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmaple/container.yaml"
updated_at: "2025-02-07 03:29:00.079699"
latest: "1.1.0--h503566f_1"
container_url: "https://biocontainers.pro/tools/cmaple"
aliases:
 - "cmaple"
 - "cmaple-aa"
versions:
 - "1.0.0--hdbdd923_0"
 - "1.0.0--hdbdd923_1"
 - "1.1.0--hdbdd923_0"
 - "1.1.0--h503566f_1"
description: "singularity registry hpc automated addition for cmaple"
config: {"url": "https://biocontainers.pro/tools/cmaple", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cmaple", "latest": {"1.1.0--h503566f_1": "sha256:2290811cd20cd1e00b1c479497439286df0070aaf9ab06d02771f39918bd3433"}, "tags": {"1.0.0--hdbdd923_0": "sha256:68edc82dc07544bfabdfd4753d5a35ada7c13c2462ccc2d370819e6d0b2f7378", "1.0.0--hdbdd923_1": "sha256:154b5f98bf60f01f48e99bcfaa8209c6e69ddcd06009ccb46f2876517b696f38", "1.1.0--hdbdd923_0": "sha256:4306a76ad1bf9bda7641f8a6c8203485e9afd374823b72af419cdbdf19365a22", "1.1.0--h503566f_1": "sha256:2290811cd20cd1e00b1c479497439286df0070aaf9ab06d02771f39918bd3433"}, "docker": "quay.io/biocontainers/cmaple", "aliases": {"cmaple": "/usr/local/bin/cmaple", "cmaple-aa": "/usr/local/bin/cmaple-aa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmaple.
singularity registry hpc automated addition for cmaple
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmaple
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmaple:1.1.0--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmaple/1.1.0--h503566f_1
$ module help quay.io/biocontainers/cmaple/1.1.0--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmaple-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmaple-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmaple-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmaple-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmaple-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmaple-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cmaple

```bash
$ singularity exec <container> /usr/local/bin/cmaple
$ podman run --it --rm --entrypoint /usr/local/bin/cmaple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmaple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmaple-aa

```bash
$ singularity exec <container> /usr/local/bin/cmaple-aa
$ podman run --it --rm --entrypoint /usr/local/bin/cmaple-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmaple-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
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