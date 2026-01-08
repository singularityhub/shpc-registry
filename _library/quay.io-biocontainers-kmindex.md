---
layout: container
name:  "quay.io/biocontainers/kmindex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmindex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmindex/container.yaml"
updated_at: "2026-01-08 04:17:12.815582"
latest: "0.6.0--h668145b_1"
container_url: "https://biocontainers.pro/tools/kmindex"
aliases:
 - "kmindex"
 - "kmindex-server"
 - "kmtricks"
versions:
 - "0.6.0--h668145b_1"
description: "singularity registry hpc automated addition for kmindex"
config: {"url": "https://biocontainers.pro/tools/kmindex", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmindex", "latest": {"0.6.0--h668145b_1": "sha256:af736c828c2da24cde3706ff65930162a1a62677bf25652c07f022e7f63b205a"}, "tags": {"0.6.0--h668145b_1": "sha256:af736c828c2da24cde3706ff65930162a1a62677bf25652c07f022e7f63b205a"}, "docker": "quay.io/biocontainers/kmindex", "aliases": {"kmindex": "/usr/local/bin/kmindex", "kmindex-server": "/usr/local/bin/kmindex-server", "kmtricks": "/usr/local/bin/kmtricks"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmindex.
singularity registry hpc automated addition for kmindex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmindex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmindex:0.6.0--h668145b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmindex/0.6.0--h668145b_1
$ module help quay.io/biocontainers/kmindex/0.6.0--h668145b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmindex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmindex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmindex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmindex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmindex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmindex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kmindex

```bash
$ singularity exec <container> /usr/local/bin/kmindex
$ podman run --it --rm --entrypoint /usr/local/bin/kmindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmindex-server

```bash
$ singularity exec <container> /usr/local/bin/kmindex-server
$ podman run --it --rm --entrypoint /usr/local/bin/kmindex-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmindex-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmtricks

```bash
$ singularity exec <container> /usr/local/bin/kmtricks
$ podman run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmtricks   -v ${PWD} -w ${PWD} <container> -c " $@"
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