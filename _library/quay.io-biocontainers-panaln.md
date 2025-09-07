---
layout: container
name:  "quay.io/biocontainers/panaln"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panaln/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panaln/container.yaml"
updated_at: "2025-09-07 03:20:23.949749"
latest: "2.09--h5ca1c30_0"
container_url: "https://biocontainers.pro/tools/panaln"
aliases:
 - "panaln"
versions:
 - "2.09--h5ca1c30_0"
description: "singularity registry hpc automated addition for panaln"
config: {"url": "https://biocontainers.pro/tools/panaln", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for panaln", "latest": {"2.09--h5ca1c30_0": "sha256:efd3994a0b6c39b37f56df0c05adf08dd19ccde9887ba5b91c5e2bd46e9925cf"}, "tags": {"2.09--h5ca1c30_0": "sha256:efd3994a0b6c39b37f56df0c05adf08dd19ccde9887ba5b91c5e2bd46e9925cf"}, "docker": "quay.io/biocontainers/panaln", "aliases": {"panaln": "/usr/local/bin/panaln"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panaln.
singularity registry hpc automated addition for panaln
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panaln
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panaln:2.09--h5ca1c30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panaln/2.09--h5ca1c30_0
$ module help quay.io/biocontainers/panaln/2.09--h5ca1c30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panaln-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panaln-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panaln-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panaln-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panaln-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panaln-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### panaln

```bash
$ singularity exec <container> /usr/local/bin/panaln
$ podman run --it --rm --entrypoint /usr/local/bin/panaln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panaln   -v ${PWD} -w ${PWD} <container> -c " $@"
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