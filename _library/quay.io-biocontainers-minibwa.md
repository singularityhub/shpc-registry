---
layout: container
name:  "quay.io/biocontainers/minibwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minibwa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minibwa/container.yaml"
updated_at: "2026-06-23 07:02:13.383863"
latest: "0.1--h118bc1c_0"
container_url: "https://biocontainers.pro/tools/minibwa"
aliases:
 - "minibwa"
versions:
 - "0.1--h118bc1c_0"
description: "singularity registry hpc automated addition for minibwa"
config: {"url": "https://biocontainers.pro/tools/minibwa", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for minibwa", "latest": {"0.1--h118bc1c_0": "sha256:02a615fb336a6f95a9c15f7a8ecacb15dad03e6e5596ca15289eccdf67dba6d5"}, "tags": {"0.1--h118bc1c_0": "sha256:02a615fb336a6f95a9c15f7a8ecacb15dad03e6e5596ca15289eccdf67dba6d5"}, "docker": "quay.io/biocontainers/minibwa", "aliases": {"minibwa": "/usr/local/bin/minibwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minibwa.
singularity registry hpc automated addition for minibwa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minibwa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minibwa:0.1--h118bc1c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minibwa/0.1--h118bc1c_0
$ module help quay.io/biocontainers/minibwa/0.1--h118bc1c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minibwa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minibwa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minibwa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minibwa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minibwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minibwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minibwa

```bash
$ singularity exec <container> /usr/local/bin/minibwa
$ podman run --it --rm --entrypoint /usr/local/bin/minibwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minibwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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