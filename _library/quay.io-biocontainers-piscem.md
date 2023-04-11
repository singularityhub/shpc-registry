---
layout: container
name:  "quay.io/biocontainers/piscem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piscem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piscem/container.yaml"
updated_at: "2023-04-11 03:13:08.144769"
latest: "0.4.3--h52b76fa_0"
container_url: "https://biocontainers.pro/tools/piscem"
aliases:
 - "piscem"
versions:
 - "0.4.3--h52b76fa_0"
description: "singularity registry hpc automated addition for piscem"
config: {"url": "https://biocontainers.pro/tools/piscem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for piscem", "latest": {"0.4.3--h52b76fa_0": "sha256:e69951f3697fc1c9b7b4ba5fa3b31c01db5a2e8d60f684d84587bb55339ce716"}, "tags": {"0.4.3--h52b76fa_0": "sha256:e69951f3697fc1c9b7b4ba5fa3b31c01db5a2e8d60f684d84587bb55339ce716"}, "docker": "quay.io/biocontainers/piscem", "aliases": {"piscem": "/usr/local/bin/piscem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piscem.
singularity registry hpc automated addition for piscem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piscem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piscem:0.4.3--h52b76fa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piscem/0.4.3--h52b76fa_0
$ module help quay.io/biocontainers/piscem/0.4.3--h52b76fa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piscem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piscem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piscem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piscem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piscem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piscem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### piscem

```bash
$ singularity exec <container> /usr/local/bin/piscem
$ podman run --it --rm --entrypoint /usr/local/bin/piscem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piscem   -v ${PWD} -w ${PWD} <container> -c " $@"
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