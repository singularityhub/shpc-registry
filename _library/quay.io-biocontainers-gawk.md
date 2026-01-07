---
layout: container
name:  "quay.io/biocontainers/gawk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gawk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gawk/container.yaml"
updated_at: "2026-01-07 04:34:41.723782"
latest: "5.3.1"
container_url: "https://biocontainers.pro/tools/gawk"
aliases:
 - "gawk"
 - "gawk-5.1.0"
 - "awk"
versions:
 - "5.1.0"
 - "5.3.0"
 - "5.3.1"
 - "5.1.0--2"
description: "shpc-registry automated BioContainers addition for gawk"
config: {"url": "https://biocontainers.pro/tools/gawk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gawk", "latest": {"5.3.1": "sha256:14649372ffb4ac76e26ac7357262f2cdd3d731ace344118ad0ce79fc49f03a9d"}, "tags": {"5.1.0": "sha256:9d300f3d0a35fb059e3952ce01b3b108d595d0a9e943f156dce7c078bb8617aa", "5.3.0": "sha256:701d6199235b36d054c24b1d0a889ca5e9740e301e4b46651f54d59576b73cd0", "5.3.1": "sha256:14649372ffb4ac76e26ac7357262f2cdd3d731ace344118ad0ce79fc49f03a9d", "5.1.0--2": "sha256:592abd02d046e9ff0195252cbf398d6c0098be23de48ffb77f827c9ccdf77c93"}, "docker": "quay.io/biocontainers/gawk", "aliases": {"gawk": "/usr/local/bin/gawk", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gawk.
shpc-registry automated BioContainers addition for gawk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gawk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gawk:5.3.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gawk/5.3.1
$ module help quay.io/biocontainers/gawk/5.3.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gawk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gawk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gawk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gawk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gawk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gawk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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