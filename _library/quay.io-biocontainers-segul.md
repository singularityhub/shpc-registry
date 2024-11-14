---
layout: container
name:  "quay.io/biocontainers/segul"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/segul/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/segul/container.yaml"
updated_at: "2024-11-14 03:13:13.985233"
latest: "0.22.1--h715e4b3_0"
container_url: "https://biocontainers.pro/tools/segul"
aliases:
 - "segul"
versions:
 - "0.21.3--h715e4b3_0"
 - "0.22.1--h715e4b3_0"
description: "singularity registry hpc automated addition for segul"
config: {"url": "https://biocontainers.pro/tools/segul", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for segul", "latest": {"0.22.1--h715e4b3_0": "sha256:d9bd75dbbdc637b769e4975154a338ae787c7c5d2d7f8486a4875308d324e502"}, "tags": {"0.21.3--h715e4b3_0": "sha256:84e5ccd7a6bccc02c48feab836a459c85ece8caa5ae5c5afb7c961c7bfc63bb5", "0.22.1--h715e4b3_0": "sha256:d9bd75dbbdc637b769e4975154a338ae787c7c5d2d7f8486a4875308d324e502"}, "docker": "quay.io/biocontainers/segul", "aliases": {"segul": "/usr/local/bin/segul"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/segul.
singularity registry hpc automated addition for segul
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/segul
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/segul:0.22.1--h715e4b3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/segul/0.22.1--h715e4b3_0
$ module help quay.io/biocontainers/segul/0.22.1--h715e4b3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### segul-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### segul-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### segul-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### segul-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### segul-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### segul-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### segul

```bash
$ singularity exec <container> /usr/local/bin/segul
$ podman run --it --rm --entrypoint /usr/local/bin/segul   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segul   -v ${PWD} -w ${PWD} <container> -c " $@"
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