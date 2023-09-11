---
layout: container
name:  "quay.io/biocontainers/guide-counter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guide-counter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/guide-counter/container.yaml"
updated_at: "2023-09-11 03:19:48.436775"
latest: "0.1.3--hdbdd923_3"
container_url: "https://biocontainers.pro/tools/guide-counter"
aliases:
 - "guide-counter"
versions:
 - "0.1.3--h87f3376_1"
 - "0.1.3--hdbdd923_3"
description: "singularity registry hpc automated addition for guide-counter"
config: {"url": "https://biocontainers.pro/tools/guide-counter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for guide-counter", "latest": {"0.1.3--hdbdd923_3": "sha256:3732663b4b3e6c69fdbcfb99be623a3ff8f26ab36daa12344cc5261e6b6b2f10"}, "tags": {"0.1.3--h87f3376_1": "sha256:e35be03a49a9317b76cec69dd2dce458e8641f942786ba12d2b98f5938ebeb83", "0.1.3--hdbdd923_3": "sha256:3732663b4b3e6c69fdbcfb99be623a3ff8f26ab36daa12344cc5261e6b6b2f10"}, "docker": "quay.io/biocontainers/guide-counter", "aliases": {"guide-counter": "/usr/local/bin/guide-counter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guide-counter.
singularity registry hpc automated addition for guide-counter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guide-counter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guide-counter:0.1.3--hdbdd923_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guide-counter/0.1.3--hdbdd923_3
$ module help quay.io/biocontainers/guide-counter/0.1.3--hdbdd923_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guide-counter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guide-counter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guide-counter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guide-counter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guide-counter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guide-counter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### guide-counter

```bash
$ singularity exec <container> /usr/local/bin/guide-counter
$ podman run --it --rm --entrypoint /usr/local/bin/guide-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guide-counter   -v ${PWD} -w ${PWD} <container> -c " $@"
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