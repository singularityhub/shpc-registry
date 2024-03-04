---
layout: container
name:  "quay.io/biocontainers/fastuniq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastuniq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastuniq/container.yaml"
updated_at: "2024-03-04 03:24:43.377126"
latest: "1.1--h470a237_1"
container_url: "https://biocontainers.pro/tools/fastuniq"
aliases:
 - "fastuniq"
versions:
 - "1.1--h470a237_1"
description: "shpc-registry automated BioContainers addition for fastuniq"
config: {"url": "https://biocontainers.pro/tools/fastuniq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastuniq", "latest": {"1.1--h470a237_1": "sha256:ce3811629bfb966cd510db0d78f5e8c8db4b467418db3ed1c4732036c91c4510"}, "tags": {"1.1--h470a237_1": "sha256:ce3811629bfb966cd510db0d78f5e8c8db4b467418db3ed1c4732036c91c4510"}, "docker": "quay.io/biocontainers/fastuniq", "aliases": {"fastuniq": "/usr/local/bin/fastuniq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastuniq.
shpc-registry automated BioContainers addition for fastuniq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastuniq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastuniq:1.1--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastuniq/1.1--h470a237_1
$ module help quay.io/biocontainers/fastuniq/1.1--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastuniq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastuniq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastuniq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastuniq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastuniq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastuniq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastuniq

```bash
$ singularity exec <container> /usr/local/bin/fastuniq
$ podman run --it --rm --entrypoint /usr/local/bin/fastuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastuniq   -v ${PWD} -w ${PWD} <container> -c " $@"
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