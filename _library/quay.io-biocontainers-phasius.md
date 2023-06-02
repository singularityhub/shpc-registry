---
layout: container
name:  "quay.io/biocontainers/phasius"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phasius/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phasius/container.yaml"
updated_at: "2023-06-02 03:44:01.183420"
latest: "0.1.0--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/phasius"
aliases:
 - "phasius"
versions:
 - "0.1.0--h9f5acd7_0"
 - "0.1.0--h4ac6f70_2"
description: "singularity registry hpc automated addition for phasius"
config: {"url": "https://biocontainers.pro/tools/phasius", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phasius", "latest": {"0.1.0--h4ac6f70_2": "sha256:aca9a69957b856f6848e20a33e38a7efd9821e82382ccbff5715e1841c9214c9"}, "tags": {"0.1.0--h9f5acd7_0": "sha256:627720aeac0c96383e368e9a641af791954b141718be3d5639152fef4e853f58", "0.1.0--h4ac6f70_2": "sha256:aca9a69957b856f6848e20a33e38a7efd9821e82382ccbff5715e1841c9214c9"}, "docker": "quay.io/biocontainers/phasius", "aliases": {"phasius": "/usr/local/bin/phasius"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phasius.
singularity registry hpc automated addition for phasius
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phasius
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phasius:0.1.0--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phasius/0.1.0--h4ac6f70_2
$ module help quay.io/biocontainers/phasius/0.1.0--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phasius-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phasius-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phasius-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phasius-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phasius-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phasius-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phasius

```bash
$ singularity exec <container> /usr/local/bin/phasius
$ podman run --it --rm --entrypoint /usr/local/bin/phasius   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phasius   -v ${PWD} -w ${PWD} <container> -c " $@"
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