---
layout: container
name:  "quay.io/biocontainers/clovers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clovers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clovers/container.yaml"
updated_at: "2026-11-05 09:37:27.018200"
latest: "1.2.2--h3be2455_0"
container_url: "https://biocontainers.pro/tools/clovers"
aliases:
 - "clovers"
versions:
 - "1.2.2--h3be2455_0"
description: "singularity registry hpc automated addition for clovers"
config: {"url": "https://biocontainers.pro/tools/clovers", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for clovers", "latest": {"1.2.2--h3be2455_0": "sha256:841ad9aeca73eff51dca8acea7bbc35d4338b4f13ce6c9db636cf3c28b50f6f8"}, "tags": {"1.2.2--h3be2455_0": "sha256:841ad9aeca73eff51dca8acea7bbc35d4338b4f13ce6c9db636cf3c28b50f6f8"}, "docker": "quay.io/biocontainers/clovers", "aliases": {"clovers": "/usr/local/bin/clovers"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clovers.
singularity registry hpc automated addition for clovers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clovers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clovers:1.2.2--h3be2455_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clovers/1.2.2--h3be2455_0
$ module help quay.io/biocontainers/clovers/1.2.2--h3be2455_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clovers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clovers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clovers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clovers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clovers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clovers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clovers

```bash
$ singularity exec <container> /usr/local/bin/clovers
$ podman run --it --rm --entrypoint /usr/local/bin/clovers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clovers   -v ${PWD} -w ${PWD} <container> -c " $@"
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