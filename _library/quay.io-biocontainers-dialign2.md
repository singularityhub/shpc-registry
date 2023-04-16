---
layout: container
name:  "quay.io/biocontainers/dialign2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dialign2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dialign2/container.yaml"
updated_at: "2023-04-16 03:19:34.272961"
latest: "2.2.1--h9f5acd7_5"
container_url: "https://biocontainers.pro/tools/dialign2"
aliases:
 - "dialign2-2"
versions:
 - "2.2.1--h9f5acd7_5"
description: "shpc-registry automated BioContainers addition for dialign2"
config: {"url": "https://biocontainers.pro/tools/dialign2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dialign2", "latest": {"2.2.1--h9f5acd7_5": "sha256:a0676b93416e999a0495c04109031bf693443b1b6cbb66e17c4c1b8ebd1597a7"}, "tags": {"2.2.1--h9f5acd7_5": "sha256:a0676b93416e999a0495c04109031bf693443b1b6cbb66e17c4c1b8ebd1597a7"}, "docker": "quay.io/biocontainers/dialign2", "aliases": {"dialign2-2": "/usr/local/bin/dialign2-2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dialign2.
shpc-registry automated BioContainers addition for dialign2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dialign2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dialign2:2.2.1--h9f5acd7_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dialign2/2.2.1--h9f5acd7_5
$ module help quay.io/biocontainers/dialign2/2.2.1--h9f5acd7_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dialign2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dialign2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dialign2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dialign2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dialign2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dialign2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dialign2-2

```bash
$ singularity exec <container> /usr/local/bin/dialign2-2
$ podman run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
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