---
layout: container
name:  "quay.io/biocontainers/ldak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ldak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ldak/container.yaml"
updated_at: "2026-11-05 09:32:19.429727"
latest: "6.3--hae53b8d_0"
container_url: "https://biocontainers.pro/tools/ldak"
aliases:
 - "ldak"
versions:
 - "6.3--hae53b8d_0"
description: "singularity registry hpc automated addition for ldak"
config: {"url": "https://biocontainers.pro/tools/ldak", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ldak", "latest": {"6.3--hae53b8d_0": "sha256:94d94a43025846120e58cea837a35801c956fc54d63e71b4c8f0a9fddf95661f"}, "tags": {"6.3--hae53b8d_0": "sha256:94d94a43025846120e58cea837a35801c956fc54d63e71b4c8f0a9fddf95661f"}, "docker": "quay.io/biocontainers/ldak", "aliases": {"ldak": "/usr/local/bin/ldak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ldak.
singularity registry hpc automated addition for ldak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ldak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ldak:6.3--hae53b8d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ldak/6.3--hae53b8d_0
$ module help quay.io/biocontainers/ldak/6.3--hae53b8d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ldak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ldak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ldak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ldak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ldak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ldak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ldak

```bash
$ singularity exec <container> /usr/local/bin/ldak
$ podman run --it --rm --entrypoint /usr/local/bin/ldak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldak   -v ${PWD} -w ${PWD} <container> -c " $@"
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