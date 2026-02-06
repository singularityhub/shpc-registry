---
layout: container
name:  "quay.io/biocontainers/krepp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/krepp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/krepp/container.yaml"
updated_at: "2026-02-06 04:29:37.837525"
latest: "0.6.0--h370f27c_0"
container_url: "https://biocontainers.pro/tools/krepp"
aliases:
 - "krepp"
versions:
 - "0.5.1--h370f27c_0"
 - "0.6.0--h370f27c_0"
description: "singularity registry hpc automated addition for krepp"
config: {"url": "https://biocontainers.pro/tools/krepp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for krepp", "latest": {"0.6.0--h370f27c_0": "sha256:7c8c0745f800b2fb5602348226be41c191db38c8dd5ded01a5a21dfbcc83ba2f"}, "tags": {"0.5.1--h370f27c_0": "sha256:af93e14f91c0a0c59008d0197df4c12f12bebb0eddc15e2a6cc89a1501a31ebd", "0.6.0--h370f27c_0": "sha256:7c8c0745f800b2fb5602348226be41c191db38c8dd5ded01a5a21dfbcc83ba2f"}, "docker": "quay.io/biocontainers/krepp", "aliases": {"krepp": "/usr/local/bin/krepp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/krepp.
singularity registry hpc automated addition for krepp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/krepp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/krepp:0.6.0--h370f27c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/krepp/0.6.0--h370f27c_0
$ module help quay.io/biocontainers/krepp/0.6.0--h370f27c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### krepp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### krepp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### krepp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### krepp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### krepp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### krepp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### krepp

```bash
$ singularity exec <container> /usr/local/bin/krepp
$ podman run --it --rm --entrypoint /usr/local/bin/krepp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krepp   -v ${PWD} -w ${PWD} <container> -c " $@"
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