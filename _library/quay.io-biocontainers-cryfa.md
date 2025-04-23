---
layout: container
name:  "quay.io/biocontainers/cryfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cryfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cryfa/container.yaml"
updated_at: "2025-04-23 03:36:52.669702"
latest: "20.04--h9948957_3"
container_url: "https://biocontainers.pro/tools/cryfa"
aliases:
 - "cryfa"
 - "keygen"
versions:
 - "20.04--h9f5acd7_0"
 - "20.04--h9f5acd7_1"
 - "20.04--h4ac6f70_2"
 - "20.04--h9948957_3"
description: "shpc-registry automated BioContainers addition for cryfa"
config: {"url": "https://biocontainers.pro/tools/cryfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cryfa", "latest": {"20.04--h9948957_3": "sha256:d350c639c942976536b6601c491c0c53ebd5809d170c809589b289d8576b7d02"}, "tags": {"20.04--h9f5acd7_0": "sha256:d1a135e085c6aaf1189ec55e534b36699171578bd9b2df1476da8f95736f4f20", "20.04--h9f5acd7_1": "sha256:b35791684e15295a3e7f3854ac637ff722c1a1724fd2268e821c332e1bd541ee", "20.04--h4ac6f70_2": "sha256:041708c397f34e61cd008bc6a44628601e4fe0f1b8672cf32f4a648eaad3473b", "20.04--h9948957_3": "sha256:d350c639c942976536b6601c491c0c53ebd5809d170c809589b289d8576b7d02"}, "docker": "quay.io/biocontainers/cryfa", "aliases": {"cryfa": "/usr/local/bin/cryfa", "keygen": "/usr/local/bin/keygen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cryfa.
shpc-registry automated BioContainers addition for cryfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cryfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cryfa:20.04--h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cryfa/20.04--h9948957_3
$ module help quay.io/biocontainers/cryfa/20.04--h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cryfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cryfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cryfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cryfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cryfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cryfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cryfa

```bash
$ singularity exec <container> /usr/local/bin/cryfa
$ podman run --it --rm --entrypoint /usr/local/bin/cryfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cryfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keygen

```bash
$ singularity exec <container> /usr/local/bin/keygen
$ podman run --it --rm --entrypoint /usr/local/bin/keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
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