---
layout: container
name:  "quay.io/biocontainers/lima"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lima/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lima/container.yaml"
updated_at: "2025-05-06 03:56:10.331745"
latest: "2.13.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/lima"
aliases:
 - "lima"
 - "lima-undo"
versions:
 - "2.6.0--h9ee0642_0"
 - "2.7.1--h9ee0642_0"
 - "2.9.0--h9ee0642_1"
 - "2.12.0--h9ee0642_1"
 - "2.13.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for lima"
config: {"url": "https://biocontainers.pro/tools/lima", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lima", "latest": {"2.13.0--h9ee0642_0": "sha256:0ed382839aed000ef1562fef4acd43d0854510a436f97ba33df1864d570c77de"}, "tags": {"2.6.0--h9ee0642_0": "sha256:f7d12565ed2c29ae7e8ae524456b1ae4fd466e1f0ed1ea915cd15da29fea44d7", "2.7.1--h9ee0642_0": "sha256:c1967046d4cc39b122d25d19f50e2fe57181715e594b51d0043ce23a94788d47", "2.9.0--h9ee0642_1": "sha256:fc370ba0a93de228990f3cb026fddd610b80e03884df0bb55809c37866d2c80c", "2.12.0--h9ee0642_1": "sha256:eea7a8030e308c1a057b3b4d8c533ef38c51a57653fb9d0a99afe8d2597924c3", "2.13.0--h9ee0642_0": "sha256:0ed382839aed000ef1562fef4acd43d0854510a436f97ba33df1864d570c77de"}, "docker": "quay.io/biocontainers/lima", "aliases": {"lima": "/usr/local/bin/lima", "lima-undo": "/usr/local/bin/lima-undo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lima.
shpc-registry automated BioContainers addition for lima
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lima
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lima:2.13.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lima/2.13.0--h9ee0642_0
$ module help quay.io/biocontainers/lima/2.13.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lima-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lima-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lima-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lima-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lima-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lima-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lima

```bash
$ singularity exec <container> /usr/local/bin/lima
$ podman run --it --rm --entrypoint /usr/local/bin/lima   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lima   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lima-undo

```bash
$ singularity exec <container> /usr/local/bin/lima-undo
$ podman run --it --rm --entrypoint /usr/local/bin/lima-undo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lima-undo   -v ${PWD} -w ${PWD} <container> -c " $@"
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