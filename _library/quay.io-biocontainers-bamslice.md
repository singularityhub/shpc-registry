---
layout: container
name:  "quay.io/biocontainers/bamslice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamslice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamslice/container.yaml"
updated_at: "2025-12-12 03:33:04.237756"
latest: "0.1.6--h67a98e6_0"
container_url: "https://biocontainers.pro/tools/bamslice"
aliases:
 - "bamslice"
versions:
 - "0.1.0--h67a98e6_0"
 - "0.1.6--h67a98e6_0"
description: "singularity registry hpc automated addition for bamslice"
config: {"url": "https://biocontainers.pro/tools/bamslice", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bamslice", "latest": {"0.1.6--h67a98e6_0": "sha256:e240f0657bf7a4aee451fa7508fc6a90a4c0366d836d1de5719e263747717268"}, "tags": {"0.1.0--h67a98e6_0": "sha256:bd2c89bfe07f8f2f385b236bd5f5918d002ba77d7c457287c92950b71e7922a9", "0.1.6--h67a98e6_0": "sha256:e240f0657bf7a4aee451fa7508fc6a90a4c0366d836d1de5719e263747717268"}, "docker": "quay.io/biocontainers/bamslice", "aliases": {"bamslice": "/usr/local/bin/bamslice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamslice.
singularity registry hpc automated addition for bamslice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamslice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamslice:0.1.6--h67a98e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamslice/0.1.6--h67a98e6_0
$ module help quay.io/biocontainers/bamslice/0.1.6--h67a98e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamslice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamslice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamslice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamslice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamslice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamslice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamslice

```bash
$ singularity exec <container> /usr/local/bin/bamslice
$ podman run --it --rm --entrypoint /usr/local/bin/bamslice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamslice   -v ${PWD} -w ${PWD} <container> -c " $@"
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