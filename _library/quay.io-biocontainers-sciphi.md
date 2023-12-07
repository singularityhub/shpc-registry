---
layout: container
name:  "quay.io/biocontainers/sciphi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sciphi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sciphi/container.yaml"
updated_at: "2023-12-07 02:52:14.140446"
latest: "0.1.7--h21ec9f0_4"
container_url: "https://biocontainers.pro/tools/sciphi"
aliases:
 - "sciphi"
versions:
 - "0.1.7--h7ff8a90_2"
 - "0.1.7--h21ec9f0_4"
description: "shpc-registry automated BioContainers addition for sciphi"
config: {"url": "https://biocontainers.pro/tools/sciphi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sciphi", "latest": {"0.1.7--h21ec9f0_4": "sha256:069942c49e0b97b2234fc8d8e8482903e9d3fae51395c697cfe3e437abf2cd26"}, "tags": {"0.1.7--h7ff8a90_2": "sha256:3d8b40615a2df11ce4bed696f2d4b3f98c31a706c4dbfda37f42db5b508a72b6", "0.1.7--h21ec9f0_4": "sha256:069942c49e0b97b2234fc8d8e8482903e9d3fae51395c697cfe3e437abf2cd26"}, "docker": "quay.io/biocontainers/sciphi", "aliases": {"sciphi": "/usr/local/bin/sciphi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sciphi.
shpc-registry automated BioContainers addition for sciphi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sciphi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sciphi:0.1.7--h21ec9f0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sciphi/0.1.7--h21ec9f0_4
$ module help quay.io/biocontainers/sciphi/0.1.7--h21ec9f0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sciphi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sciphi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sciphi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sciphi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sciphi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sciphi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sciphi

```bash
$ singularity exec <container> /usr/local/bin/sciphi
$ podman run --it --rm --entrypoint /usr/local/bin/sciphi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sciphi   -v ${PWD} -w ${PWD} <container> -c " $@"
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