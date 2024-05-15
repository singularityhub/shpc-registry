---
layout: container
name:  "quay.io/biocontainers/nanoplexer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoplexer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanoplexer/container.yaml"
updated_at: "2024-05-15 02:52:42.261005"
latest: "0.1.2--he4a0461_4"
container_url: "https://biocontainers.pro/tools/nanoplexer"
aliases:
 - "nanoplexer"
versions:
 - "0.1.2--h7132678_2"
 - "0.1.2--he4a0461_4"
description: "shpc-registry automated BioContainers addition for nanoplexer"
config: {"url": "https://biocontainers.pro/tools/nanoplexer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoplexer", "latest": {"0.1.2--he4a0461_4": "sha256:3ec4c6af4a9c440a9ebf52ec87785ccac4d6c192aa73f5c60413aceb89eb61fb"}, "tags": {"0.1.2--h7132678_2": "sha256:9d5ed38902c8878c6fb38a06ab3e9cd738d79a08ba18468a7f4e376ca1b6317e", "0.1.2--he4a0461_4": "sha256:3ec4c6af4a9c440a9ebf52ec87785ccac4d6c192aa73f5c60413aceb89eb61fb"}, "docker": "quay.io/biocontainers/nanoplexer", "aliases": {"nanoplexer": "/usr/local/bin/nanoplexer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoplexer.
shpc-registry automated BioContainers addition for nanoplexer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoplexer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoplexer:0.1.2--he4a0461_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoplexer/0.1.2--he4a0461_4
$ module help quay.io/biocontainers/nanoplexer/0.1.2--he4a0461_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoplexer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoplexer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoplexer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoplexer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoplexer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoplexer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nanoplexer

```bash
$ singularity exec <container> /usr/local/bin/nanoplexer
$ podman run --it --rm --entrypoint /usr/local/bin/nanoplexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanoplexer   -v ${PWD} -w ${PWD} <container> -c " $@"
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