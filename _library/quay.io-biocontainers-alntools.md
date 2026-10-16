---
layout: container
name:  "quay.io/biocontainers/alntools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alntools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alntools/container.yaml"
updated_at: "2026-10-16 06:51:10.842484"
latest: "1.0--h118bc1c_0"
container_url: "https://biocontainers.pro/tools/alntools"
aliases:
 - "gdbmask"
 - "svfind"
 - "taco"
 - "tanbed"
versions:
 - "1.0--h118bc1c_0"
description: "singularity registry hpc automated addition for alntools"
config: {"url": "https://biocontainers.pro/tools/alntools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alntools", "latest": {"1.0--h118bc1c_0": "sha256:d7e6db6feb8ee8cbae137ab5b681bd67f5fabaef82eb220b61a8b678daa33a1f"}, "tags": {"1.0--h118bc1c_0": "sha256:d7e6db6feb8ee8cbae137ab5b681bd67f5fabaef82eb220b61a8b678daa33a1f"}, "docker": "quay.io/biocontainers/alntools", "aliases": {"gdbmask": "/usr/local/bin/gdbmask", "svfind": "/usr/local/bin/svfind", "taco": "/usr/local/bin/taco", "tanbed": "/usr/local/bin/tanbed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alntools.
singularity registry hpc automated addition for alntools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alntools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alntools:1.0--h118bc1c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alntools/1.0--h118bc1c_0
$ module help quay.io/biocontainers/alntools/1.0--h118bc1c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alntools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alntools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alntools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alntools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alntools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alntools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdbmask

```bash
$ singularity exec <container> /usr/local/bin/gdbmask
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svfind

```bash
$ singularity exec <container> /usr/local/bin/svfind
$ podman run --it --rm --entrypoint /usr/local/bin/svfind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svfind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taco

```bash
$ singularity exec <container> /usr/local/bin/taco
$ podman run --it --rm --entrypoint /usr/local/bin/taco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tanbed

```bash
$ singularity exec <container> /usr/local/bin/tanbed
$ podman run --it --rm --entrypoint /usr/local/bin/tanbed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tanbed   -v ${PWD} -w ${PWD} <container> -c " $@"
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