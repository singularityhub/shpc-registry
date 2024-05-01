---
layout: container
name:  "quay.io/biocontainers/jemalloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jemalloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jemalloc/container.yaml"
updated_at: "2024-05-01 02:30:52.054788"
latest: "4.5.0--0"
container_url: "https://biocontainers.pro/tools/jemalloc"
aliases:
 - "jemalloc-config"
 - "jemalloc.sh"
 - "jeprof"
versions:
 - "4.5.0--0"
description: "shpc-registry automated BioContainers addition for jemalloc"
config: {"url": "https://biocontainers.pro/tools/jemalloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jemalloc", "latest": {"4.5.0--0": "sha256:49e412d7729504491acd4e8228db710436cb87c0ae6243a5a2691df4c328af30"}, "tags": {"4.5.0--0": "sha256:49e412d7729504491acd4e8228db710436cb87c0ae6243a5a2691df4c328af30"}, "docker": "quay.io/biocontainers/jemalloc", "aliases": {"jemalloc-config": "/usr/local/bin/jemalloc-config", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "jeprof": "/usr/local/bin/jeprof"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jemalloc.
shpc-registry automated BioContainers addition for jemalloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jemalloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jemalloc:4.5.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jemalloc/4.5.0--0
$ module help quay.io/biocontainers/jemalloc/4.5.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jemalloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jemalloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jemalloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jemalloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jemalloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jemalloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
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