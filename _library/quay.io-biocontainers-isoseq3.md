---
layout: container
name:  "quay.io/biocontainers/isoseq3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isoseq3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isoseq3/container.yaml"
updated_at: "2023-01-26 02:56:46.604578"
latest: "3.8.2--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/isoseq3"
aliases:
 - "isoseq3"
versions:
 - "3.8.0--h9ee0642_0"
 - "3.8.1--h9ee0642_0"
 - "3.8.2--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for isoseq3"
config: {"url": "https://biocontainers.pro/tools/isoseq3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isoseq3", "latest": {"3.8.2--h9ee0642_0": "sha256:74246884442c5c360b7abf4e264d092aa630699d06b3a433ca139fae02af8a16"}, "tags": {"3.8.0--h9ee0642_0": "sha256:3380db4a010394b4e4f14a843edce78e6e4e93d5790b32e83cb0cbef0bc97acb", "3.8.1--h9ee0642_0": "sha256:f635fa3baade7a0f796218b5d0dcf44af2f46dfad7d6c013cb60533b97bb904c", "3.8.2--h9ee0642_0": "sha256:74246884442c5c360b7abf4e264d092aa630699d06b3a433ca139fae02af8a16"}, "docker": "quay.io/biocontainers/isoseq3", "aliases": {"isoseq3": "/usr/local/bin/isoseq3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isoseq3.
shpc-registry automated BioContainers addition for isoseq3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isoseq3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isoseq3:3.8.2--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isoseq3/3.8.2--h9ee0642_0
$ module help quay.io/biocontainers/isoseq3/3.8.2--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isoseq3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isoseq3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isoseq3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isoseq3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isoseq3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isoseq3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isoseq3

```bash
$ singularity exec <container> /usr/local/bin/isoseq3
$ podman run --it --rm --entrypoint /usr/local/bin/isoseq3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoseq3   -v ${PWD} -w ${PWD} <container> -c " $@"
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