---
layout: container
name:  "quay.io/biocontainers/ribotish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribotish/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ribotish/container.yaml"
updated_at: "2022-10-27 00:55:20.145390"
latest: "0.2.5--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/ribotish"
aliases:
 - "ribotish"
versions:
 - "0.2.5--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for ribotish"
config: {"url": "https://biocontainers.pro/tools/ribotish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ribotish", "latest": {"0.2.5--pyh864c0ab_1": "sha256:38f9b04ce56dfe83b2a3d693079d1c69373852aef429be6b1b4bf855e2f582da"}, "tags": {"0.2.5--pyh864c0ab_1": "sha256:38f9b04ce56dfe83b2a3d693079d1c69373852aef429be6b1b4bf855e2f582da"}, "docker": "quay.io/biocontainers/ribotish", "aliases": {"ribotish": "/usr/local/bin/ribotish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribotish.
shpc-registry automated BioContainers addition for ribotish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribotish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribotish:0.2.5--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribotish/0.2.5--pyh864c0ab_1
$ module help quay.io/biocontainers/ribotish/0.2.5--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribotish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribotish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribotish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribotish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribotish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribotish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ribotish

```bash
$ singularity exec <container> /usr/local/bin/ribotish
$ podman run --it --rm --entrypoint /usr/local/bin/ribotish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ribotish   -v ${PWD} -w ${PWD} <container> -c " $@"
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