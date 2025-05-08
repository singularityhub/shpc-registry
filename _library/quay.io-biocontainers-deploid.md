---
layout: container
name:  "quay.io/biocontainers/deploid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deploid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deploid/container.yaml"
updated_at: "2025-05-08 03:32:09.711669"
latest: "0.5--h5ca1c30_5"
container_url: "https://biocontainers.pro/tools/deploid"
aliases:
 - "dEploid"
 - "dEploid_dbg"
versions:
 - "v0.5--h1341992_1"
 - "0.5--h5b5514e_2"
 - "0.5--h43eeafb_4"
 - "0.5--h5ca1c30_5"
description: "shpc-registry automated BioContainers addition for deploid"
config: {"url": "https://biocontainers.pro/tools/deploid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deploid", "latest": {"0.5--h5ca1c30_5": "sha256:cc8013562cc92d1f187ef3bbb88f14406141ffc6ee80d0680918751bd0cf0f2d"}, "tags": {"v0.5--h1341992_1": "sha256:0f0cbbbecc13e8b748d903b4736c6a34212b46b2c90e03b9f2448623bd6393cb", "0.5--h5b5514e_2": "sha256:d2f4f07ded58dddb85835db0d2cec93c42e5189d260e4293b74c51ebb1786beb", "0.5--h43eeafb_4": "sha256:dff0a77f8c807ffce566a8aecaa5e3b645755d6e4f77b30836b0db6952b81b16", "0.5--h5ca1c30_5": "sha256:cc8013562cc92d1f187ef3bbb88f14406141ffc6ee80d0680918751bd0cf0f2d"}, "docker": "quay.io/biocontainers/deploid", "aliases": {"dEploid": "/usr/local/bin/dEploid", "dEploid_dbg": "/usr/local/bin/dEploid_dbg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deploid.
shpc-registry automated BioContainers addition for deploid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deploid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deploid:0.5--h5ca1c30_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deploid/0.5--h5ca1c30_5
$ module help quay.io/biocontainers/deploid/0.5--h5ca1c30_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deploid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deploid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deploid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deploid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deploid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deploid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dEploid

```bash
$ singularity exec <container> /usr/local/bin/dEploid
$ podman run --it --rm --entrypoint /usr/local/bin/dEploid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dEploid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dEploid_dbg

```bash
$ singularity exec <container> /usr/local/bin/dEploid_dbg
$ podman run --it --rm --entrypoint /usr/local/bin/dEploid_dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dEploid_dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
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