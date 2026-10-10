---
layout: container
name:  "quay.io/biocontainers/proteomiqon-quantbasedalignment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-quantbasedalignment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-quantbasedalignment/container.yaml"
updated_at: "2026-10-10 19:18:24.185876"
latest: "0.0.4--h774997f_0"
container_url: "https://biocontainers.pro/tools/proteomiqon-quantbasedalignment"
aliases:
 - "proteomiqon-quantbasedalignment"
versions:
 - "0.0.4--h774997f_0"
description: "singularity registry hpc automated addition for proteomiqon-quantbasedalignment"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-quantbasedalignment", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for proteomiqon-quantbasedalignment", "latest": {"0.0.4--h774997f_0": "sha256:a3ff5f7978de065591a1ea5cd6a0679ca29509002a4ee85a102e9e6421761f4a"}, "tags": {"0.0.4--h774997f_0": "sha256:a3ff5f7978de065591a1ea5cd6a0679ca29509002a4ee85a102e9e6421761f4a"}, "docker": "quay.io/biocontainers/proteomiqon-quantbasedalignment", "aliases": {"proteomiqon-quantbasedalignment": "/usr/local/bin/proteomiqon-quantbasedalignment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-quantbasedalignment.
singularity registry hpc automated addition for proteomiqon-quantbasedalignment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-quantbasedalignment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-quantbasedalignment:0.0.4--h774997f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-quantbasedalignment/0.0.4--h774997f_0
$ module help quay.io/biocontainers/proteomiqon-quantbasedalignment/0.0.4--h774997f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-quantbasedalignment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-quantbasedalignment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-quantbasedalignment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-quantbasedalignment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-quantbasedalignment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-quantbasedalignment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proteomiqon-quantbasedalignment

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-quantbasedalignment
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-quantbasedalignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-quantbasedalignment   -v ${PWD} -w ${PWD} <container> -c " $@"
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