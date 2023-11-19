---
layout: container
name:  "quay.io/biocontainers/ont-modkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ont-modkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ont-modkit/container.yaml"
updated_at: "2023-11-19 02:52:03.186740"
latest: "0.2.1--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/ont-modkit"
aliases:
 - "modkit"
versions:
 - "0.2.0--hdcf5f25_0"
 - "0.2.1--hdcf5f25_0"
description: "singularity registry hpc automated addition for ont-modkit"
config: {"url": "https://biocontainers.pro/tools/ont-modkit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ont-modkit", "latest": {"0.2.1--hdcf5f25_0": "sha256:9652585587fd7d2d32bd6aa36b9e656adc43c8460405ec4d1cf2d63d43b25dc5"}, "tags": {"0.2.0--hdcf5f25_0": "sha256:07de6449e8476fb37b1ff4ba431386fe33313c54a88d8840402c87887affd90e", "0.2.1--hdcf5f25_0": "sha256:9652585587fd7d2d32bd6aa36b9e656adc43c8460405ec4d1cf2d63d43b25dc5"}, "docker": "quay.io/biocontainers/ont-modkit", "aliases": {"modkit": "/usr/local/bin/modkit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ont-modkit.
singularity registry hpc automated addition for ont-modkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ont-modkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ont-modkit:0.2.1--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ont-modkit/0.2.1--hdcf5f25_0
$ module help quay.io/biocontainers/ont-modkit/0.2.1--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ont-modkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ont-modkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ont-modkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ont-modkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ont-modkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ont-modkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### modkit

```bash
$ singularity exec <container> /usr/local/bin/modkit
$ podman run --it --rm --entrypoint /usr/local/bin/modkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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