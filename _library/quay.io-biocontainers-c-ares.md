---
layout: container
name:  "quay.io/biocontainers/c-ares"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/c-ares/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/c-ares/container.yaml"
updated_at: "2024-05-23 02:50:05.616965"
latest: "1.11.0--h470a237_1"
container_url: "https://biocontainers.pro/tools/c-ares"

versions:
 - "1.11.0--h470a237_1"
description: "shpc-registry automated BioContainers addition for c-ares"
config: {"url": "https://biocontainers.pro/tools/c-ares", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for c-ares", "latest": {"1.11.0--h470a237_1": "sha256:006bbe729179eed0a33b1b98e9178a95a5fcd619c16ebb72503996cd6b2d529e"}, "tags": {"1.11.0--h470a237_1": "sha256:006bbe729179eed0a33b1b98e9178a95a5fcd619c16ebb72503996cd6b2d529e"}, "docker": "quay.io/biocontainers/c-ares"}
---

This module is a singularity container wrapper for quay.io/biocontainers/c-ares.
shpc-registry automated BioContainers addition for c-ares
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/c-ares
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/c-ares:1.11.0--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/c-ares/1.11.0--h470a237_1
$ module help quay.io/biocontainers/c-ares/1.11.0--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### c-ares-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### c-ares-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### c-ares-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### c-ares-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### c-ares-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### c-ares-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### c-ares

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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