---
layout: container
name:  "quay.io/biocontainers/kivvi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kivvi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kivvi/container.yaml"
updated_at: "2026-06-29 07:01:22.479415"
latest: "1.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/kivvi"
aliases:
 - "kivvi"
versions:
 - "1.0.0--h9ee0642_0"
description: "singularity registry hpc automated addition for kivvi"
config: {"url": "https://biocontainers.pro/tools/kivvi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kivvi", "latest": {"1.0.0--h9ee0642_0": "sha256:1bc35feab18b0027277aebed7f11e11fa3bcb58f930441d6d2acb7608f37359b"}, "tags": {"1.0.0--h9ee0642_0": "sha256:1bc35feab18b0027277aebed7f11e11fa3bcb58f930441d6d2acb7608f37359b"}, "docker": "quay.io/biocontainers/kivvi", "aliases": {"kivvi": "/usr/local/bin/kivvi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kivvi.
singularity registry hpc automated addition for kivvi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kivvi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kivvi:1.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kivvi/1.0.0--h9ee0642_0
$ module help quay.io/biocontainers/kivvi/1.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kivvi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kivvi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kivvi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kivvi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kivvi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kivvi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kivvi

```bash
$ singularity exec <container> /usr/local/bin/kivvi
$ podman run --it --rm --entrypoint /usr/local/bin/kivvi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kivvi   -v ${PWD} -w ${PWD} <container> -c " $@"
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