---
layout: container
name:  "quay.io/biocontainers/bgreat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bgreat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bgreat/container.yaml"
updated_at: "2023-02-08 23:22:44.585823"
latest: "2.0.0--h5b5514e_4"
container_url: "https://biocontainers.pro/tools/bgreat"
aliases:
 - "bgreat"
versions:
 - "2.0.0--h5b5514e_4"
description: "shpc-registry automated BioContainers addition for bgreat"
config: {"url": "https://biocontainers.pro/tools/bgreat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bgreat", "latest": {"2.0.0--h5b5514e_4": "sha256:82b2058349acec28931b3b15c808c27d398c4ae7f9624098256d007670702fbe"}, "tags": {"2.0.0--h5b5514e_4": "sha256:82b2058349acec28931b3b15c808c27d398c4ae7f9624098256d007670702fbe"}, "docker": "quay.io/biocontainers/bgreat", "aliases": {"bgreat": "/usr/local/bin/bgreat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bgreat.
shpc-registry automated BioContainers addition for bgreat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bgreat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bgreat:2.0.0--h5b5514e_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bgreat/2.0.0--h5b5514e_4
$ module help quay.io/biocontainers/bgreat/2.0.0--h5b5514e_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bgreat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bgreat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bgreat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bgreat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bgreat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bgreat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgreat

```bash
$ singularity exec <container> /usr/local/bin/bgreat
$ podman run --it --rm --entrypoint /usr/local/bin/bgreat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgreat   -v ${PWD} -w ${PWD} <container> -c " $@"
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