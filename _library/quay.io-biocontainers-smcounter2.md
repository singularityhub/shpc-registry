---
layout: container
name:  "quay.io/biocontainers/smcounter2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smcounter2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/smcounter2/container.yaml"
updated_at: "2022-10-27 01:03:43.066320"
latest: "0.1.2018.08.28--2"
container_url: "https://biocontainers.pro/tools/smcounter2"
aliases:
 - "smCounter2"
versions:
 - "0.1.2018.08.28--2"
description: "shpc-registry automated BioContainers addition for smcounter2"
config: {"url": "https://biocontainers.pro/tools/smcounter2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smcounter2", "latest": {"0.1.2018.08.28--2": "sha256:ebd4f6babb6734fc5c53f35d2a93c8a2d790f64b27f32d337604faaa2677b1a0"}, "tags": {"0.1.2018.08.28--2": "sha256:ebd4f6babb6734fc5c53f35d2a93c8a2d790f64b27f32d337604faaa2677b1a0"}, "docker": "quay.io/biocontainers/smcounter2", "aliases": {"smCounter2": "/usr/local/bin/smCounter2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smcounter2.
shpc-registry automated BioContainers addition for smcounter2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smcounter2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smcounter2:0.1.2018.08.28--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smcounter2/0.1.2018.08.28--2
$ module help quay.io/biocontainers/smcounter2/0.1.2018.08.28--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smcounter2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smcounter2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smcounter2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smcounter2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smcounter2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smcounter2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smCounter2

```bash
$ singularity exec <container> /usr/local/bin/smCounter2
$ podman run --it --rm --entrypoint /usr/local/bin/smCounter2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smCounter2   -v ${PWD} -w ${PWD} <container> -c " $@"
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