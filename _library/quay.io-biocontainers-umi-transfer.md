---
layout: container
name:  "quay.io/biocontainers/umi-transfer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/umi-transfer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/umi-transfer/container.yaml"
updated_at: "2024-01-28 03:10:24.587250"
latest: "1.0.0"
container_url: "https://biocontainers.pro/tools/umi-transfer"
aliases:
 - "umi-transfer"
versions:
 - "1.0.0"
description: "singularity registry hpc automated addition for umi-transfer"
config: {"url": "https://biocontainers.pro/tools/umi-transfer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for umi-transfer", "latest": {"1.0.0": "sha256:af15b8502f9f7ea504e5f7f2372a7148bcb9bf97612530753a046e2726b115dd"}, "tags": {"1.0.0": "sha256:af15b8502f9f7ea504e5f7f2372a7148bcb9bf97612530753a046e2726b115dd"}, "docker": "quay.io/biocontainers/umi-transfer", "aliases": {"umi-transfer": "/usr/local/bin/umi-transfer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/umi-transfer.
singularity registry hpc automated addition for umi-transfer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/umi-transfer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/umi-transfer:1.0.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/umi-transfer/1.0.0
$ module help quay.io/biocontainers/umi-transfer/1.0.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umi-transfer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umi-transfer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umi-transfer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umi-transfer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umi-transfer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umi-transfer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### umi-transfer

```bash
$ singularity exec <container> /usr/local/bin/umi-transfer
$ podman run --it --rm --entrypoint /usr/local/bin/umi-transfer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/umi-transfer   -v ${PWD} -w ${PWD} <container> -c " $@"
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