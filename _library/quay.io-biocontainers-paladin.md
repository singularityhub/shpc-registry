---
layout: container
name:  "quay.io/biocontainers/paladin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paladin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paladin/container.yaml"
updated_at: "2025-08-24 03:40:36.985096"
latest: "1.4.6--h86e5fe9_6"
container_url: "https://biocontainers.pro/tools/paladin"
aliases:
 - "paladin"
versions:
 - "1.4.6--h41a57b0_3"
 - "1.4.6--h9bb4366_5"
 - "1.4.6--h86e5fe9_6"
description: "shpc-registry automated BioContainers addition for paladin"
config: {"url": "https://biocontainers.pro/tools/paladin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for paladin", "latest": {"1.4.6--h86e5fe9_6": "sha256:abe88c05916b32afa9bf372a1ad0e2f6569740c6c936ca6144dc701a170e7faf"}, "tags": {"1.4.6--h41a57b0_3": "sha256:e4afff1c8e0676c39d5d4deb39f02aefb3f81d2ff153aceb47554af1d6d92d41", "1.4.6--h9bb4366_5": "sha256:841ab0ba9a3c28a2aee66f185375972ce6101a9f8d3826b233be97a324c2503e", "1.4.6--h86e5fe9_6": "sha256:abe88c05916b32afa9bf372a1ad0e2f6569740c6c936ca6144dc701a170e7faf"}, "docker": "quay.io/biocontainers/paladin", "aliases": {"paladin": "/usr/local/bin/paladin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paladin.
shpc-registry automated BioContainers addition for paladin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paladin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paladin:1.4.6--h86e5fe9_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paladin/1.4.6--h86e5fe9_6
$ module help quay.io/biocontainers/paladin/1.4.6--h86e5fe9_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paladin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paladin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paladin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paladin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paladin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paladin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### paladin

```bash
$ singularity exec <container> /usr/local/bin/paladin
$ podman run --it --rm --entrypoint /usr/local/bin/paladin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paladin   -v ${PWD} -w ${PWD} <container> -c " $@"
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