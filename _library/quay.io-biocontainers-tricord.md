---
layout: container
name:  "quay.io/biocontainers/tricord"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tricord/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tricord/container.yaml"
updated_at: "2026-06-21 07:40:50.176745"
latest: "0.1.3--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/tricord"
aliases:
 - "tricorder"
versions:
 - "0.1.2--hfa8f182_0"
 - "0.1.3--hfa8f182_0"
description: "singularity registry hpc automated addition for tricord"
config: {"url": "https://biocontainers.pro/tools/tricord", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tricord", "latest": {"0.1.3--hfa8f182_0": "sha256:270e47cf61f04192e7948897367bad2fd81041a2aba9355295530e3b05cd753a"}, "tags": {"0.1.2--hfa8f182_0": "sha256:a836856e76815040838e6bb5a5e5d14118208bff3563340bf186db51bd315c41", "0.1.3--hfa8f182_0": "sha256:270e47cf61f04192e7948897367bad2fd81041a2aba9355295530e3b05cd753a"}, "docker": "quay.io/biocontainers/tricord", "aliases": {"tricorder": "/usr/local/bin/tricorder"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tricord.
singularity registry hpc automated addition for tricord
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tricord
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tricord:0.1.3--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tricord/0.1.3--hfa8f182_0
$ module help quay.io/biocontainers/tricord/0.1.3--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tricord-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tricord-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tricord-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tricord-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tricord-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tricord-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tricorder

```bash
$ singularity exec <container> /usr/local/bin/tricorder
$ podman run --it --rm --entrypoint /usr/local/bin/tricorder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tricorder   -v ${PWD} -w ${PWD} <container> -c " $@"
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