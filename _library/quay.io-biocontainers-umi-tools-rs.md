---
layout: container
name:  "quay.io/biocontainers/umi-tools-rs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/umi-tools-rs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/umi-tools-rs/container.yaml"
updated_at: "2026-10-20 08:02:54.432195"
latest: "2.0.1--hec9b1f2_1"
container_url: "https://biocontainers.pro/tools/umi-tools-rs"
aliases:
 - "umi-tools-rs"
versions:
 - "1.1.0--hfa8f182_0"
 - "2.0.1--hec9b1f2_1"
 - "1.3.1--hfa8f182_0"
description: "singularity registry hpc automated addition for umi-tools-rs"
config: {"url": "https://biocontainers.pro/tools/umi-tools-rs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for umi-tools-rs", "latest": {"2.0.1--hec9b1f2_1": "sha256:fc8f0a5739c51c552c2cfdacbfce76815c0b31bd66c1419837fce73321d7cd86"}, "tags": {"1.1.0--hfa8f182_0": "sha256:297d684f8feff5d42f80c29ecc4f565b40efd0c745409a5f0ff3b01f6b243025", "2.0.1--hec9b1f2_1": "sha256:fc8f0a5739c51c552c2cfdacbfce76815c0b31bd66c1419837fce73321d7cd86", "1.3.1--hfa8f182_0": "sha256:08ccddc6b109d15218bdcfc6d8dee5b4e1d36e58c990715c99a74aceb60fe2cf"}, "docker": "quay.io/biocontainers/umi-tools-rs", "aliases": {"umi-tools-rs": "/usr/local/bin/umi-tools-rs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/umi-tools-rs.
singularity registry hpc automated addition for umi-tools-rs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/umi-tools-rs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/umi-tools-rs:2.0.1--hec9b1f2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/umi-tools-rs/2.0.1--hec9b1f2_1
$ module help quay.io/biocontainers/umi-tools-rs/2.0.1--hec9b1f2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umi-tools-rs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umi-tools-rs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umi-tools-rs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umi-tools-rs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umi-tools-rs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umi-tools-rs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### umi-tools-rs

```bash
$ singularity exec <container> /usr/local/bin/umi-tools-rs
$ podman run --it --rm --entrypoint /usr/local/bin/umi-tools-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/umi-tools-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
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