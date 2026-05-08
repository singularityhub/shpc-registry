---
layout: container
name:  "quay.io/biocontainers/eggs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eggs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eggs/container.yaml"
updated_at: "2026-05-08 05:39:03.472730"
latest: "1.0.0--hb7acf71_0"
container_url: "https://biocontainers.pro/tools/eggs"
aliases:
 - "eggs"
versions:
 - "1.0.0--hb7acf71_0"
description: "singularity registry hpc automated addition for eggs"
config: {"url": "https://biocontainers.pro/tools/eggs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for eggs", "latest": {"1.0.0--hb7acf71_0": "sha256:f8c24644062f61167c6e110a6c55b0c35dfa47aa0b16a17a39567130a1d78ad3"}, "tags": {"1.0.0--hb7acf71_0": "sha256:f8c24644062f61167c6e110a6c55b0c35dfa47aa0b16a17a39567130a1d78ad3"}, "docker": "quay.io/biocontainers/eggs", "aliases": {"eggs": "/usr/local/bin/eggs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eggs.
singularity registry hpc automated addition for eggs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eggs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eggs:1.0.0--hb7acf71_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eggs/1.0.0--hb7acf71_0
$ module help quay.io/biocontainers/eggs/1.0.0--hb7acf71_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eggs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eggs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eggs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eggs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eggs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eggs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eggs

```bash
$ singularity exec <container> /usr/local/bin/eggs
$ podman run --it --rm --entrypoint /usr/local/bin/eggs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eggs   -v ${PWD} -w ${PWD} <container> -c " $@"
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