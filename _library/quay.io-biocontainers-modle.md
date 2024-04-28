---
layout: container
name:  "quay.io/biocontainers/modle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/modle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/modle/container.yaml"
updated_at: "2024-04-28 03:03:25.055865"
latest: "1.1.0--h63853f4_0"
container_url: "https://biocontainers.pro/tools/modle"
aliases:
 - "modle"
 - "modle_tools"
versions:
 - "1.0.0--h87f3376_0"
 - "1.0.1--h87f3376_0"
 - "1.1.0--h63853f4_0"
description: "singularity registry hpc automated addition for modle"
config: {"url": "https://biocontainers.pro/tools/modle", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for modle", "latest": {"1.1.0--h63853f4_0": "sha256:f20c6df66f43c63e7ea2221d38de0b0747f035d54b06c5e5b7f302e49952e8a8"}, "tags": {"1.0.0--h87f3376_0": "sha256:66c28fc5e73fcb3824f740c5aaf7e7426cee6a1b1a451db713eafd6f0ba0f319", "1.0.1--h87f3376_0": "sha256:482e9f5437c4e9ca2874fde2fb2217fde733d891d612320da4eea79e212c5d83", "1.1.0--h63853f4_0": "sha256:f20c6df66f43c63e7ea2221d38de0b0747f035d54b06c5e5b7f302e49952e8a8"}, "docker": "quay.io/biocontainers/modle", "aliases": {"modle": "/usr/local/bin/modle", "modle_tools": "/usr/local/bin/modle_tools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/modle.
singularity registry hpc automated addition for modle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/modle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/modle:1.1.0--h63853f4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/modle/1.1.0--h63853f4_0
$ module help quay.io/biocontainers/modle/1.1.0--h63853f4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### modle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### modle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### modle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### modle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### modle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### modle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### modle

```bash
$ singularity exec <container> /usr/local/bin/modle
$ podman run --it --rm --entrypoint /usr/local/bin/modle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modle_tools

```bash
$ singularity exec <container> /usr/local/bin/modle_tools
$ podman run --it --rm --entrypoint /usr/local/bin/modle_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modle_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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