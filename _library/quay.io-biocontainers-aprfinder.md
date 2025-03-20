---
layout: container
name:  "quay.io/biocontainers/aprfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aprfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aprfinder/container.yaml"
updated_at: "2025-03-20 03:28:34.468648"
latest: "1.5--h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/aprfinder"
aliases:
 - "aprfinder"
versions:
 - "1.5--hec16e2b_0"
 - "1.5--h031d066_2"
 - "1.5--h7b50bb2_3"
description: "singularity registry hpc automated addition for aprfinder"
config: {"url": "https://biocontainers.pro/tools/aprfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aprfinder", "latest": {"1.5--h7b50bb2_3": "sha256:b7c4d8e933310e8cb252deb6d56ce3b79836ddc3ed84c79bc2e9d0f4b0d63c27"}, "tags": {"1.5--hec16e2b_0": "sha256:34baea9d56a6db9076a1482fe75a94e54c16264c8732f7d482c1a6f92af97399", "1.5--h031d066_2": "sha256:b42cdfa8593b0eca5d36583ead2d64025699704e1eba274124c70166dedcf81a", "1.5--h7b50bb2_3": "sha256:b7c4d8e933310e8cb252deb6d56ce3b79836ddc3ed84c79bc2e9d0f4b0d63c27"}, "docker": "quay.io/biocontainers/aprfinder", "aliases": {"aprfinder": "/usr/local/bin/aprfinder"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aprfinder.
singularity registry hpc automated addition for aprfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aprfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aprfinder:1.5--h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aprfinder/1.5--h7b50bb2_3
$ module help quay.io/biocontainers/aprfinder/1.5--h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aprfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aprfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aprfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aprfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aprfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aprfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aprfinder

```bash
$ singularity exec <container> /usr/local/bin/aprfinder
$ podman run --it --rm --entrypoint /usr/local/bin/aprfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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