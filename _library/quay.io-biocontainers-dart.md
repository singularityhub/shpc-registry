---
layout: container
name:  "quay.io/biocontainers/dart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dart/container.yaml"
updated_at: "2023-02-09 03:15:08.169903"
latest: "1.4.6--h2ccddb4_2"
container_url: "https://biocontainers.pro/tools/dart"
aliases:
 - "bwt_index"
 - "dart"
versions:
 - "1.4.6--h2ccddb4_2"
description: "shpc-registry automated BioContainers addition for dart"
config: {"url": "https://biocontainers.pro/tools/dart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dart", "latest": {"1.4.6--h2ccddb4_2": "sha256:b614e86b5f3d13eecb280fba216d6a541ddd1a779ea727ce1b13a6d5287d477e"}, "tags": {"1.4.6--h2ccddb4_2": "sha256:b614e86b5f3d13eecb280fba216d6a541ddd1a779ea727ce1b13a6d5287d477e"}, "docker": "quay.io/biocontainers/dart", "aliases": {"bwt_index": "/usr/local/bin/bwt_index", "dart": "/usr/local/bin/dart"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dart.
shpc-registry automated BioContainers addition for dart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dart:1.4.6--h2ccddb4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dart/1.4.6--h2ccddb4_2
$ module help quay.io/biocontainers/dart/1.4.6--h2ccddb4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwt_index

```bash
$ singularity exec <container> /usr/local/bin/bwt_index
$ podman run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dart

```bash
$ singularity exec <container> /usr/local/bin/dart
$ podman run --it --rm --entrypoint /usr/local/bin/dart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dart   -v ${PWD} -w ${PWD} <container> -c " $@"
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