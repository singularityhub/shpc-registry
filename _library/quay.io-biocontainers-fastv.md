---
layout: container
name:  "quay.io/biocontainers/fastv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastv/container.yaml"
updated_at: "2025-02-18 03:23:44.159442"
latest: "0.10.0--h077b44d_1"
container_url: "https://biocontainers.pro/tools/fastv"
aliases:
 - "fastv"
versions:
 - "0.8.1--hd03093a_2"
 - "0.8.1--hdcf5f25_4"
 - "0.10.0--hdcf5f25_0"
 - "0.10.0--h077b44d_1"
description: "shpc-registry automated BioContainers addition for fastv"
config: {"url": "https://biocontainers.pro/tools/fastv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastv", "latest": {"0.10.0--h077b44d_1": "sha256:0e4dac76b1104ffb90f5086d420e00cfec78c528d8662f061a7d71b6963a2bf1"}, "tags": {"0.8.1--hd03093a_2": "sha256:4b64e899b424ad47bb4f6adbd0c067329be1717028472ad89a01d09eb9aaf73e", "0.8.1--hdcf5f25_4": "sha256:ec01cb0c9a360bc308d5ce09a69244256fdfd20d5aaf0f9f5a0b954335a748ba", "0.10.0--hdcf5f25_0": "sha256:b5ad30dea34e6a41f128ddfc1f0caa60338c718a54efc078a708960fe6b3c082", "0.10.0--h077b44d_1": "sha256:0e4dac76b1104ffb90f5086d420e00cfec78c528d8662f061a7d71b6963a2bf1"}, "docker": "quay.io/biocontainers/fastv", "aliases": {"fastv": "/usr/local/bin/fastv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastv.
shpc-registry automated BioContainers addition for fastv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastv:0.10.0--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastv/0.10.0--h077b44d_1
$ module help quay.io/biocontainers/fastv/0.10.0--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastv

```bash
$ singularity exec <container> /usr/local/bin/fastv
$ podman run --it --rm --entrypoint /usr/local/bin/fastv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastv   -v ${PWD} -w ${PWD} <container> -c " $@"
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