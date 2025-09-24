---
layout: container
name:  "quay.io/biocontainers/chromap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chromap/container.yaml"
updated_at: "2025-09-24 03:29:12.498745"
latest: "0.3.1--h077b44d_0"
container_url: "https://biocontainers.pro/tools/chromap"
aliases:
 - "chromap"
versions:
 - "0.2.3--hd03093a_1"
 - "0.2.4--hd03093a_0"
 - "0.2.5--hd03093a_0"
 - "0.2.5--hdcf5f25_2"
 - "0.2.6--hdcf5f25_0"
 - "0.2.6--hdcf5f25_1"
 - "0.2.7--hdcf5f25_0"
 - "0.2.7--h077b44d_1"
 - "0.3.0--h077b44d_0"
 - "0.3.1--h077b44d_0"
description: "shpc-registry automated BioContainers addition for chromap"
config: {"url": "https://biocontainers.pro/tools/chromap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chromap", "latest": {"0.3.1--h077b44d_0": "sha256:9ad835c99a35953f58f45fdb881b4df01d66a695409654296e4b20cfa554f2bb"}, "tags": {"0.2.3--hd03093a_1": "sha256:9a8e62c7881cb59f42978d78eb55934ea11fd4fbfc01d0964b92dbf08e43e22c", "0.2.4--hd03093a_0": "sha256:99f71d1d070f2eb285603971b218f3b70c07c62d4ae708a59f42ea508a7df024", "0.2.5--hd03093a_0": "sha256:ffe3bf3e17307675d5c6b338e8fcd26060865f51f6e43f2d9e6fadd1aa7d417d", "0.2.5--hdcf5f25_2": "sha256:d2dd59fca3f31a7bdaf508891e5e9a60ead3c1c205f427f0f7a2533ce38d62cb", "0.2.6--hdcf5f25_0": "sha256:18fca6050c753e2108eb511f8b7a62f90f483ef9a1b6dcbede853572940bb70b", "0.2.6--hdcf5f25_1": "sha256:a06f546cba81598ff5e6e8ee73e0443e003713bf134b7f66026518aa96cb2abf", "0.2.7--hdcf5f25_0": "sha256:440a3bbe526e007fbed5856f3e8109ea48a25d4adbb630f175449b017b8e0fc2", "0.2.7--h077b44d_1": "sha256:3e02bdbc18ca4762e1c9b95a97b1a766871433451a051483d4b7c5f4a11123c0", "0.3.0--h077b44d_0": "sha256:5ed9054988b9d52cb11ce3f9f76526a623a8be02aa116836711b9865d5324fc2", "0.3.1--h077b44d_0": "sha256:9ad835c99a35953f58f45fdb881b4df01d66a695409654296e4b20cfa554f2bb"}, "docker": "quay.io/biocontainers/chromap", "aliases": {"chromap": "/usr/local/bin/chromap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromap.
shpc-registry automated BioContainers addition for chromap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromap:0.3.1--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromap/0.3.1--h077b44d_0
$ module help quay.io/biocontainers/chromap/0.3.1--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chromap

```bash
$ singularity exec <container> /usr/local/bin/chromap
$ podman run --it --rm --entrypoint /usr/local/bin/chromap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chromap   -v ${PWD} -w ${PWD} <container> -c " $@"
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