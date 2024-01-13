---
layout: container
name:  "quay.io/biocontainers/me-pcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/me-pcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/me-pcr/container.yaml"
updated_at: "2024-01-13 03:08:10.791687"
latest: "1.0.6--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/me-pcr"
aliases:
 - "me-PCR"
versions:
 - "1.0.6--hdbdd923_0"
description: "singularity registry hpc automated addition for me-pcr"
config: {"url": "https://biocontainers.pro/tools/me-pcr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for me-pcr", "latest": {"1.0.6--hdbdd923_0": "sha256:3cbe34452e9dd295d9770334d2be894b191d46f456a3d6d36da18fc8105f5cb5"}, "tags": {"1.0.6--hdbdd923_0": "sha256:3cbe34452e9dd295d9770334d2be894b191d46f456a3d6d36da18fc8105f5cb5"}, "docker": "quay.io/biocontainers/me-pcr", "aliases": {"me-PCR": "/usr/local/bin/me-PCR"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/me-pcr.
singularity registry hpc automated addition for me-pcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/me-pcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/me-pcr:1.0.6--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/me-pcr/1.0.6--hdbdd923_0
$ module help quay.io/biocontainers/me-pcr/1.0.6--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### me-pcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### me-pcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### me-pcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### me-pcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### me-pcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### me-pcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### me-PCR

```bash
$ singularity exec <container> /usr/local/bin/me-PCR
$ podman run --it --rm --entrypoint /usr/local/bin/me-PCR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/me-PCR   -v ${PWD} -w ${PWD} <container> -c " $@"
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