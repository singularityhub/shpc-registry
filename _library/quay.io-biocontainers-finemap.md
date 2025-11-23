---
layout: container
name:  "quay.io/biocontainers/finemap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/finemap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/finemap/container.yaml"
updated_at: "2025-11-23 04:18:52.253279"
latest: "1.4.2--hb192632_1"
container_url: "https://biocontainers.pro/tools/finemap"
aliases:
 - "finemap"
versions:
 - "1.4.1--0"
 - "1.4.2--hb192632_0"
 - "1.4.2--hb192632_1"
description: "singularity registry hpc automated addition for finemap"
config: {"url": "https://biocontainers.pro/tools/finemap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for finemap", "latest": {"1.4.2--hb192632_1": "sha256:7df4adb6317d4df3c5d9e427d9f2e0c7f3f8f7078b58ffe6fac5b8d71ee40b3d"}, "tags": {"1.4.1--0": "sha256:6e07321784a93f0814515d36b14c4542bdda982e0fb1faf9b178bf31cd3842af", "1.4.2--hb192632_0": "sha256:30c1149fe764931e83f9905d32c359514b04e331164cbea3c6eb55949c006aaa", "1.4.2--hb192632_1": "sha256:7df4adb6317d4df3c5d9e427d9f2e0c7f3f8f7078b58ffe6fac5b8d71ee40b3d"}, "docker": "quay.io/biocontainers/finemap", "aliases": {"finemap": "/usr/local/bin/finemap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/finemap.
singularity registry hpc automated addition for finemap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/finemap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/finemap:1.4.2--hb192632_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/finemap/1.4.2--hb192632_1
$ module help quay.io/biocontainers/finemap/1.4.2--hb192632_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### finemap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### finemap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### finemap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### finemap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### finemap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### finemap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### finemap

```bash
$ singularity exec <container> /usr/local/bin/finemap
$ podman run --it --rm --entrypoint /usr/local/bin/finemap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/finemap   -v ${PWD} -w ${PWD} <container> -c " $@"
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