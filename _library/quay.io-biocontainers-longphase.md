---
layout: container
name:  "quay.io/biocontainers/longphase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longphase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longphase/container.yaml"
updated_at: "2025-05-25 04:06:16.186951"
latest: "1.7.3--hf5e1c6e_0"
container_url: "https://biocontainers.pro/tools/longphase"
aliases:
 - "longphase"
versions:
 - "1.7.3--hf5e1c6e_0"
description: "singularity registry hpc automated addition for longphase"
config: {"url": "https://biocontainers.pro/tools/longphase", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for longphase", "latest": {"1.7.3--hf5e1c6e_0": "sha256:4a4f9fbd14ea325b9d7d4310d1df8fe7940b80cc8daed1907355919e15e6e457"}, "tags": {"1.7.3--hf5e1c6e_0": "sha256:4a4f9fbd14ea325b9d7d4310d1df8fe7940b80cc8daed1907355919e15e6e457"}, "docker": "quay.io/biocontainers/longphase", "aliases": {"longphase": "/usr/local/bin/longphase"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longphase.
singularity registry hpc automated addition for longphase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longphase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longphase:1.7.3--hf5e1c6e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longphase/1.7.3--hf5e1c6e_0
$ module help quay.io/biocontainers/longphase/1.7.3--hf5e1c6e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longphase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longphase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longphase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longphase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longphase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longphase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### longphase

```bash
$ singularity exec <container> /usr/local/bin/longphase
$ podman run --it --rm --entrypoint /usr/local/bin/longphase   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longphase   -v ${PWD} -w ${PWD} <container> -c " $@"
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