---
layout: container
name:  "quay.io/biocontainers/fa-lint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fa-lint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fa-lint/container.yaml"
updated_at: "2026-01-20 04:00:05.363356"
latest: "1.2.0--he881be0_0"
container_url: "https://biocontainers.pro/tools/fa-lint"
aliases:
 - "fa-lint"
versions:
 - "1.0.0--he881be0_0"
 - "1.2.0--he881be0_0"
 - "1.1.0--he881be0_0"
description: "singularity registry hpc automated addition for fa-lint"
config: {"url": "https://biocontainers.pro/tools/fa-lint", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fa-lint", "latest": {"1.2.0--he881be0_0": "sha256:385eeb4ba9d9daa8b14b88b2d0e4f239f6bc9b4ef5957a9d6f0156a45670a001"}, "tags": {"1.0.0--he881be0_0": "sha256:a52da083275c9e35810e0cb374e50da8ebb7b8cc30c237d8e1abbe5d9f83a066", "1.2.0--he881be0_0": "sha256:385eeb4ba9d9daa8b14b88b2d0e4f239f6bc9b4ef5957a9d6f0156a45670a001", "1.1.0--he881be0_0": "sha256:9e42890ad53b4f8ab5d399ef41cd278f9f36795a2efcff6de138f240e6e4b417"}, "docker": "quay.io/biocontainers/fa-lint", "aliases": {"fa-lint": "/usr/local/bin/fa-lint"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fa-lint.
singularity registry hpc automated addition for fa-lint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fa-lint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fa-lint:1.2.0--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fa-lint/1.2.0--he881be0_0
$ module help quay.io/biocontainers/fa-lint/1.2.0--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fa-lint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fa-lint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fa-lint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fa-lint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fa-lint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fa-lint-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fa-lint

```bash
$ singularity exec <container> /usr/local/bin/fa-lint
$ podman run --it --rm --entrypoint /usr/local/bin/fa-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fa-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
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