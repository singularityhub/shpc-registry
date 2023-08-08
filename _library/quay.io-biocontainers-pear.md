---
layout: container
name:  "quay.io/biocontainers/pear"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pear/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pear/container.yaml"
updated_at: "2023-08-08 02:50:51.738586"
latest: "0.9.6--h9d449c0_10"
container_url: "https://biocontainers.pro/tools/pear"
aliases:
 - "pear"
 - "pearRM"
versions:
 - "0.9.6--h67092d7_8"
 - "0.9.6--h9d449c0_10"
description: "shpc-registry automated BioContainers addition for pear"
config: {"url": "https://biocontainers.pro/tools/pear", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pear", "latest": {"0.9.6--h9d449c0_10": "sha256:e12f7c93da40fbd416491489e5ff86dae979ccfc7530f9a4573c46725bc90f34"}, "tags": {"0.9.6--h67092d7_8": "sha256:a7f529795c2d8d94f4c197fbdb62452299536ed03978200cd995b32c7315ac5e", "0.9.6--h9d449c0_10": "sha256:e12f7c93da40fbd416491489e5ff86dae979ccfc7530f9a4573c46725bc90f34"}, "docker": "quay.io/biocontainers/pear", "aliases": {"pear": "/usr/local/bin/pear", "pearRM": "/usr/local/bin/pearRM"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pear.
shpc-registry automated BioContainers addition for pear
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pear
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pear:0.9.6--h9d449c0_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pear/0.9.6--h9d449c0_10
$ module help quay.io/biocontainers/pear/0.9.6--h9d449c0_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pear-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pear-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pear-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pear-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pear-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pear-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pear

```bash
$ singularity exec <container> /usr/local/bin/pear
$ podman run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pearRM

```bash
$ singularity exec <container> /usr/local/bin/pearRM
$ podman run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
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