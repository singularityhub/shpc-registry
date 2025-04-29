---
layout: container
name:  "quay.io/biocontainers/apoc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/apoc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/apoc/container.yaml"
updated_at: "2025-04-29 03:43:49.511669"
latest: "1b16--hb48dae3_4"
container_url: "https://biocontainers.pro/tools/apoc"
aliases:
 - "apoc"
versions:
 - "1b16--hb48dae3_4"
description: "shpc-registry automated BioContainers addition for apoc"
config: {"url": "https://biocontainers.pro/tools/apoc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for apoc", "latest": {"1b16--hb48dae3_4": "sha256:6b3f95c0e85853011293032cee4f5a2d1f42e6dd46481a2fd59ad7f585e5a2a7"}, "tags": {"1b16--hb48dae3_4": "sha256:6b3f95c0e85853011293032cee4f5a2d1f42e6dd46481a2fd59ad7f585e5a2a7"}, "docker": "quay.io/biocontainers/apoc", "aliases": {"apoc": "/usr/local/bin/apoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/apoc.
shpc-registry automated BioContainers addition for apoc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/apoc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/apoc:1b16--hb48dae3_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/apoc/1b16--hb48dae3_4
$ module help quay.io/biocontainers/apoc/1b16--hb48dae3_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### apoc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### apoc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### apoc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### apoc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### apoc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### apoc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### apoc

```bash
$ singularity exec <container> /usr/local/bin/apoc
$ podman run --it --rm --entrypoint /usr/local/bin/apoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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