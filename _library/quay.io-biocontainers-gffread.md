---
layout: container
name:  "quay.io/biocontainers/gffread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gffread/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gffread/container.yaml"
updated_at: "2022-11-01 03:37:33.826267"
latest: "0.9.9--1"
container_url: "https://biocontainers.pro/tools/gffread"
aliases:
 - "gffread"
versions:
 - "0.9.9--1"
description: "shpc-registry automated BioContainers addition for gffread"
config: {"url": "https://biocontainers.pro/tools/gffread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gffread", "latest": {"0.9.9--1": "sha256:419e1859e4fdd30217071a75fab40058e89aaaae142615d8102ac8985227e75f"}, "tags": {"0.9.9--1": "sha256:419e1859e4fdd30217071a75fab40058e89aaaae142615d8102ac8985227e75f"}, "docker": "quay.io/biocontainers/gffread", "aliases": {"gffread": "/usr/local/bin/gffread"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gffread.
shpc-registry automated BioContainers addition for gffread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gffread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gffread:0.9.9--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gffread/0.9.9--1
$ module help quay.io/biocontainers/gffread/0.9.9--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gffread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gffread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gffread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gffread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gffread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gffread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
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