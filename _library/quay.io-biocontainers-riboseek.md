---
layout: container
name:  "quay.io/biocontainers/riboseek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riboseek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riboseek/container.yaml"
updated_at: "2026-08-21 15:39:10.341200"
latest: "1.0.0--he833c27_0"
container_url: "https://biocontainers.pro/tools/riboseek"
aliases:
 - "gawk-5.4.1"
 - "riboseek"
 - "aria2c"
 - "gawkbug"
 - "gawk"
 - "awk"
versions:
 - "1.0.0--he833c27_0"
description: "singularity registry hpc automated addition for riboseek"
config: {"url": "https://biocontainers.pro/tools/riboseek", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for riboseek", "latest": {"1.0.0--he833c27_0": "sha256:57b7b1334ef41cc101d8be62cb1eb48aff99a85223345ec1a1e0783f57b2ed31"}, "tags": {"1.0.0--he833c27_0": "sha256:57b7b1334ef41cc101d8be62cb1eb48aff99a85223345ec1a1e0783f57b2ed31"}, "docker": "quay.io/biocontainers/riboseek", "aliases": {"gawk-5.4.1": "/usr/local/bin/gawk-5.4.1", "riboseek": "/usr/local/bin/riboseek", "aria2c": "/usr/local/bin/aria2c", "gawkbug": "/usr/local/bin/gawkbug", "gawk": "/usr/local/bin/gawk", "awk": "/usr/local/bin/awk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riboseek.
singularity registry hpc automated addition for riboseek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riboseek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riboseek:1.0.0--he833c27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riboseek/1.0.0--he833c27_0
$ module help quay.io/biocontainers/riboseek/1.0.0--he833c27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riboseek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riboseek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riboseek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riboseek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riboseek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riboseek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.4.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### riboseek

```bash
$ singularity exec <container> /usr/local/bin/riboseek
$ podman run --it --rm --entrypoint /usr/local/bin/riboseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/riboseek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
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