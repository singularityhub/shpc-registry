---
layout: container
name:  "ghcr.io/autamus/ascent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ascent/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/ascent/container.yaml"
updated_at: "2025-07-06 04:18:57.701390"
latest: "0.7.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/ascent"

versions:
 - "0.7.0"
 - "0.7.1"
 - "latest"
description: "An open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations."
config: {"docker": "ghcr.io/autamus/ascent", "url": "https://github.com/orgs/autamus/packages/container/package/ascent", "maintainer": "@vsoch", "description": "An open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations.", "latest": {"0.7.1": "sha256:61e3795c17382b95787f070ce0b0e382c73056d776f672ae0db9f6536718a1af"}, "tags": {"0.7.0": "sha256:c025f72e442b7a4f5626e0520e09e8a7a5e5f5c630565cbd8d0d178ff2585ee6", "0.7.1": "sha256:61e3795c17382b95787f070ce0b0e382c73056d776f672ae0db9f6536718a1af", "latest": "sha256:61e3795c17382b95787f070ce0b0e382c73056d776f672ae0db9f6536718a1af"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ascent.
An open source many-core capable lightweight in situ visualization and analysis infrastructure for multi-physics HPC simulations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ascent
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ascent:0.7.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ascent/0.7.1
$ module help ghcr.io/autamus/ascent/0.7.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ascent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ascent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ascent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ascent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ascent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ascent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ascent

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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