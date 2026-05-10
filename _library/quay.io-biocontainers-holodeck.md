---
layout: container
name:  "quay.io/biocontainers/holodeck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/holodeck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/holodeck/container.yaml"
updated_at: "2026-05-10 06:36:22.275264"
latest: "0.2.1--hd612981_0"
container_url: "https://biocontainers.pro/tools/holodeck"
aliases:
 - "holodeck"
versions:
 - "0.2.0--hd612981_0"
 - "0.2.1--hd612981_0"
description: "singularity registry hpc automated addition for holodeck"
config: {"url": "https://biocontainers.pro/tools/holodeck", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for holodeck", "latest": {"0.2.1--hd612981_0": "sha256:7a1d8d561a1b62a1c5eb746f10b7a44c742760f3a50326084eb612c28dcbac0c"}, "tags": {"0.2.0--hd612981_0": "sha256:e3e6dee6f6668e765a9ebf834cbc07d96f39d16f7049232641906af36e29bf84", "0.2.1--hd612981_0": "sha256:7a1d8d561a1b62a1c5eb746f10b7a44c742760f3a50326084eb612c28dcbac0c"}, "docker": "quay.io/biocontainers/holodeck", "aliases": {"holodeck": "/usr/local/bin/holodeck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/holodeck.
singularity registry hpc automated addition for holodeck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/holodeck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/holodeck:0.2.1--hd612981_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/holodeck/0.2.1--hd612981_0
$ module help quay.io/biocontainers/holodeck/0.2.1--hd612981_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### holodeck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### holodeck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### holodeck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### holodeck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### holodeck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### holodeck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### holodeck

```bash
$ singularity exec <container> /usr/local/bin/holodeck
$ podman run --it --rm --entrypoint /usr/local/bin/holodeck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/holodeck   -v ${PWD} -w ${PWD} <container> -c " $@"
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