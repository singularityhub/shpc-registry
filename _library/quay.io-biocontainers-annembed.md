---
layout: container
name:  "quay.io/biocontainers/annembed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/annembed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/annembed/container.yaml"
updated_at: "2025-10-02 04:10:44.644320"
latest: "0.2.5--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/annembed"
aliases:
 - "annembed"
versions:
 - "0.1.1--hdbdd923_0"
 - "0.1.2--hdbdd923_0"
 - "0.1.4--hdbdd923_0"
 - "0.1.7--hdbdd923_0"
 - "0.1.7--h503566f_1"
 - "0.1.9--h3ab6199_0"
 - "0.2.2--h3ab6199_0"
 - "0.2.4--hafc0c1d_0"
 - "0.2.5--h3ab6199_0"
description: "singularity registry hpc automated addition for annembed"
config: {"url": "https://biocontainers.pro/tools/annembed", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for annembed", "latest": {"0.2.5--h3ab6199_0": "sha256:b2ac7a5bb9e66b0b2085b11617d4de553bcc038d08d332ea50a48877de67895b"}, "tags": {"0.1.1--hdbdd923_0": "sha256:076f6e8d4dee428ac1a14e199fa64031735fca3b82e3366a5ea1bdcd4f7b929f", "0.1.2--hdbdd923_0": "sha256:35c900ef8a6e810d727a52c12ec21edda84c8e89c17633517990c9ac620cad2b", "0.1.4--hdbdd923_0": "sha256:d7caaaa5da81d9b5914d63030316d396d7260bd85969009c2ef6607c386479cf", "0.1.7--hdbdd923_0": "sha256:30b4285a24890b89b773c3e1bb021c67c6a17be2c2d34607e31724ececd104cd", "0.1.7--h503566f_1": "sha256:380bcfed8d6fe4f1f09d477cca7f874c03caed1997bcb9a6fcea79a0bc9296d6", "0.1.9--h3ab6199_0": "sha256:b2d83234af9d1b295b3d03cc3fd4ec5621a34ee86f5101feac99d4063f8cb5f1", "0.2.2--h3ab6199_0": "sha256:aaa581b26fe8b4265c2b86e5a9d2e80aac6fa51d467d916c18f13be521060df3", "0.2.4--hafc0c1d_0": "sha256:9a850bbb59c5d3f03022b9561dc24817070312f3a8b7ef8bff377f6a0310abb4", "0.2.5--h3ab6199_0": "sha256:b2ac7a5bb9e66b0b2085b11617d4de553bcc038d08d332ea50a48877de67895b"}, "docker": "quay.io/biocontainers/annembed", "aliases": {"annembed": "/usr/local/bin/annembed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/annembed.
singularity registry hpc automated addition for annembed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/annembed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/annembed:0.2.5--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/annembed/0.2.5--h3ab6199_0
$ module help quay.io/biocontainers/annembed/0.2.5--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### annembed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### annembed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### annembed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### annembed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### annembed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### annembed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annembed

```bash
$ singularity exec <container> /usr/local/bin/annembed
$ podman run --it --rm --entrypoint /usr/local/bin/annembed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annembed   -v ${PWD} -w ${PWD} <container> -c " $@"
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